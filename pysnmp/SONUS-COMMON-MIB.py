# SNMP MIB module (SONUS-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:49 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusSystemMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusSystemMIBs")

(SonusAccessLevel,
 SonusAdminState,
 SonusEventClass,
 SonusEventLevel,
 SonusEventString,
 SonusName,
 SonusNameReference,
 SonusTrapType) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAccessLevel",
    "SonusAdminState",
    "SonusEventClass",
    "SonusEventLevel",
    "SonusEventString",
    "SonusName",
    "SonusNameReference",
    "SonusTrapType")


# MODULE-IDENTITY

sonusCommonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusCommonMIBObjects_ObjectIdentity = ObjectIdentity
sonusCommonMIBObjects = _SonusCommonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1)
)
_SonusNetMgmt_ObjectIdentity = ObjectIdentity
sonusNetMgmt = _SonusNetMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1)
)
_SonusNetMgmtClient_ObjectIdentity = ObjectIdentity
sonusNetMgmtClient = _SonusNetMgmtClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1)
)


class _SonusNetMgmtClientNextIndex_Type(Integer32):
    """Custom type sonusNetMgmtClientNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusNetMgmtClientNextIndex_Type.__name__ = "Integer32"
_SonusNetMgmtClientNextIndex_Object = MibScalar
sonusNetMgmtClientNextIndex = _SonusNetMgmtClientNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 1),
    _SonusNetMgmtClientNextIndex_Type()
)
sonusNetMgmtClientNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNetMgmtClientNextIndex.setStatus("current")
_SonusNetMgmtClientTable_Object = MibTable
sonusNetMgmtClientTable = _SonusNetMgmtClientTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusNetMgmtClientTable.setStatus("current")
_SonusNetMgmtClientEntry_Object = MibTableRow
sonusNetMgmtClientEntry = _SonusNetMgmtClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1)
)
sonusNetMgmtClientEntry.setIndexNames(
    (0, "SONUS-COMMON-MIB", "sonusNetMgmtClientIndex"),
)
if mibBuilder.loadTexts:
    sonusNetMgmtClientEntry.setStatus("current")


class _SonusNetMgmtClientIndex_Type(Integer32):
    """Custom type sonusNetMgmtClientIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SonusNetMgmtClientIndex_Type.__name__ = "Integer32"
_SonusNetMgmtClientIndex_Object = MibTableColumn
sonusNetMgmtClientIndex = _SonusNetMgmtClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 1),
    _SonusNetMgmtClientIndex_Type()
)
sonusNetMgmtClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNetMgmtClientIndex.setStatus("current")
_SonusNetMgmtClientName_Type = SonusName
_SonusNetMgmtClientName_Object = MibTableColumn
sonusNetMgmtClientName = _SonusNetMgmtClientName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 2),
    _SonusNetMgmtClientName_Type()
)
sonusNetMgmtClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientName.setStatus("current")


class _SonusNetMgmtClientState_Type(SonusAdminState):
    """Custom type sonusNetMgmtClientState based on SonusAdminState"""


_SonusNetMgmtClientState_Object = MibTableColumn
sonusNetMgmtClientState = _SonusNetMgmtClientState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 3),
    _SonusNetMgmtClientState_Type()
)
sonusNetMgmtClientState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientState.setStatus("current")


class _SonusNetMgmtClientIpAddr_Type(IpAddress):
    """Custom type sonusNetMgmtClientIpAddr based on IpAddress"""
    defaultHexValue = "01010101"


_SonusNetMgmtClientIpAddr_Object = MibTableColumn
sonusNetMgmtClientIpAddr = _SonusNetMgmtClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 4),
    _SonusNetMgmtClientIpAddr_Type()
)
sonusNetMgmtClientIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientIpAddr.setStatus("current")


class _SonusNetMgmtClientAccess_Type(SonusAccessLevel):
    """Custom type sonusNetMgmtClientAccess based on SonusAccessLevel"""


_SonusNetMgmtClientAccess_Object = MibTableColumn
sonusNetMgmtClientAccess = _SonusNetMgmtClientAccess_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 5),
    _SonusNetMgmtClientAccess_Type()
)
sonusNetMgmtClientAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientAccess.setStatus("current")


class _SonusNetMgmtClientSnmpCommunityGet_Type(DisplayString):
    """Custom type sonusNetMgmtClientSnmpCommunityGet based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusNetMgmtClientSnmpCommunityGet_Type.__name__ = "DisplayString"
_SonusNetMgmtClientSnmpCommunityGet_Object = MibTableColumn
sonusNetMgmtClientSnmpCommunityGet = _SonusNetMgmtClientSnmpCommunityGet_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 6),
    _SonusNetMgmtClientSnmpCommunityGet_Type()
)
sonusNetMgmtClientSnmpCommunityGet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientSnmpCommunityGet.setStatus("current")


class _SonusNetMgmtClientSnmpCommunitySet_Type(DisplayString):
    """Custom type sonusNetMgmtClientSnmpCommunitySet based on DisplayString"""
    defaultValue = OctetString("private")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusNetMgmtClientSnmpCommunitySet_Type.__name__ = "DisplayString"
_SonusNetMgmtClientSnmpCommunitySet_Object = MibTableColumn
sonusNetMgmtClientSnmpCommunitySet = _SonusNetMgmtClientSnmpCommunitySet_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 7),
    _SonusNetMgmtClientSnmpCommunitySet_Type()
)
sonusNetMgmtClientSnmpCommunitySet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientSnmpCommunitySet.setStatus("current")


class _SonusNetMgmtClientSnmpCommunityTrap_Type(DisplayString):
    """Custom type sonusNetMgmtClientSnmpCommunityTrap based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusNetMgmtClientSnmpCommunityTrap_Type.__name__ = "DisplayString"
_SonusNetMgmtClientSnmpCommunityTrap_Object = MibTableColumn
sonusNetMgmtClientSnmpCommunityTrap = _SonusNetMgmtClientSnmpCommunityTrap_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 8),
    _SonusNetMgmtClientSnmpCommunityTrap_Type()
)
sonusNetMgmtClientSnmpCommunityTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientSnmpCommunityTrap.setStatus("current")


class _SonusNetMgmtClientTrapState_Type(SonusAdminState):
    """Custom type sonusNetMgmtClientTrapState based on SonusAdminState"""


_SonusNetMgmtClientTrapState_Object = MibTableColumn
sonusNetMgmtClientTrapState = _SonusNetMgmtClientTrapState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 9),
    _SonusNetMgmtClientTrapState_Type()
)
sonusNetMgmtClientTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientTrapState.setStatus("current")
_SonusNetMgmtClientRowStatus_Type = RowStatus
_SonusNetMgmtClientRowStatus_Object = MibTableColumn
sonusNetMgmtClientRowStatus = _SonusNetMgmtClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 10),
    _SonusNetMgmtClientRowStatus_Type()
)
sonusNetMgmtClientRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientRowStatus.setStatus("current")


class _SonusNetMgmtClientTrapPort_Type(Integer32):
    """Custom type sonusNetMgmtClientTrapPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusNetMgmtClientTrapPort_Type.__name__ = "Integer32"
_SonusNetMgmtClientTrapPort_Object = MibTableColumn
sonusNetMgmtClientTrapPort = _SonusNetMgmtClientTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 11),
    _SonusNetMgmtClientTrapPort_Type()
)
sonusNetMgmtClientTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientTrapPort.setStatus("current")


class _SonusNetMgmtClientAllTraps_Type(SonusTrapType):
    """Custom type sonusNetMgmtClientAllTraps based on SonusTrapType"""


_SonusNetMgmtClientAllTraps_Object = MibTableColumn
sonusNetMgmtClientAllTraps = _SonusNetMgmtClientAllTraps_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 12),
    _SonusNetMgmtClientAllTraps_Type()
)
sonusNetMgmtClientAllTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientAllTraps.setStatus("current")


class _SonusNetMgmtClientInformReqTimeout_Type(Integer32):
    """Custom type sonusNetMgmtClientInformReqTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SonusNetMgmtClientInformReqTimeout_Type.__name__ = "Integer32"
_SonusNetMgmtClientInformReqTimeout_Object = MibTableColumn
sonusNetMgmtClientInformReqTimeout = _SonusNetMgmtClientInformReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 13),
    _SonusNetMgmtClientInformReqTimeout_Type()
)
sonusNetMgmtClientInformReqTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientInformReqTimeout.setStatus("current")


class _SonusNetMgmtClientInformReqRetries_Type(Integer32):
    """Custom type sonusNetMgmtClientInformReqRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SonusNetMgmtClientInformReqRetries_Type.__name__ = "Integer32"
_SonusNetMgmtClientInformReqRetries_Object = MibTableColumn
sonusNetMgmtClientInformReqRetries = _SonusNetMgmtClientInformReqRetries_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 14),
    _SonusNetMgmtClientInformReqRetries_Type()
)
sonusNetMgmtClientInformReqRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientInformReqRetries.setStatus("current")


class _SonusNetMgmtClientInformReqMaxQueue_Type(Integer32):
    """Custom type sonusNetMgmtClientInformReqMaxQueue based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SonusNetMgmtClientInformReqMaxQueue_Type.__name__ = "Integer32"
_SonusNetMgmtClientInformReqMaxQueue_Object = MibTableColumn
sonusNetMgmtClientInformReqMaxQueue = _SonusNetMgmtClientInformReqMaxQueue_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 2, 1, 15),
    _SonusNetMgmtClientInformReqMaxQueue_Type()
)
sonusNetMgmtClientInformReqMaxQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtClientInformReqMaxQueue.setStatus("current")
_SonusNetMgmtClientStatusTable_Object = MibTable
sonusNetMgmtClientStatusTable = _SonusNetMgmtClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sonusNetMgmtClientStatusTable.setStatus("current")
_SonusNetMgmtClientStatusEntry_Object = MibTableRow
sonusNetMgmtClientStatusEntry = _SonusNetMgmtClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 3, 1)
)
sonusNetMgmtClientStatusEntry.setIndexNames(
    (0, "SONUS-COMMON-MIB", "sonusNetMgmtClientStatusIndex"),
)
if mibBuilder.loadTexts:
    sonusNetMgmtClientStatusEntry.setStatus("current")


class _SonusNetMgmtClientStatusIndex_Type(Integer32):
    """Custom type sonusNetMgmtClientStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SonusNetMgmtClientStatusIndex_Type.__name__ = "Integer32"
_SonusNetMgmtClientStatusIndex_Object = MibTableColumn
sonusNetMgmtClientStatusIndex = _SonusNetMgmtClientStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 3, 1, 1),
    _SonusNetMgmtClientStatusIndex_Type()
)
sonusNetMgmtClientStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusNetMgmtClientStatusIndex.setStatus("current")
_SonusNetMgmtClientStatusLastConfigChange_Type = DateAndTime
_SonusNetMgmtClientStatusLastConfigChange_Object = MibTableColumn
sonusNetMgmtClientStatusLastConfigChange = _SonusNetMgmtClientStatusLastConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 1, 3, 1, 2),
    _SonusNetMgmtClientStatusLastConfigChange_Type()
)
sonusNetMgmtClientStatusLastConfigChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNetMgmtClientStatusLastConfigChange.setStatus("current")
_SonusNetMgmtTrap_ObjectIdentity = ObjectIdentity
sonusNetMgmtTrap = _SonusNetMgmtTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2)
)
_SonusNetMgmtTrapNextIndex_ObjectIdentity = ObjectIdentity
sonusNetMgmtTrapNextIndex = _SonusNetMgmtTrapNextIndex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 1)
)
_SonusNetMgmtTrapTable_Object = MibTable
sonusNetMgmtTrapTable = _SonusNetMgmtTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sonusNetMgmtTrapTable.setStatus("current")
_SonusNetMgmtTrapEntry_Object = MibTableRow
sonusNetMgmtTrapEntry = _SonusNetMgmtTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1)
)
sonusNetMgmtTrapEntry.setIndexNames(
    (0, "SONUS-COMMON-MIB", "sonusNetMgmtTrapIndex"),
)
if mibBuilder.loadTexts:
    sonusNetMgmtTrapEntry.setStatus("current")


class _SonusNetMgmtTrapIndex_Type(Integer32):
    """Custom type sonusNetMgmtTrapIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusNetMgmtTrapIndex_Type.__name__ = "Integer32"
_SonusNetMgmtTrapIndex_Object = MibTableColumn
sonusNetMgmtTrapIndex = _SonusNetMgmtTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 1),
    _SonusNetMgmtTrapIndex_Type()
)
sonusNetMgmtTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusNetMgmtTrapIndex.setStatus("current")
_SonusNetMgmtTrapName_Type = SonusName
_SonusNetMgmtTrapName_Object = MibTableColumn
sonusNetMgmtTrapName = _SonusNetMgmtTrapName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 2),
    _SonusNetMgmtTrapName_Type()
)
sonusNetMgmtTrapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNetMgmtTrapName.setStatus("current")


class _SonusNetMgmtTrapMIBName_Type(DisplayString):
    """Custom type sonusNetMgmtTrapMIBName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SonusNetMgmtTrapMIBName_Type.__name__ = "DisplayString"
_SonusNetMgmtTrapMIBName_Object = MibTableColumn
sonusNetMgmtTrapMIBName = _SonusNetMgmtTrapMIBName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 3),
    _SonusNetMgmtTrapMIBName_Type()
)
sonusNetMgmtTrapMIBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNetMgmtTrapMIBName.setStatus("obsolete")
_SonusNetMgmtTrapOID_Type = ObjectIdentifier
_SonusNetMgmtTrapOID_Object = MibTableColumn
sonusNetMgmtTrapOID = _SonusNetMgmtTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 4),
    _SonusNetMgmtTrapOID_Type()
)
sonusNetMgmtTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNetMgmtTrapOID.setStatus("current")


class _SonusNetMgmtTrapClass_Type(SonusEventClass):
    """Custom type sonusNetMgmtTrapClass based on SonusEventClass"""


_SonusNetMgmtTrapClass_Object = MibTableColumn
sonusNetMgmtTrapClass = _SonusNetMgmtTrapClass_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 5),
    _SonusNetMgmtTrapClass_Type()
)
sonusNetMgmtTrapClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNetMgmtTrapClass.setStatus("current")


class _SonusNetMgmtTrapLevel_Type(SonusEventLevel):
    """Custom type sonusNetMgmtTrapLevel based on SonusEventLevel"""


_SonusNetMgmtTrapLevel_Object = MibTableColumn
sonusNetMgmtTrapLevel = _SonusNetMgmtTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 6),
    _SonusNetMgmtTrapLevel_Type()
)
sonusNetMgmtTrapLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNetMgmtTrapLevel.setStatus("current")


class _SonusNetMgmtTrapState_Type(SonusAdminState):
    """Custom type sonusNetMgmtTrapState based on SonusAdminState"""


_SonusNetMgmtTrapState_Object = MibTableColumn
sonusNetMgmtTrapState = _SonusNetMgmtTrapState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 2, 2, 1, 7),
    _SonusNetMgmtTrapState_Type()
)
sonusNetMgmtTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtTrapState.setStatus("current")
_SonusNetMgmtNotify_ObjectIdentity = ObjectIdentity
sonusNetMgmtNotify = _SonusNetMgmtNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3)
)


class _SonusNetMgmtNotifyNextIndex_Type(Integer32):
    """Custom type sonusNetMgmtNotifyNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusNetMgmtNotifyNextIndex_Type.__name__ = "Integer32"
_SonusNetMgmtNotifyNextIndex_Object = MibScalar
sonusNetMgmtNotifyNextIndex = _SonusNetMgmtNotifyNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 1),
    _SonusNetMgmtNotifyNextIndex_Type()
)
sonusNetMgmtNotifyNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNetMgmtNotifyNextIndex.setStatus("current")
_SonusNetMgmtNotifyTable_Object = MibTable
sonusNetMgmtNotifyTable = _SonusNetMgmtNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    sonusNetMgmtNotifyTable.setStatus("current")
_SonusNetMgmtNotifyEntry_Object = MibTableRow
sonusNetMgmtNotifyEntry = _SonusNetMgmtNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1)
)
sonusNetMgmtNotifyEntry.setIndexNames(
    (0, "SONUS-COMMON-MIB", "sonusNetMgmtNotifyIndex"),
)
if mibBuilder.loadTexts:
    sonusNetMgmtNotifyEntry.setStatus("current")


class _SonusNetMgmtNotifyIndex_Type(Integer32):
    """Custom type sonusNetMgmtNotifyIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusNetMgmtNotifyIndex_Type.__name__ = "Integer32"
_SonusNetMgmtNotifyIndex_Object = MibTableColumn
sonusNetMgmtNotifyIndex = _SonusNetMgmtNotifyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 1),
    _SonusNetMgmtNotifyIndex_Type()
)
sonusNetMgmtNotifyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusNetMgmtNotifyIndex.setStatus("current")
_SonusNetMgmtNotifyName_Type = SonusName
_SonusNetMgmtNotifyName_Object = MibTableColumn
sonusNetMgmtNotifyName = _SonusNetMgmtNotifyName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 2),
    _SonusNetMgmtNotifyName_Type()
)
sonusNetMgmtNotifyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtNotifyName.setStatus("current")
_SonusNetMgmtNotifyMgmtName_Type = SonusNameReference
_SonusNetMgmtNotifyMgmtName_Object = MibTableColumn
sonusNetMgmtNotifyMgmtName = _SonusNetMgmtNotifyMgmtName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 3),
    _SonusNetMgmtNotifyMgmtName_Type()
)
sonusNetMgmtNotifyMgmtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtNotifyMgmtName.setStatus("current")
_SonusNetMgmtNotifyTrapName_Type = SonusNameReference
_SonusNetMgmtNotifyTrapName_Object = MibTableColumn
sonusNetMgmtNotifyTrapName = _SonusNetMgmtNotifyTrapName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 4),
    _SonusNetMgmtNotifyTrapName_Type()
)
sonusNetMgmtNotifyTrapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtNotifyTrapName.setStatus("current")


class _SonusNetMgmtNotifyTrapType_Type(SonusTrapType):
    """Custom type sonusNetMgmtNotifyTrapType based on SonusTrapType"""


_SonusNetMgmtNotifyTrapType_Object = MibTableColumn
sonusNetMgmtNotifyTrapType = _SonusNetMgmtNotifyTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 5),
    _SonusNetMgmtNotifyTrapType_Type()
)
sonusNetMgmtNotifyTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtNotifyTrapType.setStatus("current")
_SonusNetMgmtNotifyRowStatus_Type = RowStatus
_SonusNetMgmtNotifyRowStatus_Object = MibTableColumn
sonusNetMgmtNotifyRowStatus = _SonusNetMgmtNotifyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 1, 1, 3, 2, 1, 6),
    _SonusNetMgmtNotifyRowStatus_Type()
)
sonusNetMgmtNotifyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNetMgmtNotifyRowStatus.setStatus("current")
_SonusCommonMIBNotifications_ObjectIdentity = ObjectIdentity
sonusCommonMIBNotifications = _SonusCommonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2)
)
_SonusCommonMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusCommonMIBNotificationsPrefix = _SonusCommonMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 0)
)
_SonusCommonMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusCommonMIBNotificationsObjects = _SonusCommonMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1)
)


class _SonusShelfIndex_Type(Integer32):
    """Custom type sonusShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusShelfIndex_Type.__name__ = "Integer32"
_SonusShelfIndex_Object = MibScalar
sonusShelfIndex = _SonusShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 1),
    _SonusShelfIndex_Type()
)
sonusShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusShelfIndex.setStatus("current")


class _SonusSlotIndex_Type(Integer32):
    """Custom type sonusSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusSlotIndex_Type.__name__ = "Integer32"
_SonusSlotIndex_Object = MibScalar
sonusSlotIndex = _SonusSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 2),
    _SonusSlotIndex_Type()
)
sonusSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSlotIndex.setStatus("current")


class _SonusPortIndex_Type(Integer32):
    """Custom type sonusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusPortIndex_Type.__name__ = "Integer32"
_SonusPortIndex_Object = MibScalar
sonusPortIndex = _SonusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 3),
    _SonusPortIndex_Type()
)
sonusPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPortIndex.setStatus("current")


class _SonusDs3Index_Type(Integer32):
    """Custom type sonusDs3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusDs3Index_Type.__name__ = "Integer32"
_SonusDs3Index_Object = MibScalar
sonusDs3Index = _SonusDs3Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 4),
    _SonusDs3Index_Type()
)
sonusDs3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs3Index.setStatus("current")


class _SonusDs1Index_Type(Integer32):
    """Custom type sonusDs1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusDs1Index_Type.__name__ = "Integer32"
_SonusDs1Index_Object = MibScalar
sonusDs1Index = _SonusDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 5),
    _SonusDs1Index_Type()
)
sonusDs1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusDs1Index.setStatus("current")
_SonusEventDescription_Type = SonusEventString
_SonusEventDescription_Object = MibScalar
sonusEventDescription = _SonusEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 6),
    _SonusEventDescription_Type()
)
sonusEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEventDescription.setStatus("current")
_SonusEventClass_Type = SonusEventClass
_SonusEventClass_Object = MibScalar
sonusEventClass = _SonusEventClass_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 7),
    _SonusEventClass_Type()
)
sonusEventClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEventClass.setStatus("current")
_SonusEventLevel_Type = SonusEventLevel
_SonusEventLevel_Object = MibScalar
sonusEventLevel = _SonusEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 8),
    _SonusEventLevel_Type()
)
sonusEventLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEventLevel.setStatus("current")
_SonusSequenceId_Type = Unsigned32
_SonusSequenceId_Object = MibScalar
sonusSequenceId = _SonusSequenceId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 9),
    _SonusSequenceId_Type()
)
sonusSequenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSequenceId.setStatus("current")
_SonusEventTime_Type = DateAndTime
_SonusEventTime_Object = MibScalar
sonusEventTime = _SonusEventTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 10),
    _SonusEventTime_Type()
)
sonusEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusEventTime.setStatus("current")


class _SonusNetMgmtInformReqDiscards_Type(Integer32):
    """Custom type sonusNetMgmtInformReqDiscards based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SonusNetMgmtInformReqDiscards_Type.__name__ = "Integer32"
_SonusNetMgmtInformReqDiscards_Object = MibScalar
sonusNetMgmtInformReqDiscards = _SonusNetMgmtInformReqDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 1, 11),
    _SonusNetMgmtInformReqDiscards_Type()
)
sonusNetMgmtInformReqDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNetMgmtInformReqDiscards.setStatus("current")

# Managed Objects groups


# Notification objects

sonusNetMgmtClientInformReqQueueFlushedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 0, 1)
)
sonusNetMgmtClientInformReqQueueFlushedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusNetMgmtClientName"),
        ("SONUS-COMMON-MIB", "sonusNetMgmtInformReqDiscards"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNetMgmtClientInformReqQueueFlushedNotification.setStatus(
        "current"
    )

sonusNetMgmtClientInformReqQueueFullNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 5, 2, 0, 2)
)
sonusNetMgmtClientInformReqQueueFullNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusNetMgmtClientName"),
        ("SONUS-COMMON-MIB", "sonusNetMgmtInformReqDiscards"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNetMgmtClientInformReqQueueFullNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-COMMON-MIB",
    **{"sonusCommonMIB": sonusCommonMIB,
       "sonusCommonMIBObjects": sonusCommonMIBObjects,
       "sonusNetMgmt": sonusNetMgmt,
       "sonusNetMgmtClient": sonusNetMgmtClient,
       "sonusNetMgmtClientNextIndex": sonusNetMgmtClientNextIndex,
       "sonusNetMgmtClientTable": sonusNetMgmtClientTable,
       "sonusNetMgmtClientEntry": sonusNetMgmtClientEntry,
       "sonusNetMgmtClientIndex": sonusNetMgmtClientIndex,
       "sonusNetMgmtClientName": sonusNetMgmtClientName,
       "sonusNetMgmtClientState": sonusNetMgmtClientState,
       "sonusNetMgmtClientIpAddr": sonusNetMgmtClientIpAddr,
       "sonusNetMgmtClientAccess": sonusNetMgmtClientAccess,
       "sonusNetMgmtClientSnmpCommunityGet": sonusNetMgmtClientSnmpCommunityGet,
       "sonusNetMgmtClientSnmpCommunitySet": sonusNetMgmtClientSnmpCommunitySet,
       "sonusNetMgmtClientSnmpCommunityTrap": sonusNetMgmtClientSnmpCommunityTrap,
       "sonusNetMgmtClientTrapState": sonusNetMgmtClientTrapState,
       "sonusNetMgmtClientRowStatus": sonusNetMgmtClientRowStatus,
       "sonusNetMgmtClientTrapPort": sonusNetMgmtClientTrapPort,
       "sonusNetMgmtClientAllTraps": sonusNetMgmtClientAllTraps,
       "sonusNetMgmtClientInformReqTimeout": sonusNetMgmtClientInformReqTimeout,
       "sonusNetMgmtClientInformReqRetries": sonusNetMgmtClientInformReqRetries,
       "sonusNetMgmtClientInformReqMaxQueue": sonusNetMgmtClientInformReqMaxQueue,
       "sonusNetMgmtClientStatusTable": sonusNetMgmtClientStatusTable,
       "sonusNetMgmtClientStatusEntry": sonusNetMgmtClientStatusEntry,
       "sonusNetMgmtClientStatusIndex": sonusNetMgmtClientStatusIndex,
       "sonusNetMgmtClientStatusLastConfigChange": sonusNetMgmtClientStatusLastConfigChange,
       "sonusNetMgmtTrap": sonusNetMgmtTrap,
       "sonusNetMgmtTrapNextIndex": sonusNetMgmtTrapNextIndex,
       "sonusNetMgmtTrapTable": sonusNetMgmtTrapTable,
       "sonusNetMgmtTrapEntry": sonusNetMgmtTrapEntry,
       "sonusNetMgmtTrapIndex": sonusNetMgmtTrapIndex,
       "sonusNetMgmtTrapName": sonusNetMgmtTrapName,
       "sonusNetMgmtTrapMIBName": sonusNetMgmtTrapMIBName,
       "sonusNetMgmtTrapOID": sonusNetMgmtTrapOID,
       "sonusNetMgmtTrapClass": sonusNetMgmtTrapClass,
       "sonusNetMgmtTrapLevel": sonusNetMgmtTrapLevel,
       "sonusNetMgmtTrapState": sonusNetMgmtTrapState,
       "sonusNetMgmtNotify": sonusNetMgmtNotify,
       "sonusNetMgmtNotifyNextIndex": sonusNetMgmtNotifyNextIndex,
       "sonusNetMgmtNotifyTable": sonusNetMgmtNotifyTable,
       "sonusNetMgmtNotifyEntry": sonusNetMgmtNotifyEntry,
       "sonusNetMgmtNotifyIndex": sonusNetMgmtNotifyIndex,
       "sonusNetMgmtNotifyName": sonusNetMgmtNotifyName,
       "sonusNetMgmtNotifyMgmtName": sonusNetMgmtNotifyMgmtName,
       "sonusNetMgmtNotifyTrapName": sonusNetMgmtNotifyTrapName,
       "sonusNetMgmtNotifyTrapType": sonusNetMgmtNotifyTrapType,
       "sonusNetMgmtNotifyRowStatus": sonusNetMgmtNotifyRowStatus,
       "sonusCommonMIBNotifications": sonusCommonMIBNotifications,
       "sonusCommonMIBNotificationsPrefix": sonusCommonMIBNotificationsPrefix,
       "sonusNetMgmtClientInformReqQueueFlushedNotification": sonusNetMgmtClientInformReqQueueFlushedNotification,
       "sonusNetMgmtClientInformReqQueueFullNotification": sonusNetMgmtClientInformReqQueueFullNotification,
       "sonusCommonMIBNotificationsObjects": sonusCommonMIBNotificationsObjects,
       "sonusShelfIndex": sonusShelfIndex,
       "sonusSlotIndex": sonusSlotIndex,
       "sonusPortIndex": sonusPortIndex,
       "sonusDs3Index": sonusDs3Index,
       "sonusDs1Index": sonusDs1Index,
       "sonusEventDescription": sonusEventDescription,
       "sonusEventClass": sonusEventClass,
       "sonusEventLevel": sonusEventLevel,
       "sonusSequenceId": sonusSequenceId,
       "sonusEventTime": sonusEventTime,
       "sonusNetMgmtInformReqDiscards": sonusNetMgmtInformReqDiscards}
)
