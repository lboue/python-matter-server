"""Various models and helpers for (custom) Matter clusters."""

from dataclasses import dataclass
from typing import ClassVar

from chip.clusters.ClusterObjects import (
    Cluster,
    ClusterAttributeDescriptor,
    ClusterObjectDescriptor,
    ClusterObjectFieldDescriptor,
)
from chip import ChipUtility
from chip.tlv import float32, uint


@dataclass
class EveEnergyCluster(Cluster):
    """Custom (vendor-specific) cluster for Eve Energy plug."""

    id: ClassVar[int] = 0x130AFC01

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(
                    Label="watt", Tag=0x130A000A, Type=float32
                ),
                ClusterObjectFieldDescriptor(
                    Label="wattAccumulated", Tag=0x130A000B, Type=float32
                ),
                ClusterObjectFieldDescriptor(
                    Label="wattAccumulatedControlPoint", Tag=0x130A000E, Type=float32
                ),
                ClusterObjectFieldDescriptor(
                    Label="voltage", Tag=0x130A0008, Type=float32
                ),
                ClusterObjectFieldDescriptor(
                    Label="current", Tag=0x130A0009, Type=float32
                ),
            ]
        )

    watt: float32 | None = None
    wattAccumulated: float32 | None = None
    wattAccumulatedControlPoint: float32 | None = None
    voltage: float32 | None = None
    current: float32 | None = None

    class Attributes:
        @dataclass
        class Watt(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x130AFC01

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x130A000A

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=float32)

            value: float32 = 0

        @dataclass
        class WattAccumulated(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x130AFC01

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x130A000B

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=float32)

            value: float32 = 0

        @dataclass
        class wattAccumulatedControlPoint(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x130AFC01

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x130A000E

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=float32)

            value: float32 = 0

        @dataclass
        class Voltage(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x130AFC01

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x130A0008

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=float32)

            value: float32 = 0

        @dataclass
        class Current(ClusterAttributeDescriptor):
            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0x130AFC01

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x130A0009

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=float32)

            value: float32 = 0

@dataclass
class WeatherStationCluster(Cluster):

    id: ClassVar[int] = 0xFFF1FEDC

    @ChipUtility.classproperty
    def descriptor(cls) -> ClusterObjectDescriptor:
        return ClusterObjectDescriptor(
            Fields=[
                ClusterObjectFieldDescriptor(
                    Label="windspeed", Tag=0x0000, Type=float32
                ),
                ClusterObjectFieldDescriptor(
                    Label="winddirection", Tag=0x0001, Type=float32
                ),
                ClusterObjectFieldDescriptor(
                    Label="rainfall", Tag=0x0002, Type=float32
                ),
            ]
        )

    windspeed: float32 | None = None
    winddirection: float32 | None = None
    rainfall: float32 | None = None

    class Attributes:

        @dataclass
        class WindSpeed(ClusterAttributeDescriptor):

            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0xFFF1FEDC

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x0000

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=float32)

            value: float32 = 0

        @dataclass
        class WindDirection(ClusterAttributeDescriptor):

            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0xFFF1FEDC

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x0001

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=float32)

            value: float32 = 0

        @dataclass
        class Rainfall(ClusterAttributeDescriptor):

            @ChipUtility.classproperty
            def cluster_id(cls) -> int:
                return 0xFFF1FEDC

            @ChipUtility.classproperty
            def attribute_id(cls) -> int:
                return 0x0002

            @ChipUtility.classproperty
            def attribute_type(cls) -> ClusterObjectFieldDescriptor:
                return ClusterObjectFieldDescriptor(Type=float32)

            value: float32 = 0
