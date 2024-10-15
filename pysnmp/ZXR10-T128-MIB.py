# SNMP MIB module (ZXR10-T128-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-T128-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:09 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(AvailStatus,
 BoardType,
 BoolStatus,
 DisplayString,
 MasterStatus,
 NpcType,
 OperStatus,
 PidUsedStatus,
 PortType,
 PortWorkingType,
 ShelfAttrib,
 UnitRunStatus,
 zxr10,
 zxr10PosInRack,
 zxr10RackNo,
 zxr10rack) = mibBuilder.importSymbols(
    "ZXR10-MIB",
    "AvailStatus",
    "BoardType",
    "BoolStatus",
    "DisplayString",
    "MasterStatus",
    "NpcType",
    "OperStatus",
    "PidUsedStatus",
    "PortType",
    "PortWorkingType",
    "ShelfAttrib",
    "UnitRunStatus",
    "zxr10",
    "zxr10PosInRack",
    "zxr10RackNo",
    "zxr10rack")


# MODULE-IDENTITY


# Types definitions



class AlarmType(Integer32):
    """Custom type AlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              129,
              130,
              131,
              132,
              133,
              134)
        )
    )
    namedValues = NamedValues(
        *(("hardware-board", 2),
          ("hardware-environment", 1),
          ("hardware-port", 3),
          ("softprotocol-arp", 78),
          ("softprotocol-bgp", 71),
          ("softprotocol-database", 66),
          ("softprotocol-drp", 72),
          ("softprotocol-icmp", 80),
          ("softprotocol-igmp", 75),
          ("softprotocol-ip", 74),
          ("softprotocol-isis", 79),
          ("softprotocol-oam", 67),
          ("softprotocol-ospf", 69),
          ("softprotocol-rip", 70),
          ("softprotocol-rmon", 82),
          ("softprotocol-ros", 65),
          ("softprotocol-security", 68),
          ("softprotocol-snmp", 81),
          ("softprotocol-tcp-udp", 73),
          ("softprotocol-telnet", 76),
          ("softprotocol-udp", 77),
          ("statistics-bgp", 134),
          ("statistics-icmp", 133),
          ("statistics-ip", 130),
          ("statistics-microcode", 129),
          ("statistics-tcp", 131),
          ("statistics-udp", 132))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zxr10shelfTable_Object = MibTable
zxr10shelfTable = _Zxr10shelfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 2)
)
if mibBuilder.loadTexts:
    zxr10shelfTable.setStatus("current")
_Zxr10shelfEntry_Object = MibTableRow
zxr10shelfEntry = _Zxr10shelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 2, 1)
)
zxr10shelfEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10RackNo"),
    (0, "ZXR10-T128-MIB", "zxr10ShelfNo"),
)
if mibBuilder.loadTexts:
    zxr10shelfEntry.setStatus("current")
_Zxr10ShelfNo_Type = Integer32
_Zxr10ShelfNo_Object = MibTableColumn
zxr10ShelfNo = _Zxr10ShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 2, 1, 1),
    _Zxr10ShelfNo_Type()
)
zxr10ShelfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ShelfNo.setStatus("current")
_Zxr10ShelfAttrib_Type = ShelfAttrib
_Zxr10ShelfAttrib_Object = MibTableColumn
zxr10ShelfAttrib = _Zxr10ShelfAttrib_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 2, 1, 2),
    _Zxr10ShelfAttrib_Type()
)
zxr10ShelfAttrib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ShelfAttrib.setStatus("current")
_Zxr10ShelfAvailStatus_Type = AvailStatus
_Zxr10ShelfAvailStatus_Object = MibTableColumn
zxr10ShelfAvailStatus = _Zxr10ShelfAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 2, 1, 3),
    _Zxr10ShelfAvailStatus_Type()
)
zxr10ShelfAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10ShelfAvailStatus.setStatus("current")
_Zxr10portTable_Object = MibTable
zxr10portTable = _Zxr10portTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4)
)
if mibBuilder.loadTexts:
    zxr10portTable.setStatus("current")
_Zxr10portEntry_Object = MibTableRow
zxr10portEntry = _Zxr10portEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1)
)
zxr10portEntry.setIndexNames(
    (0, "ZXR10-MIB", "zxr10RackNo"),
    (0, "ZXR10-T128-MIB", "zxr10ShelfNo"),
    (0, "ZXR10-MIB", "zxr10PosInRack"),
    (0, "ZXR10-T128-MIB", "zxr10PortNo"),
)
if mibBuilder.loadTexts:
    zxr10portEntry.setStatus("current")
_Zxr10PortIfIndex_Type = Integer32
_Zxr10PortIfIndex_Object = MibTableColumn
zxr10PortIfIndex = _Zxr10PortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 1),
    _Zxr10PortIfIndex_Type()
)
zxr10PortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortIfIndex.setStatus("current")
_Zxr10PortNo_Type = Integer32
_Zxr10PortNo_Object = MibTableColumn
zxr10PortNo = _Zxr10PortNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 2),
    _Zxr10PortNo_Type()
)
zxr10PortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortNo.setStatus("current")
_Zxr10PortType_Type = PortType
_Zxr10PortType_Object = MibTableColumn
zxr10PortType = _Zxr10PortType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 3),
    _Zxr10PortType_Type()
)
zxr10PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortType.setStatus("current")
_Zxr10PortWorkingType_Type = PortWorkingType
_Zxr10PortWorkingType_Object = MibTableColumn
zxr10PortWorkingType = _Zxr10PortWorkingType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 4),
    _Zxr10PortWorkingType_Type()
)
zxr10PortWorkingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortWorkingType.setStatus("current")
_Zxr10PortMTU_Type = Integer32
_Zxr10PortMTU_Object = MibTableColumn
zxr10PortMTU = _Zxr10PortMTU_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 5),
    _Zxr10PortMTU_Type()
)
zxr10PortMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortMTU.setStatus("current")


class _Zxr10PortSpeed_Type(DisplayString):
    """Custom type zxr10PortSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Zxr10PortSpeed_Type.__name__ = "DisplayString"
_Zxr10PortSpeed_Object = MibTableColumn
zxr10PortSpeed = _Zxr10PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 6),
    _Zxr10PortSpeed_Type()
)
zxr10PortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortSpeed.setStatus("current")
_Zxr10PortAvailStatus_Type = AvailStatus
_Zxr10PortAvailStatus_Object = MibTableColumn
zxr10PortAvailStatus = _Zxr10PortAvailStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 7),
    _Zxr10PortAvailStatus_Type()
)
zxr10PortAvailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortAvailStatus.setStatus("current")
_Zxr10PortOperStatus_Type = OperStatus
_Zxr10PortOperStatus_Object = MibTableColumn
zxr10PortOperStatus = _Zxr10PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 2, 4, 1, 8),
    _Zxr10PortOperStatus_Type()
)
zxr10PortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10PortOperStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-T128-MIB",
    **{"AlarmType": AlarmType,
       "zxr10shelfTable": zxr10shelfTable,
       "zxr10shelfEntry": zxr10shelfEntry,
       "zxr10ShelfNo": zxr10ShelfNo,
       "zxr10ShelfAttrib": zxr10ShelfAttrib,
       "zxr10ShelfAvailStatus": zxr10ShelfAvailStatus,
       "zxr10portTable": zxr10portTable,
       "zxr10portEntry": zxr10portEntry,
       "zxr10PortIfIndex": zxr10PortIfIndex,
       "zxr10PortNo": zxr10PortNo,
       "zxr10PortType": zxr10PortType,
       "zxr10PortWorkingType": zxr10PortWorkingType,
       "zxr10PortMTU": zxr10PortMTU,
       "zxr10PortSpeed": zxr10PortSpeed,
       "zxr10PortAvailStatus": zxr10PortAvailStatus,
       "zxr10PortOperStatus": zxr10PortOperStatus}
)
