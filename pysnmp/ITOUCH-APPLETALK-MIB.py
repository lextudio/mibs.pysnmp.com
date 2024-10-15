# SNMP MIB module (ITOUCH-APPLETALK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITOUCH-APPLETALK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:03 2024
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

(iTouch,) = mibBuilder.importSymbols(
    "ITOUCH-MIB",
    "iTouch")

(DdpAddress,) = mibBuilder.importSymbols(
    "RFC1243-MIB",
    "DdpAddress")

(charPortIndex,) = mibBuilder.importSymbols(
    "RFC1316-MIB",
    "charPortIndex")

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
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XApple_ObjectIdentity = ObjectIdentity
xApple = _XApple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 21)
)
_XAppleSystem_ObjectIdentity = ObjectIdentity
xAppleSystem = _XAppleSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 21, 1)
)


class _AppleState_Type(Integer32):
    """Custom type appleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AppleState_Type.__name__ = "Integer32"
_AppleState_Object = MibScalar
appleState = _AppleState_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 1, 1),
    _AppleState_Type()
)
appleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appleState.setStatus("mandatory")


class _AppleStatus_Type(Integer32):
    """Custom type appleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("badConfig", 4),
          ("disabled", 1),
          ("noInterface", 3),
          ("noInterfaceActive", 5))
    )


_AppleStatus_Type.__name__ = "Integer32"
_AppleStatus_Object = MibScalar
appleStatus = _AppleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 1, 2),
    _AppleStatus_Type()
)
appleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleStatus.setStatus("mandatory")
_AppleStatusIf_Type = Integer32
_AppleStatusIf_Object = MibScalar
appleStatusIf = _AppleStatusIf_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 1, 3),
    _AppleStatusIf_Type()
)
appleStatusIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleStatusIf.setStatus("mandatory")
_XApplePort_ObjectIdentity = ObjectIdentity
xApplePort = _XApplePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 21, 2)
)
_ApplePortTable_Object = MibTable
applePortTable = _ApplePortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1)
)
if mibBuilder.loadTexts:
    applePortTable.setStatus("mandatory")
_ApplePortEntry_Object = MibTableRow
applePortEntry = _ApplePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1)
)
applePortEntry.setIndexNames(
    (0, "ITOUCH-APPLETALK-MIB", "applePortIndex"),
)
if mibBuilder.loadTexts:
    applePortEntry.setStatus("mandatory")
_ApplePortIndex_Type = Integer32
_ApplePortIndex_Object = MibTableColumn
applePortIndex = _ApplePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 1),
    _ApplePortIndex_Type()
)
applePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortIndex.setStatus("mandatory")


class _ApplePortProtocolPriority_Type(Integer32):
    """Custom type applePortProtocolPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("high", 5),
          ("low", 1),
          ("medium", 3))
    )


_ApplePortProtocolPriority_Type.__name__ = "Integer32"
_ApplePortProtocolPriority_Object = MibTableColumn
applePortProtocolPriority = _ApplePortProtocolPriority_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 2),
    _ApplePortProtocolPriority_Type()
)
applePortProtocolPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortProtocolPriority.setStatus("mandatory")


class _ApplePortArpInterval_Type(Integer32):
    """Custom type applePortArpInterval based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33, 65535),
    )


_ApplePortArpInterval_Type.__name__ = "Integer32"
_ApplePortArpInterval_Object = MibTableColumn
applePortArpInterval = _ApplePortArpInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 3),
    _ApplePortArpInterval_Type()
)
applePortArpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortArpInterval.setStatus("mandatory")


class _ApplePortArpRetransmitCount_Type(Integer32):
    """Custom type applePortArpRetransmitCount based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApplePortArpRetransmitCount_Type.__name__ = "Integer32"
_ApplePortArpRetransmitCount_Object = MibTableColumn
applePortArpRetransmitCount = _ApplePortArpRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 4),
    _ApplePortArpRetransmitCount_Type()
)
applePortArpRetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortArpRetransmitCount.setStatus("mandatory")


class _ApplePortChecksum_Type(Integer32):
    """Custom type applePortChecksum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ApplePortChecksum_Type.__name__ = "Integer32"
_ApplePortChecksum_Object = MibTableColumn
applePortChecksum = _ApplePortChecksum_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 5),
    _ApplePortChecksum_Type()
)
applePortChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortChecksum.setStatus("mandatory")
_ApplePortPacketsIn_Type = Counter32
_ApplePortPacketsIn_Object = MibTableColumn
applePortPacketsIn = _ApplePortPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 6),
    _ApplePortPacketsIn_Type()
)
applePortPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortPacketsIn.setStatus("mandatory")
_ApplePortPacketsOut_Type = Counter32
_ApplePortPacketsOut_Object = MibTableColumn
applePortPacketsOut = _ApplePortPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 7),
    _ApplePortPacketsOut_Type()
)
applePortPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortPacketsOut.setStatus("mandatory")
_ApplePortForwardsIn_Type = Counter32
_ApplePortForwardsIn_Object = MibTableColumn
applePortForwardsIn = _ApplePortForwardsIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 8),
    _ApplePortForwardsIn_Type()
)
applePortForwardsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortForwardsIn.setStatus("mandatory")
_ApplePortForwardsOut_Type = Counter32
_ApplePortForwardsOut_Object = MibTableColumn
applePortForwardsOut = _ApplePortForwardsOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 9),
    _ApplePortForwardsOut_Type()
)
applePortForwardsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortForwardsOut.setStatus("mandatory")
_ApplePortNetAddress_Type = DdpAddress
_ApplePortNetAddress_Object = MibTableColumn
applePortNetAddress = _ApplePortNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 10),
    _ApplePortNetAddress_Type()
)
applePortNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortNetAddress.setStatus("mandatory")


class _ApplePortNetStart_Type(OctetString):
    """Custom type applePortNetStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ApplePortNetStart_Type.__name__ = "OctetString"
_ApplePortNetStart_Object = MibTableColumn
applePortNetStart = _ApplePortNetStart_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 11),
    _ApplePortNetStart_Type()
)
applePortNetStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortNetStart.setStatus("mandatory")


class _ApplePortNetEnd_Type(OctetString):
    """Custom type applePortNetEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ApplePortNetEnd_Type.__name__ = "OctetString"
_ApplePortNetEnd_Object = MibTableColumn
applePortNetEnd = _ApplePortNetEnd_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 12),
    _ApplePortNetEnd_Type()
)
applePortNetEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortNetEnd.setStatus("mandatory")
_ApplePortErrors_Type = Counter32
_ApplePortErrors_Object = MibTableColumn
applePortErrors = _ApplePortErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 13),
    _ApplePortErrors_Type()
)
applePortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortErrors.setStatus("mandatory")


class _ApplePortLastError_Type(Integer32):
    """Custom type applePortLastError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("checksum", 2),
          ("hopCount", 3),
          ("noProtocol", 4),
          ("noRoute", 5),
          ("shortDDP", 6),
          ("tooLong", 7),
          ("tooShort", 8))
    )


_ApplePortLastError_Type.__name__ = "Integer32"
_ApplePortLastError_Object = MibTableColumn
applePortLastError = _ApplePortLastError_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 14),
    _ApplePortLastError_Type()
)
applePortLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortLastError.setStatus("mandatory")
_ApplePortLastErrorTime_Type = TimeTicks
_ApplePortLastErrorTime_Object = MibTableColumn
applePortLastErrorTime = _ApplePortLastErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 15),
    _ApplePortLastErrorTime_Type()
)
applePortLastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortLastErrorTime.setStatus("mandatory")


class _ApplePortLastErrorData_Type(OctetString):
    """Custom type applePortLastErrorData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_ApplePortLastErrorData_Type.__name__ = "OctetString"
_ApplePortLastErrorData_Object = MibTableColumn
applePortLastErrorData = _ApplePortLastErrorData_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 16),
    _ApplePortLastErrorData_Type()
)
applePortLastErrorData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortLastErrorData.setStatus("mandatory")


class _ApplePortBringBackTime_Type(Integer32):
    """Custom type applePortBringBackTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApplePortBringBackTime_Type.__name__ = "Integer32"
_ApplePortBringBackTime_Object = MibTableColumn
applePortBringBackTime = _ApplePortBringBackTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 17),
    _ApplePortBringBackTime_Type()
)
applePortBringBackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortBringBackTime.setStatus("mandatory")


class _ApplePortUseNeighborNotify_Type(Integer32):
    """Custom type applePortUseNeighborNotify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ApplePortUseNeighborNotify_Type.__name__ = "Integer32"
_ApplePortUseNeighborNotify_Object = MibTableColumn
applePortUseNeighborNotify = _ApplePortUseNeighborNotify_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 18),
    _ApplePortUseNeighborNotify_Type()
)
applePortUseNeighborNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortUseNeighborNotify.setStatus("mandatory")


class _ApplePortRouterType_Type(Integer32):
    """Custom type applePortRouterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_ApplePortRouterType_Type.__name__ = "Integer32"
_ApplePortRouterType_Object = MibTableColumn
applePortRouterType = _ApplePortRouterType_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 1, 1, 19),
    _ApplePortRouterType_Type()
)
applePortRouterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortRouterType.setStatus("mandatory")
_ApplePortZoneTable_Object = MibTable
applePortZoneTable = _ApplePortZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 2)
)
if mibBuilder.loadTexts:
    applePortZoneTable.setStatus("mandatory")
_ApplePortZoneEntry_Object = MibTableRow
applePortZoneEntry = _ApplePortZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 2, 1)
)
applePortZoneEntry.setIndexNames(
    (0, "ITOUCH-APPLETALK-MIB", "applePortZoneIndex"),
    (0, "ITOUCH-APPLETALK-MIB", "applePortZoneName"),
)
if mibBuilder.loadTexts:
    applePortZoneEntry.setStatus("mandatory")
_ApplePortZoneIndex_Type = Integer32
_ApplePortZoneIndex_Object = MibTableColumn
applePortZoneIndex = _ApplePortZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 2, 1, 1),
    _ApplePortZoneIndex_Type()
)
applePortZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortZoneIndex.setStatus("mandatory")


class _ApplePortZoneName_Type(OctetString):
    """Custom type applePortZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_ApplePortZoneName_Type.__name__ = "OctetString"
_ApplePortZoneName_Object = MibTableColumn
applePortZoneName = _ApplePortZoneName_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 2, 1, 2),
    _ApplePortZoneName_Type()
)
applePortZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortZoneName.setStatus("mandatory")


class _ApplePortZoneStatus_Type(Integer32):
    """Custom type applePortZoneStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ApplePortZoneStatus_Type.__name__ = "Integer32"
_ApplePortZoneStatus_Object = MibTableColumn
applePortZoneStatus = _ApplePortZoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 2, 2, 1, 3),
    _ApplePortZoneStatus_Type()
)
applePortZoneStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortZoneStatus.setStatus("mandatory")
_XApplePolicy_ObjectIdentity = ObjectIdentity
xApplePolicy = _XApplePolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 21, 3)
)
_ApplePortExportTable_Object = MibTable
applePortExportTable = _ApplePortExportTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 1)
)
if mibBuilder.loadTexts:
    applePortExportTable.setStatus("mandatory")
_ApplePortExportEntry_Object = MibTableRow
applePortExportEntry = _ApplePortExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 1, 1)
)
applePortExportEntry.setIndexNames(
    (0, "ITOUCH-APPLETALK-MIB", "applePortExportIndex"),
    (0, "ITOUCH-APPLETALK-MIB", "applePortExportZone"),
    (0, "ITOUCH-APPLETALK-MIB", "applePortExportName"),
    (0, "ITOUCH-APPLETALK-MIB", "applePortExportType"),
)
if mibBuilder.loadTexts:
    applePortExportEntry.setStatus("mandatory")
_ApplePortExportIndex_Type = Integer32
_ApplePortExportIndex_Object = MibTableColumn
applePortExportIndex = _ApplePortExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 1, 1, 1),
    _ApplePortExportIndex_Type()
)
applePortExportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortExportIndex.setStatus("mandatory")


class _ApplePortExportZone_Type(OctetString):
    """Custom type applePortExportZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApplePortExportZone_Type.__name__ = "OctetString"
_ApplePortExportZone_Object = MibTableColumn
applePortExportZone = _ApplePortExportZone_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 1, 1, 2),
    _ApplePortExportZone_Type()
)
applePortExportZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortExportZone.setStatus("mandatory")


class _ApplePortExportName_Type(OctetString):
    """Custom type applePortExportName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApplePortExportName_Type.__name__ = "OctetString"
_ApplePortExportName_Object = MibTableColumn
applePortExportName = _ApplePortExportName_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 1, 1, 3),
    _ApplePortExportName_Type()
)
applePortExportName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortExportName.setStatus("mandatory")


class _ApplePortExportType_Type(OctetString):
    """Custom type applePortExportType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApplePortExportType_Type.__name__ = "OctetString"
_ApplePortExportType_Object = MibTableColumn
applePortExportType = _ApplePortExportType_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 1, 1, 4),
    _ApplePortExportType_Type()
)
applePortExportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortExportType.setStatus("mandatory")


class _ApplePortExportAction_Type(Integer32):
    """Custom type applePortExportAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("hide", 1))
    )


_ApplePortExportAction_Type.__name__ = "Integer32"
_ApplePortExportAction_Object = MibTableColumn
applePortExportAction = _ApplePortExportAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 1, 1, 5),
    _ApplePortExportAction_Type()
)
applePortExportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortExportAction.setStatus("mandatory")


class _ApplePortExportStatus_Type(Integer32):
    """Custom type applePortExportStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ApplePortExportStatus_Type.__name__ = "Integer32"
_ApplePortExportStatus_Object = MibTableColumn
applePortExportStatus = _ApplePortExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 1, 1, 6),
    _ApplePortExportStatus_Type()
)
applePortExportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortExportStatus.setStatus("mandatory")
_ApplePortImportTable_Object = MibTable
applePortImportTable = _ApplePortImportTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 2)
)
if mibBuilder.loadTexts:
    applePortImportTable.setStatus("mandatory")
_ApplePortImportEntry_Object = MibTableRow
applePortImportEntry = _ApplePortImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 2, 1)
)
applePortImportEntry.setIndexNames(
    (0, "ITOUCH-APPLETALK-MIB", "applePortImportIndex"),
    (0, "ITOUCH-APPLETALK-MIB", "applePortImportZone"),
    (0, "ITOUCH-APPLETALK-MIB", "applePortImportName"),
    (0, "ITOUCH-APPLETALK-MIB", "applePortImportType"),
)
if mibBuilder.loadTexts:
    applePortImportEntry.setStatus("mandatory")
_ApplePortImportIndex_Type = Integer32
_ApplePortImportIndex_Object = MibTableColumn
applePortImportIndex = _ApplePortImportIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 2, 1, 1),
    _ApplePortImportIndex_Type()
)
applePortImportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortImportIndex.setStatus("mandatory")


class _ApplePortImportZone_Type(OctetString):
    """Custom type applePortImportZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApplePortImportZone_Type.__name__ = "OctetString"
_ApplePortImportZone_Object = MibTableColumn
applePortImportZone = _ApplePortImportZone_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 2, 1, 2),
    _ApplePortImportZone_Type()
)
applePortImportZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortImportZone.setStatus("mandatory")


class _ApplePortImportName_Type(OctetString):
    """Custom type applePortImportName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApplePortImportName_Type.__name__ = "OctetString"
_ApplePortImportName_Object = MibTableColumn
applePortImportName = _ApplePortImportName_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 2, 1, 3),
    _ApplePortImportName_Type()
)
applePortImportName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortImportName.setStatus("mandatory")


class _ApplePortImportType_Type(OctetString):
    """Custom type applePortImportType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApplePortImportType_Type.__name__ = "OctetString"
_ApplePortImportType_Object = MibTableColumn
applePortImportType = _ApplePortImportType_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 2, 1, 4),
    _ApplePortImportType_Type()
)
applePortImportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applePortImportType.setStatus("mandatory")


class _ApplePortImportAction_Type(Integer32):
    """Custom type applePortImportAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("discard", 1))
    )


_ApplePortImportAction_Type.__name__ = "Integer32"
_ApplePortImportAction_Object = MibTableColumn
applePortImportAction = _ApplePortImportAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 2, 1, 5),
    _ApplePortImportAction_Type()
)
applePortImportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortImportAction.setStatus("mandatory")


class _ApplePortImportStatus_Type(Integer32):
    """Custom type applePortImportStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ApplePortImportStatus_Type.__name__ = "Integer32"
_ApplePortImportStatus_Object = MibTableColumn
applePortImportStatus = _ApplePortImportStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 3, 2, 1, 6),
    _ApplePortImportStatus_Type()
)
applePortImportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applePortImportStatus.setStatus("mandatory")
_XAppleNbp_ObjectIdentity = ObjectIdentity
xAppleNbp = _XAppleNbp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 21, 4)
)
_AppleNbpTable_Object = MibTable
appleNbpTable = _AppleNbpTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 4, 1)
)
if mibBuilder.loadTexts:
    appleNbpTable.setStatus("mandatory")
_AppleNbpEntry_Object = MibTableRow
appleNbpEntry = _AppleNbpEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 4, 1, 1)
)
appleNbpEntry.setIndexNames(
    (0, "ITOUCH-APPLETALK-MIB", "appleNbpZone"),
    (0, "ITOUCH-APPLETALK-MIB", "appleNbpName"),
    (0, "ITOUCH-APPLETALK-MIB", "appleNbpType"),
)
if mibBuilder.loadTexts:
    appleNbpEntry.setStatus("mandatory")


class _AppleNbpZone_Type(OctetString):
    """Custom type appleNbpZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AppleNbpZone_Type.__name__ = "OctetString"
_AppleNbpZone_Object = MibTableColumn
appleNbpZone = _AppleNbpZone_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 4, 1, 1, 1),
    _AppleNbpZone_Type()
)
appleNbpZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleNbpZone.setStatus("mandatory")


class _AppleNbpName_Type(OctetString):
    """Custom type appleNbpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AppleNbpName_Type.__name__ = "OctetString"
_AppleNbpName_Object = MibTableColumn
appleNbpName = _AppleNbpName_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 4, 1, 1, 2),
    _AppleNbpName_Type()
)
appleNbpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleNbpName.setStatus("mandatory")


class _AppleNbpType_Type(OctetString):
    """Custom type appleNbpType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AppleNbpType_Type.__name__ = "OctetString"
_AppleNbpType_Object = MibTableColumn
appleNbpType = _AppleNbpType_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 4, 1, 1, 3),
    _AppleNbpType_Type()
)
appleNbpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleNbpType.setStatus("mandatory")
_AppleNbpNode_Type = DdpAddress
_AppleNbpNode_Object = MibTableColumn
appleNbpNode = _AppleNbpNode_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 4, 1, 1, 4),
    _AppleNbpNode_Type()
)
appleNbpNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleNbpNode.setStatus("mandatory")
_AppleNbpSocket_Type = Integer32
_AppleNbpSocket_Object = MibTableColumn
appleNbpSocket = _AppleNbpSocket_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 4, 1, 1, 5),
    _AppleNbpSocket_Type()
)
appleNbpSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleNbpSocket.setStatus("mandatory")
_XAppleTraffic_ObjectIdentity = ObjectIdentity
xAppleTraffic = _XAppleTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 21, 5)
)


class _AppleTrafficSort_Type(Integer32):
    """Custom type appleTrafficSort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_AppleTrafficSort_Type.__name__ = "Integer32"
_AppleTrafficSort_Object = MibScalar
appleTrafficSort = _AppleTrafficSort_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 5, 1),
    _AppleTrafficSort_Type()
)
appleTrafficSort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appleTrafficSort.setStatus("mandatory")
_AppleTrafficTable_Object = MibTable
appleTrafficTable = _AppleTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 5, 2)
)
if mibBuilder.loadTexts:
    appleTrafficTable.setStatus("mandatory")
_AppleTrafficEntry_Object = MibTableRow
appleTrafficEntry = _AppleTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 5, 2, 1)
)
appleTrafficEntry.setIndexNames(
    (0, "ITOUCH-APPLETALK-MIB", "appleTrafficIndex"),
)
if mibBuilder.loadTexts:
    appleTrafficEntry.setStatus("mandatory")
_AppleTrafficIndex_Type = Integer32
_AppleTrafficIndex_Object = MibTableColumn
appleTrafficIndex = _AppleTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 5, 2, 1, 1),
    _AppleTrafficIndex_Type()
)
appleTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleTrafficIndex.setStatus("mandatory")


class _AppleTrafficPercent_Type(Integer32):
    """Custom type appleTrafficPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AppleTrafficPercent_Type.__name__ = "Integer32"
_AppleTrafficPercent_Object = MibTableColumn
appleTrafficPercent = _AppleTrafficPercent_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 5, 2, 1, 2),
    _AppleTrafficPercent_Type()
)
appleTrafficPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleTrafficPercent.setStatus("mandatory")
_AppleTrafficDst_Type = DdpAddress
_AppleTrafficDst_Object = MibTableColumn
appleTrafficDst = _AppleTrafficDst_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 5, 2, 1, 3),
    _AppleTrafficDst_Type()
)
appleTrafficDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleTrafficDst.setStatus("mandatory")
_AppleTrafficSrc_Type = DdpAddress
_AppleTrafficSrc_Object = MibTableColumn
appleTrafficSrc = _AppleTrafficSrc_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 5, 2, 1, 4),
    _AppleTrafficSrc_Type()
)
appleTrafficSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleTrafficSrc.setStatus("mandatory")
_AppleTrafficIntf_Type = Integer32
_AppleTrafficIntf_Object = MibTableColumn
appleTrafficIntf = _AppleTrafficIntf_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 5, 2, 1, 5),
    _AppleTrafficIntf_Type()
)
appleTrafficIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appleTrafficIntf.setStatus("mandatory")


class _AppleTrafficMonitoring_Type(Integer32):
    """Custom type appleTrafficMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AppleTrafficMonitoring_Type.__name__ = "Integer32"
_AppleTrafficMonitoring_Object = MibScalar
appleTrafficMonitoring = _AppleTrafficMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 5, 3),
    _AppleTrafficMonitoring_Type()
)
appleTrafficMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appleTrafficMonitoring.setStatus("mandatory")
_XAppleRemoteAccess_ObjectIdentity = ObjectIdentity
xAppleRemoteAccess = _XAppleRemoteAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 21, 6)
)


class _ArapPassword_Type(DisplayString):
    """Custom type arapPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ArapPassword_Type.__name__ = "DisplayString"
_ArapPassword_Object = MibScalar
arapPassword = _ArapPassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 6, 1),
    _ArapPassword_Type()
)
arapPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arapPassword.setStatus("mandatory")


class _ArapDefaultZoneName_Type(DisplayString):
    """Custom type arapDefaultZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArapDefaultZoneName_Type.__name__ = "DisplayString"
_ArapDefaultZoneName_Object = MibScalar
arapDefaultZoneName = _ArapDefaultZoneName_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 6, 2),
    _ArapDefaultZoneName_Type()
)
arapDefaultZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arapDefaultZoneName.setStatus("mandatory")
_ArapPortTable_Object = MibTable
arapPortTable = _ArapPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 6, 3)
)
if mibBuilder.loadTexts:
    arapPortTable.setStatus("mandatory")
_ArapPortEntry_Object = MibTableRow
arapPortEntry = _ArapPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 6, 3, 1)
)
arapPortEntry.setIndexNames(
    (0, "RFC1316-MIB", "charPortIndex"),
)
if mibBuilder.loadTexts:
    arapPortEntry.setStatus("mandatory")


class _ArapPortEnabled_Type(Integer32):
    """Custom type arapPortEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ArapPortEnabled_Type.__name__ = "Integer32"
_ArapPortEnabled_Object = MibTableColumn
arapPortEnabled = _ArapPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 6, 3, 1, 1),
    _ArapPortEnabled_Type()
)
arapPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arapPortEnabled.setStatus("mandatory")


class _ArapPortZoneAccess_Type(Integer32):
    """Custom type arapPortZoneAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("local", 2),
          ("namedzone", 4),
          ("none", 3))
    )


_ArapPortZoneAccess_Type.__name__ = "Integer32"
_ArapPortZoneAccess_Object = MibTableColumn
arapPortZoneAccess = _ArapPortZoneAccess_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 6, 3, 1, 2),
    _ArapPortZoneAccess_Type()
)
arapPortZoneAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arapPortZoneAccess.setStatus("mandatory")


class _ArapPortZoneName_Type(DisplayString):
    """Custom type arapPortZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArapPortZoneName_Type.__name__ = "DisplayString"
_ArapPortZoneName_Object = MibTableColumn
arapPortZoneName = _ArapPortZoneName_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 6, 3, 1, 3),
    _ArapPortZoneName_Type()
)
arapPortZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arapPortZoneName.setStatus("mandatory")
_ArapPortMaxConnectTime_Type = Integer32
_ArapPortMaxConnectTime_Object = MibTableColumn
arapPortMaxConnectTime = _ArapPortMaxConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 6, 3, 1, 4),
    _ArapPortMaxConnectTime_Type()
)
arapPortMaxConnectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arapPortMaxConnectTime.setStatus("mandatory")


class _ArapPortGuestLoginsOk_Type(Integer32):
    """Custom type arapPortGuestLoginsOk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ArapPortGuestLoginsOk_Type.__name__ = "Integer32"
_ArapPortGuestLoginsOk_Object = MibTableColumn
arapPortGuestLoginsOk = _ArapPortGuestLoginsOk_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 6, 3, 1, 5),
    _ArapPortGuestLoginsOk_Type()
)
arapPortGuestLoginsOk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arapPortGuestLoginsOk.setStatus("mandatory")
_ArapPortTimeConnected_Type = Integer32
_ArapPortTimeConnected_Object = MibTableColumn
arapPortTimeConnected = _ArapPortTimeConnected_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 6, 3, 1, 6),
    _ArapPortTimeConnected_Type()
)
arapPortTimeConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arapPortTimeConnected.setStatus("mandatory")
_ArapPortTimeRemaining_Type = Integer32
_ArapPortTimeRemaining_Object = MibTableColumn
arapPortTimeRemaining = _ArapPortTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 33, 21, 6, 3, 1, 7),
    _ArapPortTimeRemaining_Type()
)
arapPortTimeRemaining.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arapPortTimeRemaining.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITOUCH-APPLETALK-MIB",
    **{"xApple": xApple,
       "xAppleSystem": xAppleSystem,
       "appleState": appleState,
       "appleStatus": appleStatus,
       "appleStatusIf": appleStatusIf,
       "xApplePort": xApplePort,
       "applePortTable": applePortTable,
       "applePortEntry": applePortEntry,
       "applePortIndex": applePortIndex,
       "applePortProtocolPriority": applePortProtocolPriority,
       "applePortArpInterval": applePortArpInterval,
       "applePortArpRetransmitCount": applePortArpRetransmitCount,
       "applePortChecksum": applePortChecksum,
       "applePortPacketsIn": applePortPacketsIn,
       "applePortPacketsOut": applePortPacketsOut,
       "applePortForwardsIn": applePortForwardsIn,
       "applePortForwardsOut": applePortForwardsOut,
       "applePortNetAddress": applePortNetAddress,
       "applePortNetStart": applePortNetStart,
       "applePortNetEnd": applePortNetEnd,
       "applePortErrors": applePortErrors,
       "applePortLastError": applePortLastError,
       "applePortLastErrorTime": applePortLastErrorTime,
       "applePortLastErrorData": applePortLastErrorData,
       "applePortBringBackTime": applePortBringBackTime,
       "applePortUseNeighborNotify": applePortUseNeighborNotify,
       "applePortRouterType": applePortRouterType,
       "applePortZoneTable": applePortZoneTable,
       "applePortZoneEntry": applePortZoneEntry,
       "applePortZoneIndex": applePortZoneIndex,
       "applePortZoneName": applePortZoneName,
       "applePortZoneStatus": applePortZoneStatus,
       "xApplePolicy": xApplePolicy,
       "applePortExportTable": applePortExportTable,
       "applePortExportEntry": applePortExportEntry,
       "applePortExportIndex": applePortExportIndex,
       "applePortExportZone": applePortExportZone,
       "applePortExportName": applePortExportName,
       "applePortExportType": applePortExportType,
       "applePortExportAction": applePortExportAction,
       "applePortExportStatus": applePortExportStatus,
       "applePortImportTable": applePortImportTable,
       "applePortImportEntry": applePortImportEntry,
       "applePortImportIndex": applePortImportIndex,
       "applePortImportZone": applePortImportZone,
       "applePortImportName": applePortImportName,
       "applePortImportType": applePortImportType,
       "applePortImportAction": applePortImportAction,
       "applePortImportStatus": applePortImportStatus,
       "xAppleNbp": xAppleNbp,
       "appleNbpTable": appleNbpTable,
       "appleNbpEntry": appleNbpEntry,
       "appleNbpZone": appleNbpZone,
       "appleNbpName": appleNbpName,
       "appleNbpType": appleNbpType,
       "appleNbpNode": appleNbpNode,
       "appleNbpSocket": appleNbpSocket,
       "xAppleTraffic": xAppleTraffic,
       "appleTrafficSort": appleTrafficSort,
       "appleTrafficTable": appleTrafficTable,
       "appleTrafficEntry": appleTrafficEntry,
       "appleTrafficIndex": appleTrafficIndex,
       "appleTrafficPercent": appleTrafficPercent,
       "appleTrafficDst": appleTrafficDst,
       "appleTrafficSrc": appleTrafficSrc,
       "appleTrafficIntf": appleTrafficIntf,
       "appleTrafficMonitoring": appleTrafficMonitoring,
       "xAppleRemoteAccess": xAppleRemoteAccess,
       "arapPassword": arapPassword,
       "arapDefaultZoneName": arapDefaultZoneName,
       "arapPortTable": arapPortTable,
       "arapPortEntry": arapPortEntry,
       "arapPortEnabled": arapPortEnabled,
       "arapPortZoneAccess": arapPortZoneAccess,
       "arapPortZoneName": arapPortZoneName,
       "arapPortMaxConnectTime": arapPortMaxConnectTime,
       "arapPortGuestLoginsOk": arapPortGuestLoginsOk,
       "arapPortTimeConnected": arapPortTimeConnected,
       "arapPortTimeRemaining": arapPortTimeRemaining}
)
