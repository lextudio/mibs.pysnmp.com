# SNMP MIB module (Unisphere-Data-PPPOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-PPPOE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:20 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,
 UsdNextIfIndex) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdPPPoEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18)
)
usdPPPoEMIB.setRevisions(
        ("2002-08-16 21:46",
         "2001-06-19 14:27",
         "2001-03-21 15:00",
         "2001-02-12 00:00",
         "2000-10-25 00:00",
         "1999-05-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdPPPoEObjects_ObjectIdentity = ObjectIdentity
usdPPPoEObjects = _UsdPPPoEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1)
)
_UsdPPPoEIfLayer_ObjectIdentity = ObjectIdentity
usdPPPoEIfLayer = _UsdPPPoEIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1)
)
_UsdPPPoENextIfIndex_Type = UsdNextIfIndex
_UsdPPPoENextIfIndex_Object = MibScalar
usdPPPoENextIfIndex = _UsdPPPoENextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 1),
    _UsdPPPoENextIfIndex_Type()
)
usdPPPoENextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoENextIfIndex.setStatus("current")
_UsdPPPoEIfTable_Object = MibTable
usdPPPoEIfTable = _UsdPPPoEIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdPPPoEIfTable.setStatus("current")
_UsdPPPoEIfEntry_Object = MibTableRow
usdPPPoEIfEntry = _UsdPPPoEIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1)
)
usdPPPoEIfEntry.setIndexNames(
    (0, "Unisphere-Data-PPPOE-MIB", "usdPPPoEIfIfIndex"),
)
if mibBuilder.loadTexts:
    usdPPPoEIfEntry.setStatus("current")
_UsdPPPoEIfIfIndex_Type = InterfaceIndex
_UsdPPPoEIfIfIndex_Object = MibTableColumn
usdPPPoEIfIfIndex = _UsdPPPoEIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 1),
    _UsdPPPoEIfIfIndex_Type()
)
usdPPPoEIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfIfIndex.setStatus("current")


class _UsdPPPoEIfMaxNumSessions_Type(Integer32):
    """Custom type usdPPPoEIfMaxNumSessions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65335),
    )


_UsdPPPoEIfMaxNumSessions_Type.__name__ = "Integer32"
_UsdPPPoEIfMaxNumSessions_Object = MibTableColumn
usdPPPoEIfMaxNumSessions = _UsdPPPoEIfMaxNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 2),
    _UsdPPPoEIfMaxNumSessions_Type()
)
usdPPPoEIfMaxNumSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoEIfMaxNumSessions.setStatus("current")
_UsdPPPoEIfRowStatus_Type = RowStatus
_UsdPPPoEIfRowStatus_Object = MibTableColumn
usdPPPoEIfRowStatus = _UsdPPPoEIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 3),
    _UsdPPPoEIfRowStatus_Type()
)
usdPPPoEIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoEIfRowStatus.setStatus("current")
_UsdPPPoEIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdPPPoEIfLowerIfIndex_Object = MibTableColumn
usdPPPoEIfLowerIfIndex = _UsdPPPoEIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 4),
    _UsdPPPoEIfLowerIfIndex_Type()
)
usdPPPoEIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoEIfLowerIfIndex.setStatus("current")


class _UsdPPPoEIfAcName_Type(DisplayString):
    """Custom type usdPPPoEIfAcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UsdPPPoEIfAcName_Type.__name__ = "DisplayString"
_UsdPPPoEIfAcName_Object = MibTableColumn
usdPPPoEIfAcName = _UsdPPPoEIfAcName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 5),
    _UsdPPPoEIfAcName_Type()
)
usdPPPoEIfAcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoEIfAcName.setStatus("current")


class _UsdPPPoEIfDupProtect_Type(UsdEnable):
    """Custom type usdPPPoEIfDupProtect based on UsdEnable"""


_UsdPPPoEIfDupProtect_Object = MibTableColumn
usdPPPoEIfDupProtect = _UsdPPPoEIfDupProtect_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 6),
    _UsdPPPoEIfDupProtect_Type()
)
usdPPPoEIfDupProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoEIfDupProtect.setStatus("current")


class _UsdPPPoEIfPADIFlag_Type(UsdEnable):
    """Custom type usdPPPoEIfPADIFlag based on UsdEnable"""


_UsdPPPoEIfPADIFlag_Object = MibTableColumn
usdPPPoEIfPADIFlag = _UsdPPPoEIfPADIFlag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 7),
    _UsdPPPoEIfPADIFlag_Type()
)
usdPPPoEIfPADIFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoEIfPADIFlag.setStatus("current")


class _UsdPPPoEIfAutoconfig_Type(UsdEnable):
    """Custom type usdPPPoEIfAutoconfig based on UsdEnable"""


_UsdPPPoEIfAutoconfig_Object = MibTableColumn
usdPPPoEIfAutoconfig = _UsdPPPoEIfAutoconfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 8),
    _UsdPPPoEIfAutoconfig_Type()
)
usdPPPoEIfAutoconfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoEIfAutoconfig.setStatus("current")
_UsdPPPoEIfStatsTable_Object = MibTable
usdPPPoEIfStatsTable = _UsdPPPoEIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3)
)
if mibBuilder.loadTexts:
    usdPPPoEIfStatsTable.setStatus("current")
_UsdPPPoEIfStatsEntry_Object = MibTableRow
usdPPPoEIfStatsEntry = _UsdPPPoEIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1)
)
usdPPPoEIfStatsEntry.setIndexNames(
    (0, "Unisphere-Data-PPPOE-MIB", "usdPPPoEIfIfIndex"),
)
if mibBuilder.loadTexts:
    usdPPPoEIfStatsEntry.setStatus("current")
_UsdPPPoEIfStatsRxPADI_Type = Counter32
_UsdPPPoEIfStatsRxPADI_Object = MibTableColumn
usdPPPoEIfStatsRxPADI = _UsdPPPoEIfStatsRxPADI_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 1),
    _UsdPPPoEIfStatsRxPADI_Type()
)
usdPPPoEIfStatsRxPADI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsRxPADI.setStatus("current")
_UsdPPPoEIfStatsTxPADO_Type = Counter32
_UsdPPPoEIfStatsTxPADO_Object = MibTableColumn
usdPPPoEIfStatsTxPADO = _UsdPPPoEIfStatsTxPADO_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 2),
    _UsdPPPoEIfStatsTxPADO_Type()
)
usdPPPoEIfStatsTxPADO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsTxPADO.setStatus("current")
_UsdPPPoEIfStatsRxPADR_Type = Counter32
_UsdPPPoEIfStatsRxPADR_Object = MibTableColumn
usdPPPoEIfStatsRxPADR = _UsdPPPoEIfStatsRxPADR_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 3),
    _UsdPPPoEIfStatsRxPADR_Type()
)
usdPPPoEIfStatsRxPADR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsRxPADR.setStatus("current")
_UsdPPPoEIfStatsTxPADS_Type = Counter32
_UsdPPPoEIfStatsTxPADS_Object = MibTableColumn
usdPPPoEIfStatsTxPADS = _UsdPPPoEIfStatsTxPADS_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 4),
    _UsdPPPoEIfStatsTxPADS_Type()
)
usdPPPoEIfStatsTxPADS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsTxPADS.setStatus("current")
_UsdPPPoEIfStatsRxPADT_Type = Counter32
_UsdPPPoEIfStatsRxPADT_Object = MibTableColumn
usdPPPoEIfStatsRxPADT = _UsdPPPoEIfStatsRxPADT_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 5),
    _UsdPPPoEIfStatsRxPADT_Type()
)
usdPPPoEIfStatsRxPADT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsRxPADT.setStatus("current")
_UsdPPPoEIfStatsTxPADT_Type = Counter32
_UsdPPPoEIfStatsTxPADT_Object = MibTableColumn
usdPPPoEIfStatsTxPADT = _UsdPPPoEIfStatsTxPADT_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 6),
    _UsdPPPoEIfStatsTxPADT_Type()
)
usdPPPoEIfStatsTxPADT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsTxPADT.setStatus("current")
_UsdPPPoEIfStatsRxInvVersion_Type = Counter32
_UsdPPPoEIfStatsRxInvVersion_Object = MibTableColumn
usdPPPoEIfStatsRxInvVersion = _UsdPPPoEIfStatsRxInvVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 7),
    _UsdPPPoEIfStatsRxInvVersion_Type()
)
usdPPPoEIfStatsRxInvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsRxInvVersion.setStatus("current")
_UsdPPPoEIfStatsRxInvCode_Type = Counter32
_UsdPPPoEIfStatsRxInvCode_Object = MibTableColumn
usdPPPoEIfStatsRxInvCode = _UsdPPPoEIfStatsRxInvCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 8),
    _UsdPPPoEIfStatsRxInvCode_Type()
)
usdPPPoEIfStatsRxInvCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsRxInvCode.setStatus("current")
_UsdPPPoEIfStatsRxInvTags_Type = Counter32
_UsdPPPoEIfStatsRxInvTags_Object = MibTableColumn
usdPPPoEIfStatsRxInvTags = _UsdPPPoEIfStatsRxInvTags_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 9),
    _UsdPPPoEIfStatsRxInvTags_Type()
)
usdPPPoEIfStatsRxInvTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsRxInvTags.setStatus("current")
_UsdPPPoEIfStatsRxInvSession_Type = Counter32
_UsdPPPoEIfStatsRxInvSession_Object = MibTableColumn
usdPPPoEIfStatsRxInvSession = _UsdPPPoEIfStatsRxInvSession_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 10),
    _UsdPPPoEIfStatsRxInvSession_Type()
)
usdPPPoEIfStatsRxInvSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsRxInvSession.setStatus("current")
_UsdPPPoEIfStatsRxInvTypes_Type = Counter32
_UsdPPPoEIfStatsRxInvTypes_Object = MibTableColumn
usdPPPoEIfStatsRxInvTypes = _UsdPPPoEIfStatsRxInvTypes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 11),
    _UsdPPPoEIfStatsRxInvTypes_Type()
)
usdPPPoEIfStatsRxInvTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsRxInvTypes.setStatus("current")
_UsdPPPoEIfStatsRxInvPackets_Type = Counter32
_UsdPPPoEIfStatsRxInvPackets_Object = MibTableColumn
usdPPPoEIfStatsRxInvPackets = _UsdPPPoEIfStatsRxInvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 12),
    _UsdPPPoEIfStatsRxInvPackets_Type()
)
usdPPPoEIfStatsRxInvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsRxInvPackets.setStatus("current")
_UsdPPPoEIfStatsRxInsufficientResources_Type = Counter32
_UsdPPPoEIfStatsRxInsufficientResources_Object = MibTableColumn
usdPPPoEIfStatsRxInsufficientResources = _UsdPPPoEIfStatsRxInsufficientResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 13),
    _UsdPPPoEIfStatsRxInsufficientResources_Type()
)
usdPPPoEIfStatsRxInsufficientResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsRxInsufficientResources.setStatus("current")
_UsdPPPoEIfStatsTxPADM_Type = Counter32
_UsdPPPoEIfStatsTxPADM_Object = MibTableColumn
usdPPPoEIfStatsTxPADM = _UsdPPPoEIfStatsTxPADM_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 14),
    _UsdPPPoEIfStatsTxPADM_Type()
)
usdPPPoEIfStatsTxPADM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEIfStatsTxPADM.setStatus("current")
_UsdPPPoESubIfLayer_ObjectIdentity = ObjectIdentity
usdPPPoESubIfLayer = _UsdPPPoESubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2)
)
_UsdPPPoESubIfNextIfIndex_Type = UsdNextIfIndex
_UsdPPPoESubIfNextIfIndex_Object = MibScalar
usdPPPoESubIfNextIfIndex = _UsdPPPoESubIfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 1),
    _UsdPPPoESubIfNextIfIndex_Type()
)
usdPPPoESubIfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESubIfNextIfIndex.setStatus("current")
_UsdPPPoESubIfTable_Object = MibTable
usdPPPoESubIfTable = _UsdPPPoESubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usdPPPoESubIfTable.setStatus("current")
_UsdPPPoESubIfEntry_Object = MibTableRow
usdPPPoESubIfEntry = _UsdPPPoESubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1)
)
usdPPPoESubIfEntry.setIndexNames(
    (0, "Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfIndex"),
)
if mibBuilder.loadTexts:
    usdPPPoESubIfEntry.setStatus("current")
_UsdPPPoESubIfIndex_Type = InterfaceIndex
_UsdPPPoESubIfIndex_Object = MibTableColumn
usdPPPoESubIfIndex = _UsdPPPoESubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 1),
    _UsdPPPoESubIfIndex_Type()
)
usdPPPoESubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPPPoESubIfIndex.setStatus("current")
_UsdPPPoESubIfRowStatus_Type = RowStatus
_UsdPPPoESubIfRowStatus_Object = MibTableColumn
usdPPPoESubIfRowStatus = _UsdPPPoESubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 2),
    _UsdPPPoESubIfRowStatus_Type()
)
usdPPPoESubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoESubIfRowStatus.setStatus("current")
_UsdPPPoESubIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdPPPoESubIfLowerIfIndex_Object = MibTableColumn
usdPPPoESubIfLowerIfIndex = _UsdPPPoESubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 3),
    _UsdPPPoESubIfLowerIfIndex_Type()
)
usdPPPoESubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoESubIfLowerIfIndex.setStatus("current")


class _UsdPPPoESubIfId_Type(Integer32):
    """Custom type usdPPPoESubIfId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UsdPPPoESubIfId_Type.__name__ = "Integer32"
_UsdPPPoESubIfId_Object = MibTableColumn
usdPPPoESubIfId = _UsdPPPoESubIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 4),
    _UsdPPPoESubIfId_Type()
)
usdPPPoESubIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoESubIfId.setStatus("current")


class _UsdPPPoESubIfSessionId_Type(Integer32):
    """Custom type usdPPPoESubIfSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdPPPoESubIfSessionId_Type.__name__ = "Integer32"
_UsdPPPoESubIfSessionId_Object = MibTableColumn
usdPPPoESubIfSessionId = _UsdPPPoESubIfSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 5),
    _UsdPPPoESubIfSessionId_Type()
)
usdPPPoESubIfSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESubIfSessionId.setStatus("current")


class _UsdPPPoESubIfMotm_Type(DisplayString):
    """Custom type usdPPPoESubIfMotm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UsdPPPoESubIfMotm_Type.__name__ = "DisplayString"
_UsdPPPoESubIfMotm_Object = MibTableColumn
usdPPPoESubIfMotm = _UsdPPPoESubIfMotm_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 6),
    _UsdPPPoESubIfMotm_Type()
)
usdPPPoESubIfMotm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoESubIfMotm.setStatus("current")


class _UsdPPPoESubIfUrl_Type(DisplayString):
    """Custom type usdPPPoESubIfUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UsdPPPoESubIfUrl_Type.__name__ = "DisplayString"
_UsdPPPoESubIfUrl_Object = MibTableColumn
usdPPPoESubIfUrl = _UsdPPPoESubIfUrl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 7),
    _UsdPPPoESubIfUrl_Type()
)
usdPPPoESubIfUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoESubIfUrl.setStatus("current")
_UsdPPPoEGlobal_ObjectIdentity = ObjectIdentity
usdPPPoEGlobal = _UsdPPPoEGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 3)
)


class _UsdPPPoEGlobalMotm_Type(DisplayString):
    """Custom type usdPPPoEGlobalMotm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UsdPPPoEGlobalMotm_Type.__name__ = "DisplayString"
_UsdPPPoEGlobalMotm_Object = MibScalar
usdPPPoEGlobalMotm = _UsdPPPoEGlobalMotm_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 3, 1),
    _UsdPPPoEGlobalMotm_Type()
)
usdPPPoEGlobalMotm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPPPoEGlobalMotm.setStatus("current")
_UsdPPPoEProfile_ObjectIdentity = ObjectIdentity
usdPPPoEProfile = _UsdPPPoEProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4)
)
_UsdPPPoEProfileTable_Object = MibTable
usdPPPoEProfileTable = _UsdPPPoEProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1)
)
if mibBuilder.loadTexts:
    usdPPPoEProfileTable.setStatus("deprecated")
_UsdPPPoEProfileEntry_Object = MibTableRow
usdPPPoEProfileEntry = _UsdPPPoEProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1)
)
usdPPPoEProfileEntry.setIndexNames(
    (0, "Unisphere-Data-PPPOE-MIB", "usdPPPoEProfileIndex"),
)
if mibBuilder.loadTexts:
    usdPPPoEProfileEntry.setStatus("deprecated")
_UsdPPPoEProfileIndex_Type = Unsigned32
_UsdPPPoEProfileIndex_Object = MibTableColumn
usdPPPoEProfileIndex = _UsdPPPoEProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1, 1),
    _UsdPPPoEProfileIndex_Type()
)
usdPPPoEProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPPPoEProfileIndex.setStatus("deprecated")
_UsdPPPoEProfileRowStatus_Type = RowStatus
_UsdPPPoEProfileRowStatus_Object = MibTableColumn
usdPPPoEProfileRowStatus = _UsdPPPoEProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1, 2),
    _UsdPPPoEProfileRowStatus_Type()
)
usdPPPoEProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoEProfileRowStatus.setStatus("deprecated")


class _UsdPPPoEProfileMotm_Type(DisplayString):
    """Custom type usdPPPoEProfileMotm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UsdPPPoEProfileMotm_Type.__name__ = "DisplayString"
_UsdPPPoEProfileMotm_Object = MibTableColumn
usdPPPoEProfileMotm = _UsdPPPoEProfileMotm_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1, 3),
    _UsdPPPoEProfileMotm_Type()
)
usdPPPoEProfileMotm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoEProfileMotm.setStatus("deprecated")


class _UsdPPPoEProfileUrl_Type(DisplayString):
    """Custom type usdPPPoEProfileUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UsdPPPoEProfileUrl_Type.__name__ = "DisplayString"
_UsdPPPoEProfileUrl_Object = MibTableColumn
usdPPPoEProfileUrl = _UsdPPPoEProfileUrl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1, 4),
    _UsdPPPoEProfileUrl_Type()
)
usdPPPoEProfileUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPPPoEProfileUrl.setStatus("deprecated")
_UsdPPPoESummary_ObjectIdentity = ObjectIdentity
usdPPPoESummary = _UsdPPPoESummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5)
)
_UsdPPPoEMajorInterfaceCount_Type = Integer32
_UsdPPPoEMajorInterfaceCount_Object = MibScalar
usdPPPoEMajorInterfaceCount = _UsdPPPoEMajorInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 1),
    _UsdPPPoEMajorInterfaceCount_Type()
)
usdPPPoEMajorInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoEMajorInterfaceCount.setStatus("current")
_UsdPPPoESummaryMajorIfAdminUp_Type = Integer32
_UsdPPPoESummaryMajorIfAdminUp_Object = MibScalar
usdPPPoESummaryMajorIfAdminUp = _UsdPPPoESummaryMajorIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 2),
    _UsdPPPoESummaryMajorIfAdminUp_Type()
)
usdPPPoESummaryMajorIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESummaryMajorIfAdminUp.setStatus("current")
_UsdPPPoESummaryMajorIfAdminDown_Type = Integer32
_UsdPPPoESummaryMajorIfAdminDown_Object = MibScalar
usdPPPoESummaryMajorIfAdminDown = _UsdPPPoESummaryMajorIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 3),
    _UsdPPPoESummaryMajorIfAdminDown_Type()
)
usdPPPoESummaryMajorIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESummaryMajorIfAdminDown.setStatus("current")
_UsdPPPoESummaryMajorIfOperUp_Type = Integer32
_UsdPPPoESummaryMajorIfOperUp_Object = MibScalar
usdPPPoESummaryMajorIfOperUp = _UsdPPPoESummaryMajorIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 4),
    _UsdPPPoESummaryMajorIfOperUp_Type()
)
usdPPPoESummaryMajorIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESummaryMajorIfOperUp.setStatus("current")
_UsdPPPoESummaryMajorIfOperDown_Type = Integer32
_UsdPPPoESummaryMajorIfOperDown_Object = MibScalar
usdPPPoESummaryMajorIfOperDown = _UsdPPPoESummaryMajorIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 5),
    _UsdPPPoESummaryMajorIfOperDown_Type()
)
usdPPPoESummaryMajorIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESummaryMajorIfOperDown.setStatus("current")
_UsdPPPoESummaryMajorIfLowerLayerDown_Type = Integer32
_UsdPPPoESummaryMajorIfLowerLayerDown_Object = MibScalar
usdPPPoESummaryMajorIfLowerLayerDown = _UsdPPPoESummaryMajorIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 6),
    _UsdPPPoESummaryMajorIfLowerLayerDown_Type()
)
usdPPPoESummaryMajorIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESummaryMajorIfLowerLayerDown.setStatus("current")
_UsdPPPoESummaryMajorIfNotPresent_Type = Integer32
_UsdPPPoESummaryMajorIfNotPresent_Object = MibScalar
usdPPPoESummaryMajorIfNotPresent = _UsdPPPoESummaryMajorIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 7),
    _UsdPPPoESummaryMajorIfNotPresent_Type()
)
usdPPPoESummaryMajorIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESummaryMajorIfNotPresent.setStatus("current")
_UsdPPPoESummarySubInterfaceCount_Type = Integer32
_UsdPPPoESummarySubInterfaceCount_Object = MibScalar
usdPPPoESummarySubInterfaceCount = _UsdPPPoESummarySubInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 8),
    _UsdPPPoESummarySubInterfaceCount_Type()
)
usdPPPoESummarySubInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESummarySubInterfaceCount.setStatus("current")
_UsdPPPoESummarySubIfAdminUp_Type = Integer32
_UsdPPPoESummarySubIfAdminUp_Object = MibScalar
usdPPPoESummarySubIfAdminUp = _UsdPPPoESummarySubIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 9),
    _UsdPPPoESummarySubIfAdminUp_Type()
)
usdPPPoESummarySubIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESummarySubIfAdminUp.setStatus("current")
_UsdPPPoESummarySubIfAdminDown_Type = Integer32
_UsdPPPoESummarySubIfAdminDown_Object = MibScalar
usdPPPoESummarySubIfAdminDown = _UsdPPPoESummarySubIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 10),
    _UsdPPPoESummarySubIfAdminDown_Type()
)
usdPPPoESummarySubIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESummarySubIfAdminDown.setStatus("current")
_UsdPPPoESummarySubIfOperUp_Type = Integer32
_UsdPPPoESummarySubIfOperUp_Object = MibScalar
usdPPPoESummarySubIfOperUp = _UsdPPPoESummarySubIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 11),
    _UsdPPPoESummarySubIfOperUp_Type()
)
usdPPPoESummarySubIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESummarySubIfOperUp.setStatus("current")
_UsdPPPoESummarySubIfOperDown_Type = Integer32
_UsdPPPoESummarySubIfOperDown_Object = MibScalar
usdPPPoESummarySubIfOperDown = _UsdPPPoESummarySubIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 12),
    _UsdPPPoESummarySubIfOperDown_Type()
)
usdPPPoESummarySubIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESummarySubIfOperDown.setStatus("current")
_UsdPPPoESummarySubIfLowerLayerDown_Type = Integer32
_UsdPPPoESummarySubIfLowerLayerDown_Object = MibScalar
usdPPPoESummarySubIfLowerLayerDown = _UsdPPPoESummarySubIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 13),
    _UsdPPPoESummarySubIfLowerLayerDown_Type()
)
usdPPPoESummarySubIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESummarySubIfLowerLayerDown.setStatus("current")
_UsdPPPoESummarySubIfNotPresent_Type = Integer32
_UsdPPPoESummarySubIfNotPresent_Object = MibScalar
usdPPPoESummarySubIfNotPresent = _UsdPPPoESummarySubIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 14),
    _UsdPPPoESummarySubIfNotPresent_Type()
)
usdPPPoESummarySubIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPPPoESummarySubIfNotPresent.setStatus("current")
_UsdPPPoEConformance_ObjectIdentity = ObjectIdentity
usdPPPoEConformance = _UsdPPPoEConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4)
)
_UsdPPPoEGroups_ObjectIdentity = ObjectIdentity
usdPPPoEGroups = _UsdPPPoEGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4)
)
_UsdPPPoECompliances_ObjectIdentity = ObjectIdentity
usdPPPoECompliances = _UsdPPPoECompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5)
)

# Managed Objects groups

usdPPPoEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 1)
)
usdPPPoEGroup.setObjects(
      *(("Unisphere-Data-PPPOE-MIB", "usdPPPoENextIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfMaxNumSessions"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfRowStatus"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfLowerIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADI"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADO"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADR"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADS"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADT"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADT"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvVersion"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvCode"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTags"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvSession"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTypes"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvPackets"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInsufficientResources"))
)
if mibBuilder.loadTexts:
    usdPPPoEGroup.setStatus("obsolete")

usdPPPoESubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 2)
)
usdPPPoESubIfGroup.setObjects(
      *(("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfNextIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfRowStatus"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfLowerIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfId"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfSessionId"))
)
if mibBuilder.loadTexts:
    usdPPPoESubIfGroup.setStatus("obsolete")

usdPPPoEProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 3)
)
usdPPPoEProfileGroup.setObjects(
      *(("Unisphere-Data-PPPOE-MIB", "usdPPPoEProfileRowStatus"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEProfileUrl"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEProfileMotm"))
)
if mibBuilder.loadTexts:
    usdPPPoEProfileGroup.setStatus("deprecated")

usdPPPoEGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 4)
)
usdPPPoEGroup2.setObjects(
      *(("Unisphere-Data-PPPOE-MIB", "usdPPPoENextIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfMaxNumSessions"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfRowStatus"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfLowerIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADI"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADO"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADR"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADS"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADT"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADT"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvVersion"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvCode"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTags"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvSession"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTypes"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvPackets"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInsufficientResources"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADM"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEGlobalMotm"))
)
if mibBuilder.loadTexts:
    usdPPPoEGroup2.setStatus("obsolete")

usdPPPoESubIfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 5)
)
usdPPPoESubIfGroup2.setObjects(
      *(("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfNextIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfRowStatus"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfLowerIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfId"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfSessionId"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfUrl"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESubIfMotm"))
)
if mibBuilder.loadTexts:
    usdPPPoESubIfGroup2.setStatus("current")

usdPPPoESummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 6)
)
usdPPPoESummaryGroup.setObjects(
      *(("Unisphere-Data-PPPOE-MIB", "usdPPPoEMajorInterfaceCount"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryMajorIfAdminUp"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryMajorIfAdminDown"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryMajorIfOperUp"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryMajorIfOperDown"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryMajorIfNotPresent"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummaryMajorIfLowerLayerDown"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubInterfaceCount"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubIfAdminUp"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubIfAdminDown"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubIfOperUp"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubIfOperDown"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubIfNotPresent"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoESummarySubIfLowerLayerDown"))
)
if mibBuilder.loadTexts:
    usdPPPoESummaryGroup.setStatus("current")

usdPPPoEGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 7)
)
usdPPPoEGroup3.setObjects(
      *(("Unisphere-Data-PPPOE-MIB", "usdPPPoENextIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfMaxNumSessions"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfRowStatus"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfLowerIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfAcName"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfDupProtect"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADI"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADO"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADR"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADS"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADT"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADT"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvVersion"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvCode"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTags"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvSession"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTypes"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvPackets"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInsufficientResources"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADM"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEGlobalMotm"))
)
if mibBuilder.loadTexts:
    usdPPPoEGroup3.setStatus("obsolete")

usdPPPoEGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 8)
)
usdPPPoEGroup4.setObjects(
      *(("Unisphere-Data-PPPOE-MIB", "usdPPPoENextIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfMaxNumSessions"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfRowStatus"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfLowerIfIndex"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfAcName"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfDupProtect"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfPADIFlag"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfAutoconfig"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADI"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADO"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADR"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADS"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxPADT"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADT"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvVersion"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvCode"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTags"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvSession"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvTypes"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInvPackets"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsRxInsufficientResources"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEIfStatsTxPADM"),
        ("Unisphere-Data-PPPOE-MIB", "usdPPPoEGlobalMotm"))
)
if mibBuilder.loadTexts:
    usdPPPoEGroup4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdPPPoECompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 1)
)
if mibBuilder.loadTexts:
    usdPPPoECompliance.setStatus(
        "obsolete"
    )

usdPPPoECompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 2)
)
if mibBuilder.loadTexts:
    usdPPPoECompliance2.setStatus(
        "obsolete"
    )

usdPPPoECompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 3)
)
if mibBuilder.loadTexts:
    usdPPPoECompliance3.setStatus(
        "obsolete"
    )

usdPPPoECompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 4)
)
if mibBuilder.loadTexts:
    usdPPPoECompliance4.setStatus(
        "obsolete"
    )

usdPPPoECompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 5)
)
if mibBuilder.loadTexts:
    usdPPPoECompliance5.setStatus(
        "obsolete"
    )

usdPPPoECompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 6)
)
if mibBuilder.loadTexts:
    usdPPPoECompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-PPPOE-MIB",
    **{"usdPPPoEMIB": usdPPPoEMIB,
       "usdPPPoEObjects": usdPPPoEObjects,
       "usdPPPoEIfLayer": usdPPPoEIfLayer,
       "usdPPPoENextIfIndex": usdPPPoENextIfIndex,
       "usdPPPoEIfTable": usdPPPoEIfTable,
       "usdPPPoEIfEntry": usdPPPoEIfEntry,
       "usdPPPoEIfIfIndex": usdPPPoEIfIfIndex,
       "usdPPPoEIfMaxNumSessions": usdPPPoEIfMaxNumSessions,
       "usdPPPoEIfRowStatus": usdPPPoEIfRowStatus,
       "usdPPPoEIfLowerIfIndex": usdPPPoEIfLowerIfIndex,
       "usdPPPoEIfAcName": usdPPPoEIfAcName,
       "usdPPPoEIfDupProtect": usdPPPoEIfDupProtect,
       "usdPPPoEIfPADIFlag": usdPPPoEIfPADIFlag,
       "usdPPPoEIfAutoconfig": usdPPPoEIfAutoconfig,
       "usdPPPoEIfStatsTable": usdPPPoEIfStatsTable,
       "usdPPPoEIfStatsEntry": usdPPPoEIfStatsEntry,
       "usdPPPoEIfStatsRxPADI": usdPPPoEIfStatsRxPADI,
       "usdPPPoEIfStatsTxPADO": usdPPPoEIfStatsTxPADO,
       "usdPPPoEIfStatsRxPADR": usdPPPoEIfStatsRxPADR,
       "usdPPPoEIfStatsTxPADS": usdPPPoEIfStatsTxPADS,
       "usdPPPoEIfStatsRxPADT": usdPPPoEIfStatsRxPADT,
       "usdPPPoEIfStatsTxPADT": usdPPPoEIfStatsTxPADT,
       "usdPPPoEIfStatsRxInvVersion": usdPPPoEIfStatsRxInvVersion,
       "usdPPPoEIfStatsRxInvCode": usdPPPoEIfStatsRxInvCode,
       "usdPPPoEIfStatsRxInvTags": usdPPPoEIfStatsRxInvTags,
       "usdPPPoEIfStatsRxInvSession": usdPPPoEIfStatsRxInvSession,
       "usdPPPoEIfStatsRxInvTypes": usdPPPoEIfStatsRxInvTypes,
       "usdPPPoEIfStatsRxInvPackets": usdPPPoEIfStatsRxInvPackets,
       "usdPPPoEIfStatsRxInsufficientResources": usdPPPoEIfStatsRxInsufficientResources,
       "usdPPPoEIfStatsTxPADM": usdPPPoEIfStatsTxPADM,
       "usdPPPoESubIfLayer": usdPPPoESubIfLayer,
       "usdPPPoESubIfNextIfIndex": usdPPPoESubIfNextIfIndex,
       "usdPPPoESubIfTable": usdPPPoESubIfTable,
       "usdPPPoESubIfEntry": usdPPPoESubIfEntry,
       "usdPPPoESubIfIndex": usdPPPoESubIfIndex,
       "usdPPPoESubIfRowStatus": usdPPPoESubIfRowStatus,
       "usdPPPoESubIfLowerIfIndex": usdPPPoESubIfLowerIfIndex,
       "usdPPPoESubIfId": usdPPPoESubIfId,
       "usdPPPoESubIfSessionId": usdPPPoESubIfSessionId,
       "usdPPPoESubIfMotm": usdPPPoESubIfMotm,
       "usdPPPoESubIfUrl": usdPPPoESubIfUrl,
       "usdPPPoEGlobal": usdPPPoEGlobal,
       "usdPPPoEGlobalMotm": usdPPPoEGlobalMotm,
       "usdPPPoEProfile": usdPPPoEProfile,
       "usdPPPoEProfileTable": usdPPPoEProfileTable,
       "usdPPPoEProfileEntry": usdPPPoEProfileEntry,
       "usdPPPoEProfileIndex": usdPPPoEProfileIndex,
       "usdPPPoEProfileRowStatus": usdPPPoEProfileRowStatus,
       "usdPPPoEProfileMotm": usdPPPoEProfileMotm,
       "usdPPPoEProfileUrl": usdPPPoEProfileUrl,
       "usdPPPoESummary": usdPPPoESummary,
       "usdPPPoEMajorInterfaceCount": usdPPPoEMajorInterfaceCount,
       "usdPPPoESummaryMajorIfAdminUp": usdPPPoESummaryMajorIfAdminUp,
       "usdPPPoESummaryMajorIfAdminDown": usdPPPoESummaryMajorIfAdminDown,
       "usdPPPoESummaryMajorIfOperUp": usdPPPoESummaryMajorIfOperUp,
       "usdPPPoESummaryMajorIfOperDown": usdPPPoESummaryMajorIfOperDown,
       "usdPPPoESummaryMajorIfLowerLayerDown": usdPPPoESummaryMajorIfLowerLayerDown,
       "usdPPPoESummaryMajorIfNotPresent": usdPPPoESummaryMajorIfNotPresent,
       "usdPPPoESummarySubInterfaceCount": usdPPPoESummarySubInterfaceCount,
       "usdPPPoESummarySubIfAdminUp": usdPPPoESummarySubIfAdminUp,
       "usdPPPoESummarySubIfAdminDown": usdPPPoESummarySubIfAdminDown,
       "usdPPPoESummarySubIfOperUp": usdPPPoESummarySubIfOperUp,
       "usdPPPoESummarySubIfOperDown": usdPPPoESummarySubIfOperDown,
       "usdPPPoESummarySubIfLowerLayerDown": usdPPPoESummarySubIfLowerLayerDown,
       "usdPPPoESummarySubIfNotPresent": usdPPPoESummarySubIfNotPresent,
       "usdPPPoEConformance": usdPPPoEConformance,
       "usdPPPoEGroups": usdPPPoEGroups,
       "usdPPPoEGroup": usdPPPoEGroup,
       "usdPPPoESubIfGroup": usdPPPoESubIfGroup,
       "usdPPPoEProfileGroup": usdPPPoEProfileGroup,
       "usdPPPoEGroup2": usdPPPoEGroup2,
       "usdPPPoESubIfGroup2": usdPPPoESubIfGroup2,
       "usdPPPoESummaryGroup": usdPPPoESummaryGroup,
       "usdPPPoEGroup3": usdPPPoEGroup3,
       "usdPPPoEGroup4": usdPPPoEGroup4,
       "usdPPPoECompliances": usdPPPoECompliances,
       "usdPPPoECompliance": usdPPPoECompliance,
       "usdPPPoECompliance2": usdPPPoECompliance2,
       "usdPPPoECompliance3": usdPPPoECompliance3,
       "usdPPPoECompliance4": usdPPPoECompliance4,
       "usdPPPoECompliance5": usdPPPoECompliance5,
       "usdPPPoECompliance6": usdPPPoECompliance6}
)
