# SNMP MIB module (Juniper-PPPOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-PPPOE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:00 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,
 JuniNextIfIndex) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable",
    "JuniNextIfIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniPPPoEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18)
)
juniPPPoEMIB.setRevisions(
        ("2008-11-27 10:23",
         "2008-06-18 09:42",
         "2005-08-03 20:58",
         "2005-05-18 12:01",
         "2004-06-09 20:58",
         "2003-03-10 18:30",
         "2002-10-02 20:12",
         "2002-10-01 18:27",
         "2002-08-16 21:46",
         "2001-06-19 14:27",
         "2001-03-21 15:00",
         "2001-02-12 00:00",
         "2000-10-25 00:00",
         "1999-05-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniPPPoEServiceNameAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("drop", 0),
          ("terminate", 1))
    )



# MIB Managed Objects in the order of their OIDs

_JuniPPPoEObjects_ObjectIdentity = ObjectIdentity
juniPPPoEObjects = _JuniPPPoEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1)
)
_JuniPPPoEIfLayer_ObjectIdentity = ObjectIdentity
juniPPPoEIfLayer = _JuniPPPoEIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1)
)
_JuniPPPoENextIfIndex_Type = JuniNextIfIndex
_JuniPPPoENextIfIndex_Object = MibScalar
juniPPPoENextIfIndex = _JuniPPPoENextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 1),
    _JuniPPPoENextIfIndex_Type()
)
juniPPPoENextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoENextIfIndex.setStatus("current")
_JuniPPPoEIfTable_Object = MibTable
juniPPPoEIfTable = _JuniPPPoEIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniPPPoEIfTable.setStatus("current")
_JuniPPPoEIfEntry_Object = MibTableRow
juniPPPoEIfEntry = _JuniPPPoEIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1)
)
juniPPPoEIfEntry.setIndexNames(
    (0, "Juniper-PPPOE-MIB", "juniPPPoEIfIfIndex"),
)
if mibBuilder.loadTexts:
    juniPPPoEIfEntry.setStatus("current")
_JuniPPPoEIfIfIndex_Type = InterfaceIndex
_JuniPPPoEIfIfIndex_Object = MibTableColumn
juniPPPoEIfIfIndex = _JuniPPPoEIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 1),
    _JuniPPPoEIfIfIndex_Type()
)
juniPPPoEIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfIfIndex.setStatus("current")


class _JuniPPPoEIfMaxNumSessions_Type(Integer32):
    """Custom type juniPPPoEIfMaxNumSessions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65335),
    )


_JuniPPPoEIfMaxNumSessions_Type.__name__ = "Integer32"
_JuniPPPoEIfMaxNumSessions_Object = MibTableColumn
juniPPPoEIfMaxNumSessions = _JuniPPPoEIfMaxNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 2),
    _JuniPPPoEIfMaxNumSessions_Type()
)
juniPPPoEIfMaxNumSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEIfMaxNumSessions.setStatus("current")
_JuniPPPoEIfRowStatus_Type = RowStatus
_JuniPPPoEIfRowStatus_Object = MibTableColumn
juniPPPoEIfRowStatus = _JuniPPPoEIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 3),
    _JuniPPPoEIfRowStatus_Type()
)
juniPPPoEIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEIfRowStatus.setStatus("current")
_JuniPPPoEIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniPPPoEIfLowerIfIndex_Object = MibTableColumn
juniPPPoEIfLowerIfIndex = _JuniPPPoEIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 4),
    _JuniPPPoEIfLowerIfIndex_Type()
)
juniPPPoEIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEIfLowerIfIndex.setStatus("current")


class _JuniPPPoEIfAcName_Type(DisplayString):
    """Custom type juniPPPoEIfAcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniPPPoEIfAcName_Type.__name__ = "DisplayString"
_JuniPPPoEIfAcName_Object = MibTableColumn
juniPPPoEIfAcName = _JuniPPPoEIfAcName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 5),
    _JuniPPPoEIfAcName_Type()
)
juniPPPoEIfAcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEIfAcName.setStatus("current")


class _JuniPPPoEIfDupProtect_Type(JuniEnable):
    """Custom type juniPPPoEIfDupProtect based on JuniEnable"""


_JuniPPPoEIfDupProtect_Object = MibTableColumn
juniPPPoEIfDupProtect = _JuniPPPoEIfDupProtect_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 6),
    _JuniPPPoEIfDupProtect_Type()
)
juniPPPoEIfDupProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEIfDupProtect.setStatus("current")


class _JuniPPPoEIfPADIFlag_Type(JuniEnable):
    """Custom type juniPPPoEIfPADIFlag based on JuniEnable"""


_JuniPPPoEIfPADIFlag_Object = MibTableColumn
juniPPPoEIfPADIFlag = _JuniPPPoEIfPADIFlag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 7),
    _JuniPPPoEIfPADIFlag_Type()
)
juniPPPoEIfPADIFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEIfPADIFlag.setStatus("current")


class _JuniPPPoEIfAutoconfig_Type(JuniEnable):
    """Custom type juniPPPoEIfAutoconfig based on JuniEnable"""


_JuniPPPoEIfAutoconfig_Object = MibTableColumn
juniPPPoEIfAutoconfig = _JuniPPPoEIfAutoconfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 8),
    _JuniPPPoEIfAutoconfig_Type()
)
juniPPPoEIfAutoconfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEIfAutoconfig.setStatus("current")
_JuniPPPoEIfServiceNameTable_Type = Unsigned32
_JuniPPPoEIfServiceNameTable_Object = MibTableColumn
juniPPPoEIfServiceNameTable = _JuniPPPoEIfServiceNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 9),
    _JuniPPPoEIfServiceNameTable_Type()
)
juniPPPoEIfServiceNameTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEIfServiceNameTable.setStatus("current")


class _JuniPPPoEIfPadrRemoteCircuitIdCapture_Type(JuniEnable):
    """Custom type juniPPPoEIfPadrRemoteCircuitIdCapture based on JuniEnable"""


_JuniPPPoEIfPadrRemoteCircuitIdCapture_Object = MibTableColumn
juniPPPoEIfPadrRemoteCircuitIdCapture = _JuniPPPoEIfPadrRemoteCircuitIdCapture_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 10),
    _JuniPPPoEIfPadrRemoteCircuitIdCapture_Type()
)
juniPPPoEIfPadrRemoteCircuitIdCapture.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEIfPadrRemoteCircuitIdCapture.setStatus("current")


class _JuniPPPoEIfMtu_Type(Integer32):
    """Custom type juniPPPoEIfMtu based on Integer32"""
    defaultValue = 1494

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(66, 65535),
    )


_JuniPPPoEIfMtu_Type.__name__ = "Integer32"
_JuniPPPoEIfMtu_Object = MibTableColumn
juniPPPoEIfMtu = _JuniPPPoEIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 11),
    _JuniPPPoEIfMtu_Type()
)
juniPPPoEIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPPPoEIfMtu.setStatus("current")


class _JuniPPPoEIfLockoutMin_Type(Integer32):
    """Custom type juniPPPoEIfLockoutMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniPPPoEIfLockoutMin_Type.__name__ = "Integer32"
_JuniPPPoEIfLockoutMin_Object = MibTableColumn
juniPPPoEIfLockoutMin = _JuniPPPoEIfLockoutMin_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 12),
    _JuniPPPoEIfLockoutMin_Type()
)
juniPPPoEIfLockoutMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPPPoEIfLockoutMin.setStatus("current")


class _JuniPPPoEIfLockoutMax_Type(Integer32):
    """Custom type juniPPPoEIfLockoutMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniPPPoEIfLockoutMax_Type.__name__ = "Integer32"
_JuniPPPoEIfLockoutMax_Object = MibTableColumn
juniPPPoEIfLockoutMax = _JuniPPPoEIfLockoutMax_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 13),
    _JuniPPPoEIfLockoutMax_Type()
)
juniPPPoEIfLockoutMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPPPoEIfLockoutMax.setStatus("current")


class _JuniPPPoEMaxSessionVsa_Type(Integer32):
    """Custom type juniPPPoEMaxSessionVsa based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 2),
          ("override", 1))
    )


_JuniPPPoEMaxSessionVsa_Type.__name__ = "Integer32"
_JuniPPPoEMaxSessionVsa_Object = MibTableColumn
juniPPPoEMaxSessionVsa = _JuniPPPoEMaxSessionVsa_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 2, 1, 14),
    _JuniPPPoEMaxSessionVsa_Type()
)
juniPPPoEMaxSessionVsa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPPPoEMaxSessionVsa.setStatus("current")
_JuniPPPoEIfStatsTable_Object = MibTable
juniPPPoEIfStatsTable = _JuniPPPoEIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniPPPoEIfStatsTable.setStatus("current")
_JuniPPPoEIfStatsEntry_Object = MibTableRow
juniPPPoEIfStatsEntry = _JuniPPPoEIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1)
)
juniPPPoEIfStatsEntry.setIndexNames(
    (0, "Juniper-PPPOE-MIB", "juniPPPoEIfIfIndex"),
)
if mibBuilder.loadTexts:
    juniPPPoEIfStatsEntry.setStatus("current")
_JuniPPPoEIfStatsRxPADI_Type = Counter32
_JuniPPPoEIfStatsRxPADI_Object = MibTableColumn
juniPPPoEIfStatsRxPADI = _JuniPPPoEIfStatsRxPADI_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 1),
    _JuniPPPoEIfStatsRxPADI_Type()
)
juniPPPoEIfStatsRxPADI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxPADI.setStatus("current")
_JuniPPPoEIfStatsTxPADO_Type = Counter32
_JuniPPPoEIfStatsTxPADO_Object = MibTableColumn
juniPPPoEIfStatsTxPADO = _JuniPPPoEIfStatsTxPADO_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 2),
    _JuniPPPoEIfStatsTxPADO_Type()
)
juniPPPoEIfStatsTxPADO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsTxPADO.setStatus("current")
_JuniPPPoEIfStatsRxPADR_Type = Counter32
_JuniPPPoEIfStatsRxPADR_Object = MibTableColumn
juniPPPoEIfStatsRxPADR = _JuniPPPoEIfStatsRxPADR_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 3),
    _JuniPPPoEIfStatsRxPADR_Type()
)
juniPPPoEIfStatsRxPADR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxPADR.setStatus("current")
_JuniPPPoEIfStatsTxPADS_Type = Counter32
_JuniPPPoEIfStatsTxPADS_Object = MibTableColumn
juniPPPoEIfStatsTxPADS = _JuniPPPoEIfStatsTxPADS_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 4),
    _JuniPPPoEIfStatsTxPADS_Type()
)
juniPPPoEIfStatsTxPADS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsTxPADS.setStatus("current")
_JuniPPPoEIfStatsRxPADT_Type = Counter32
_JuniPPPoEIfStatsRxPADT_Object = MibTableColumn
juniPPPoEIfStatsRxPADT = _JuniPPPoEIfStatsRxPADT_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 5),
    _JuniPPPoEIfStatsRxPADT_Type()
)
juniPPPoEIfStatsRxPADT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxPADT.setStatus("current")
_JuniPPPoEIfStatsTxPADT_Type = Counter32
_JuniPPPoEIfStatsTxPADT_Object = MibTableColumn
juniPPPoEIfStatsTxPADT = _JuniPPPoEIfStatsTxPADT_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 6),
    _JuniPPPoEIfStatsTxPADT_Type()
)
juniPPPoEIfStatsTxPADT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsTxPADT.setStatus("current")
_JuniPPPoEIfStatsRxInvVersion_Type = Counter32
_JuniPPPoEIfStatsRxInvVersion_Object = MibTableColumn
juniPPPoEIfStatsRxInvVersion = _JuniPPPoEIfStatsRxInvVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 7),
    _JuniPPPoEIfStatsRxInvVersion_Type()
)
juniPPPoEIfStatsRxInvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxInvVersion.setStatus("current")
_JuniPPPoEIfStatsRxInvCode_Type = Counter32
_JuniPPPoEIfStatsRxInvCode_Object = MibTableColumn
juniPPPoEIfStatsRxInvCode = _JuniPPPoEIfStatsRxInvCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 8),
    _JuniPPPoEIfStatsRxInvCode_Type()
)
juniPPPoEIfStatsRxInvCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxInvCode.setStatus("current")
_JuniPPPoEIfStatsRxInvTags_Type = Counter32
_JuniPPPoEIfStatsRxInvTags_Object = MibTableColumn
juniPPPoEIfStatsRxInvTags = _JuniPPPoEIfStatsRxInvTags_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 9),
    _JuniPPPoEIfStatsRxInvTags_Type()
)
juniPPPoEIfStatsRxInvTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxInvTags.setStatus("current")
_JuniPPPoEIfStatsRxInvSession_Type = Counter32
_JuniPPPoEIfStatsRxInvSession_Object = MibTableColumn
juniPPPoEIfStatsRxInvSession = _JuniPPPoEIfStatsRxInvSession_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 10),
    _JuniPPPoEIfStatsRxInvSession_Type()
)
juniPPPoEIfStatsRxInvSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxInvSession.setStatus("obsolete")
_JuniPPPoEIfStatsRxInvTypes_Type = Counter32
_JuniPPPoEIfStatsRxInvTypes_Object = MibTableColumn
juniPPPoEIfStatsRxInvTypes = _JuniPPPoEIfStatsRxInvTypes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 11),
    _JuniPPPoEIfStatsRxInvTypes_Type()
)
juniPPPoEIfStatsRxInvTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxInvTypes.setStatus("current")
_JuniPPPoEIfStatsRxInvPackets_Type = Counter32
_JuniPPPoEIfStatsRxInvPackets_Object = MibTableColumn
juniPPPoEIfStatsRxInvPackets = _JuniPPPoEIfStatsRxInvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 12),
    _JuniPPPoEIfStatsRxInvPackets_Type()
)
juniPPPoEIfStatsRxInvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxInvPackets.setStatus("current")
_JuniPPPoEIfStatsRxInsufficientResources_Type = Counter32
_JuniPPPoEIfStatsRxInsufficientResources_Object = MibTableColumn
juniPPPoEIfStatsRxInsufficientResources = _JuniPPPoEIfStatsRxInsufficientResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 13),
    _JuniPPPoEIfStatsRxInsufficientResources_Type()
)
juniPPPoEIfStatsRxInsufficientResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxInsufficientResources.setStatus("current")
_JuniPPPoEIfStatsTxPADM_Type = Counter32
_JuniPPPoEIfStatsTxPADM_Object = MibTableColumn
juniPPPoEIfStatsTxPADM = _JuniPPPoEIfStatsTxPADM_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 14),
    _JuniPPPoEIfStatsTxPADM_Type()
)
juniPPPoEIfStatsTxPADM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsTxPADM.setStatus("current")
_JuniPPPoEIfStatsTxPADN_Type = Counter32
_JuniPPPoEIfStatsTxPADN_Object = MibTableColumn
juniPPPoEIfStatsTxPADN = _JuniPPPoEIfStatsTxPADN_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 15),
    _JuniPPPoEIfStatsTxPADN_Type()
)
juniPPPoEIfStatsTxPADN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsTxPADN.setStatus("current")
_JuniPPPoEIfStatsRxInvTagLength_Type = Counter32
_JuniPPPoEIfStatsRxInvTagLength_Object = MibTableColumn
juniPPPoEIfStatsRxInvTagLength = _JuniPPPoEIfStatsRxInvTagLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 16),
    _JuniPPPoEIfStatsRxInvTagLength_Type()
)
juniPPPoEIfStatsRxInvTagLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxInvTagLength.setStatus("current")
_JuniPPPoEIfStatsRxInvLength_Type = Counter32
_JuniPPPoEIfStatsRxInvLength_Object = MibTableColumn
juniPPPoEIfStatsRxInvLength = _JuniPPPoEIfStatsRxInvLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 17),
    _JuniPPPoEIfStatsRxInvLength_Type()
)
juniPPPoEIfStatsRxInvLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxInvLength.setStatus("current")
_JuniPPPoEIfStatsRxInvPadISession_Type = Counter32
_JuniPPPoEIfStatsRxInvPadISession_Object = MibTableColumn
juniPPPoEIfStatsRxInvPadISession = _JuniPPPoEIfStatsRxInvPadISession_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 18),
    _JuniPPPoEIfStatsRxInvPadISession_Type()
)
juniPPPoEIfStatsRxInvPadISession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxInvPadISession.setStatus("current")
_JuniPPPoEIfStatsRxInvPadRSession_Type = Counter32
_JuniPPPoEIfStatsRxInvPadRSession_Object = MibTableColumn
juniPPPoEIfStatsRxInvPadRSession = _JuniPPPoEIfStatsRxInvPadRSession_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 3, 1, 19),
    _JuniPPPoEIfStatsRxInvPadRSession_Type()
)
juniPPPoEIfStatsRxInvPadRSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfStatsRxInvPadRSession.setStatus("current")
_JuniPPPoEIfLockoutTable_Object = MibTable
juniPPPoEIfLockoutTable = _JuniPPPoEIfLockoutTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniPPPoEIfLockoutTable.setStatus("current")
_JuniPPPoEIfLockoutEntry_Object = MibTableRow
juniPPPoEIfLockoutEntry = _JuniPPPoEIfLockoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 4, 1)
)
juniPPPoEIfLockoutEntry.setIndexNames(
    (0, "Juniper-PPPOE-MIB", "juniPPPoEIfIfIndex"),
    (0, "Juniper-PPPOE-MIB", "juniPPPoEIfLockoutClientAddress"),
)
if mibBuilder.loadTexts:
    juniPPPoEIfLockoutEntry.setStatus("current")
_JuniPPPoEIfLockoutClientAddress_Type = MacAddress
_JuniPPPoEIfLockoutClientAddress_Object = MibTableColumn
juniPPPoEIfLockoutClientAddress = _JuniPPPoEIfLockoutClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 4, 1, 1),
    _JuniPPPoEIfLockoutClientAddress_Type()
)
juniPPPoEIfLockoutClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPPPoEIfLockoutClientAddress.setStatus("current")


class _JuniPPPoEIfLockoutTime_Type(Integer32):
    """Custom type juniPPPoEIfLockoutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniPPPoEIfLockoutTime_Type.__name__ = "Integer32"
_JuniPPPoEIfLockoutTime_Object = MibTableColumn
juniPPPoEIfLockoutTime = _JuniPPPoEIfLockoutTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 4, 1, 2),
    _JuniPPPoEIfLockoutTime_Type()
)
juniPPPoEIfLockoutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfLockoutTime.setStatus("current")


class _JuniPPPoEIfLockoutElapsedTime_Type(Integer32):
    """Custom type juniPPPoEIfLockoutElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniPPPoEIfLockoutElapsedTime_Type.__name__ = "Integer32"
_JuniPPPoEIfLockoutElapsedTime_Object = MibTableColumn
juniPPPoEIfLockoutElapsedTime = _JuniPPPoEIfLockoutElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 4, 1, 3),
    _JuniPPPoEIfLockoutElapsedTime_Type()
)
juniPPPoEIfLockoutElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfLockoutElapsedTime.setStatus("current")


class _JuniPPPoEIfLockoutNextTime_Type(Integer32):
    """Custom type juniPPPoEIfLockoutNextTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniPPPoEIfLockoutNextTime_Type.__name__ = "Integer32"
_JuniPPPoEIfLockoutNextTime_Object = MibTableColumn
juniPPPoEIfLockoutNextTime = _JuniPPPoEIfLockoutNextTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 1, 4, 1, 4),
    _JuniPPPoEIfLockoutNextTime_Type()
)
juniPPPoEIfLockoutNextTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEIfLockoutNextTime.setStatus("current")
_JuniPPPoESubIfLayer_ObjectIdentity = ObjectIdentity
juniPPPoESubIfLayer = _JuniPPPoESubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2)
)
_JuniPPPoESubIfNextIfIndex_Type = JuniNextIfIndex
_JuniPPPoESubIfNextIfIndex_Object = MibScalar
juniPPPoESubIfNextIfIndex = _JuniPPPoESubIfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 1),
    _JuniPPPoESubIfNextIfIndex_Type()
)
juniPPPoESubIfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESubIfNextIfIndex.setStatus("current")
_JuniPPPoESubIfTable_Object = MibTable
juniPPPoESubIfTable = _JuniPPPoESubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniPPPoESubIfTable.setStatus("current")
_JuniPPPoESubIfEntry_Object = MibTableRow
juniPPPoESubIfEntry = _JuniPPPoESubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1)
)
juniPPPoESubIfEntry.setIndexNames(
    (0, "Juniper-PPPOE-MIB", "juniPPPoESubIfIndex"),
)
if mibBuilder.loadTexts:
    juniPPPoESubIfEntry.setStatus("current")
_JuniPPPoESubIfIndex_Type = InterfaceIndex
_JuniPPPoESubIfIndex_Object = MibTableColumn
juniPPPoESubIfIndex = _JuniPPPoESubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 1),
    _JuniPPPoESubIfIndex_Type()
)
juniPPPoESubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPPPoESubIfIndex.setStatus("current")
_JuniPPPoESubIfRowStatus_Type = RowStatus
_JuniPPPoESubIfRowStatus_Object = MibTableColumn
juniPPPoESubIfRowStatus = _JuniPPPoESubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 2),
    _JuniPPPoESubIfRowStatus_Type()
)
juniPPPoESubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoESubIfRowStatus.setStatus("current")
_JuniPPPoESubIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniPPPoESubIfLowerIfIndex_Object = MibTableColumn
juniPPPoESubIfLowerIfIndex = _JuniPPPoESubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 3),
    _JuniPPPoESubIfLowerIfIndex_Type()
)
juniPPPoESubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoESubIfLowerIfIndex.setStatus("current")


class _JuniPPPoESubIfId_Type(Integer32):
    """Custom type juniPPPoESubIfId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_JuniPPPoESubIfId_Type.__name__ = "Integer32"
_JuniPPPoESubIfId_Object = MibTableColumn
juniPPPoESubIfId = _JuniPPPoESubIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 4),
    _JuniPPPoESubIfId_Type()
)
juniPPPoESubIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoESubIfId.setStatus("current")


class _JuniPPPoESubIfSessionId_Type(Integer32):
    """Custom type juniPPPoESubIfSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniPPPoESubIfSessionId_Type.__name__ = "Integer32"
_JuniPPPoESubIfSessionId_Object = MibTableColumn
juniPPPoESubIfSessionId = _JuniPPPoESubIfSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 5),
    _JuniPPPoESubIfSessionId_Type()
)
juniPPPoESubIfSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESubIfSessionId.setStatus("current")


class _JuniPPPoESubIfMotm_Type(DisplayString):
    """Custom type juniPPPoESubIfMotm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JuniPPPoESubIfMotm_Type.__name__ = "DisplayString"
_JuniPPPoESubIfMotm_Object = MibTableColumn
juniPPPoESubIfMotm = _JuniPPPoESubIfMotm_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 6),
    _JuniPPPoESubIfMotm_Type()
)
juniPPPoESubIfMotm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoESubIfMotm.setStatus("current")


class _JuniPPPoESubIfUrl_Type(DisplayString):
    """Custom type juniPPPoESubIfUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JuniPPPoESubIfUrl_Type.__name__ = "DisplayString"
_JuniPPPoESubIfUrl_Object = MibTableColumn
juniPPPoESubIfUrl = _JuniPPPoESubIfUrl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 2, 2, 1, 7),
    _JuniPPPoESubIfUrl_Type()
)
juniPPPoESubIfUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoESubIfUrl.setStatus("current")
_JuniPPPoEGlobal_ObjectIdentity = ObjectIdentity
juniPPPoEGlobal = _JuniPPPoEGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 3)
)


class _JuniPPPoEGlobalMotm_Type(DisplayString):
    """Custom type juniPPPoEGlobalMotm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JuniPPPoEGlobalMotm_Type.__name__ = "DisplayString"
_JuniPPPoEGlobalMotm_Object = MibScalar
juniPPPoEGlobalMotm = _JuniPPPoEGlobalMotm_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 3, 1),
    _JuniPPPoEGlobalMotm_Type()
)
juniPPPoEGlobalMotm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPPPoEGlobalMotm.setStatus("current")
_JuniPPPoEProfile_ObjectIdentity = ObjectIdentity
juniPPPoEProfile = _JuniPPPoEProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4)
)
_JuniPPPoEProfileTable_Object = MibTable
juniPPPoEProfileTable = _JuniPPPoEProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1)
)
if mibBuilder.loadTexts:
    juniPPPoEProfileTable.setStatus("deprecated")
_JuniPPPoEProfileEntry_Object = MibTableRow
juniPPPoEProfileEntry = _JuniPPPoEProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1)
)
juniPPPoEProfileEntry.setIndexNames(
    (0, "Juniper-PPPOE-MIB", "juniPPPoEProfileIndex"),
)
if mibBuilder.loadTexts:
    juniPPPoEProfileEntry.setStatus("deprecated")
_JuniPPPoEProfileIndex_Type = Unsigned32
_JuniPPPoEProfileIndex_Object = MibTableColumn
juniPPPoEProfileIndex = _JuniPPPoEProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1, 1),
    _JuniPPPoEProfileIndex_Type()
)
juniPPPoEProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPPPoEProfileIndex.setStatus("deprecated")
_JuniPPPoEProfileRowStatus_Type = RowStatus
_JuniPPPoEProfileRowStatus_Object = MibTableColumn
juniPPPoEProfileRowStatus = _JuniPPPoEProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1, 2),
    _JuniPPPoEProfileRowStatus_Type()
)
juniPPPoEProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEProfileRowStatus.setStatus("deprecated")


class _JuniPPPoEProfileMotm_Type(DisplayString):
    """Custom type juniPPPoEProfileMotm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JuniPPPoEProfileMotm_Type.__name__ = "DisplayString"
_JuniPPPoEProfileMotm_Object = MibTableColumn
juniPPPoEProfileMotm = _JuniPPPoEProfileMotm_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1, 3),
    _JuniPPPoEProfileMotm_Type()
)
juniPPPoEProfileMotm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEProfileMotm.setStatus("deprecated")


class _JuniPPPoEProfileUrl_Type(DisplayString):
    """Custom type juniPPPoEProfileUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JuniPPPoEProfileUrl_Type.__name__ = "DisplayString"
_JuniPPPoEProfileUrl_Object = MibTableColumn
juniPPPoEProfileUrl = _JuniPPPoEProfileUrl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 4, 1, 1, 4),
    _JuniPPPoEProfileUrl_Type()
)
juniPPPoEProfileUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEProfileUrl.setStatus("deprecated")
_JuniPPPoESummary_ObjectIdentity = ObjectIdentity
juniPPPoESummary = _JuniPPPoESummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5)
)
_JuniPPPoEMajorInterfaceCount_Type = Integer32
_JuniPPPoEMajorInterfaceCount_Object = MibScalar
juniPPPoEMajorInterfaceCount = _JuniPPPoEMajorInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 1),
    _JuniPPPoEMajorInterfaceCount_Type()
)
juniPPPoEMajorInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEMajorInterfaceCount.setStatus("current")
_JuniPPPoESummaryMajorIfAdminUp_Type = Integer32
_JuniPPPoESummaryMajorIfAdminUp_Object = MibScalar
juniPPPoESummaryMajorIfAdminUp = _JuniPPPoESummaryMajorIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 2),
    _JuniPPPoESummaryMajorIfAdminUp_Type()
)
juniPPPoESummaryMajorIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESummaryMajorIfAdminUp.setStatus("current")
_JuniPPPoESummaryMajorIfAdminDown_Type = Integer32
_JuniPPPoESummaryMajorIfAdminDown_Object = MibScalar
juniPPPoESummaryMajorIfAdminDown = _JuniPPPoESummaryMajorIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 3),
    _JuniPPPoESummaryMajorIfAdminDown_Type()
)
juniPPPoESummaryMajorIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESummaryMajorIfAdminDown.setStatus("current")
_JuniPPPoESummaryMajorIfOperUp_Type = Integer32
_JuniPPPoESummaryMajorIfOperUp_Object = MibScalar
juniPPPoESummaryMajorIfOperUp = _JuniPPPoESummaryMajorIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 4),
    _JuniPPPoESummaryMajorIfOperUp_Type()
)
juniPPPoESummaryMajorIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESummaryMajorIfOperUp.setStatus("current")
_JuniPPPoESummaryMajorIfOperDown_Type = Integer32
_JuniPPPoESummaryMajorIfOperDown_Object = MibScalar
juniPPPoESummaryMajorIfOperDown = _JuniPPPoESummaryMajorIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 5),
    _JuniPPPoESummaryMajorIfOperDown_Type()
)
juniPPPoESummaryMajorIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESummaryMajorIfOperDown.setStatus("current")
_JuniPPPoESummaryMajorIfLowerLayerDown_Type = Integer32
_JuniPPPoESummaryMajorIfLowerLayerDown_Object = MibScalar
juniPPPoESummaryMajorIfLowerLayerDown = _JuniPPPoESummaryMajorIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 6),
    _JuniPPPoESummaryMajorIfLowerLayerDown_Type()
)
juniPPPoESummaryMajorIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESummaryMajorIfLowerLayerDown.setStatus("current")
_JuniPPPoESummaryMajorIfNotPresent_Type = Integer32
_JuniPPPoESummaryMajorIfNotPresent_Object = MibScalar
juniPPPoESummaryMajorIfNotPresent = _JuniPPPoESummaryMajorIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 7),
    _JuniPPPoESummaryMajorIfNotPresent_Type()
)
juniPPPoESummaryMajorIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESummaryMajorIfNotPresent.setStatus("current")
_JuniPPPoESummarySubInterfaceCount_Type = Integer32
_JuniPPPoESummarySubInterfaceCount_Object = MibScalar
juniPPPoESummarySubInterfaceCount = _JuniPPPoESummarySubInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 8),
    _JuniPPPoESummarySubInterfaceCount_Type()
)
juniPPPoESummarySubInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESummarySubInterfaceCount.setStatus("current")
_JuniPPPoESummarySubIfAdminUp_Type = Integer32
_JuniPPPoESummarySubIfAdminUp_Object = MibScalar
juniPPPoESummarySubIfAdminUp = _JuniPPPoESummarySubIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 9),
    _JuniPPPoESummarySubIfAdminUp_Type()
)
juniPPPoESummarySubIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESummarySubIfAdminUp.setStatus("current")
_JuniPPPoESummarySubIfAdminDown_Type = Integer32
_JuniPPPoESummarySubIfAdminDown_Object = MibScalar
juniPPPoESummarySubIfAdminDown = _JuniPPPoESummarySubIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 10),
    _JuniPPPoESummarySubIfAdminDown_Type()
)
juniPPPoESummarySubIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESummarySubIfAdminDown.setStatus("current")
_JuniPPPoESummarySubIfOperUp_Type = Integer32
_JuniPPPoESummarySubIfOperUp_Object = MibScalar
juniPPPoESummarySubIfOperUp = _JuniPPPoESummarySubIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 11),
    _JuniPPPoESummarySubIfOperUp_Type()
)
juniPPPoESummarySubIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESummarySubIfOperUp.setStatus("current")
_JuniPPPoESummarySubIfOperDown_Type = Integer32
_JuniPPPoESummarySubIfOperDown_Object = MibScalar
juniPPPoESummarySubIfOperDown = _JuniPPPoESummarySubIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 12),
    _JuniPPPoESummarySubIfOperDown_Type()
)
juniPPPoESummarySubIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESummarySubIfOperDown.setStatus("current")
_JuniPPPoESummarySubIfLowerLayerDown_Type = Integer32
_JuniPPPoESummarySubIfLowerLayerDown_Object = MibScalar
juniPPPoESummarySubIfLowerLayerDown = _JuniPPPoESummarySubIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 13),
    _JuniPPPoESummarySubIfLowerLayerDown_Type()
)
juniPPPoESummarySubIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESummarySubIfLowerLayerDown.setStatus("current")
_JuniPPPoESummarySubIfNotPresent_Type = Integer32
_JuniPPPoESummarySubIfNotPresent_Object = MibScalar
juniPPPoESummarySubIfNotPresent = _JuniPPPoESummarySubIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 5, 14),
    _JuniPPPoESummarySubIfNotPresent_Type()
)
juniPPPoESummarySubIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoESummarySubIfNotPresent.setStatus("current")
_JuniPPPoEServices_ObjectIdentity = ObjectIdentity
juniPPPoEServices = _JuniPPPoEServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6)
)
_JuniPPPoEServiceNameTableNextIndex_Type = Unsigned32
_JuniPPPoEServiceNameTableNextIndex_Object = MibScalar
juniPPPoEServiceNameTableNextIndex = _JuniPPPoEServiceNameTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6, 1),
    _JuniPPPoEServiceNameTableNextIndex_Type()
)
juniPPPoEServiceNameTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPPPoEServiceNameTableNextIndex.setStatus("current")
_JuniPPPoEServiceNameTableTable_Object = MibTable
juniPPPoEServiceNameTableTable = _JuniPPPoEServiceNameTableTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6, 2)
)
if mibBuilder.loadTexts:
    juniPPPoEServiceNameTableTable.setStatus("current")
_JuniPPPoEServiceNameTableEntry_Object = MibTableRow
juniPPPoEServiceNameTableEntry = _JuniPPPoEServiceNameTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6, 2, 1)
)
juniPPPoEServiceNameTableEntry.setIndexNames(
    (0, "Juniper-PPPOE-MIB", "juniPPPoEServiceNameTableIndex"),
)
if mibBuilder.loadTexts:
    juniPPPoEServiceNameTableEntry.setStatus("current")
_JuniPPPoEServiceNameTableIndex_Type = Unsigned32
_JuniPPPoEServiceNameTableIndex_Object = MibTableColumn
juniPPPoEServiceNameTableIndex = _JuniPPPoEServiceNameTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6, 2, 1, 1),
    _JuniPPPoEServiceNameTableIndex_Type()
)
juniPPPoEServiceNameTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPPPoEServiceNameTableIndex.setStatus("current")


class _JuniPPPoEServiceNameTableName_Type(DisplayString):
    """Custom type juniPPPoEServiceNameTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JuniPPPoEServiceNameTableName_Type.__name__ = "DisplayString"
_JuniPPPoEServiceNameTableName_Object = MibTableColumn
juniPPPoEServiceNameTableName = _JuniPPPoEServiceNameTableName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6, 2, 1, 2),
    _JuniPPPoEServiceNameTableName_Type()
)
juniPPPoEServiceNameTableName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEServiceNameTableName.setStatus("current")
_JuniPPPoEServiceNameTableEmptyAction_Type = JuniPPPoEServiceNameAction
_JuniPPPoEServiceNameTableEmptyAction_Object = MibTableColumn
juniPPPoEServiceNameTableEmptyAction = _JuniPPPoEServiceNameTableEmptyAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6, 2, 1, 3),
    _JuniPPPoEServiceNameTableEmptyAction_Type()
)
juniPPPoEServiceNameTableEmptyAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEServiceNameTableEmptyAction.setStatus("current")
_JuniPPPoEServiceNameTableRowStatus_Type = RowStatus
_JuniPPPoEServiceNameTableRowStatus_Object = MibTableColumn
juniPPPoEServiceNameTableRowStatus = _JuniPPPoEServiceNameTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6, 2, 1, 4),
    _JuniPPPoEServiceNameTableRowStatus_Type()
)
juniPPPoEServiceNameTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEServiceNameTableRowStatus.setStatus("current")
_JuniPPPoEServiceNameTableUnknownAction_Type = JuniPPPoEServiceNameAction
_JuniPPPoEServiceNameTableUnknownAction_Object = MibTableColumn
juniPPPoEServiceNameTableUnknownAction = _JuniPPPoEServiceNameTableUnknownAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6, 2, 1, 5),
    _JuniPPPoEServiceNameTableUnknownAction_Type()
)
juniPPPoEServiceNameTableUnknownAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEServiceNameTableUnknownAction.setStatus("current")
_JuniPPPoEServiceNameTable_Object = MibTable
juniPPPoEServiceNameTable = _JuniPPPoEServiceNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6, 3)
)
if mibBuilder.loadTexts:
    juniPPPoEServiceNameTable.setStatus("current")
_JuniPPPoEServiceNameEntry_Object = MibTableRow
juniPPPoEServiceNameEntry = _JuniPPPoEServiceNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6, 3, 1)
)
juniPPPoEServiceNameEntry.setIndexNames(
    (0, "Juniper-PPPOE-MIB", "juniPPPoEServiceNameTableIndex"),
    (0, "Juniper-PPPOE-MIB", "juniPPPoEServiceName"),
)
if mibBuilder.loadTexts:
    juniPPPoEServiceNameEntry.setStatus("current")


class _JuniPPPoEServiceName_Type(DisplayString):
    """Custom type juniPPPoEServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JuniPPPoEServiceName_Type.__name__ = "DisplayString"
_JuniPPPoEServiceName_Object = MibTableColumn
juniPPPoEServiceName = _JuniPPPoEServiceName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6, 3, 1, 1),
    _JuniPPPoEServiceName_Type()
)
juniPPPoEServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPPPoEServiceName.setStatus("current")
_JuniPPPoEServiceNameAction_Type = JuniPPPoEServiceNameAction
_JuniPPPoEServiceNameAction_Object = MibTableColumn
juniPPPoEServiceNameAction = _JuniPPPoEServiceNameAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6, 3, 1, 2),
    _JuniPPPoEServiceNameAction_Type()
)
juniPPPoEServiceNameAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEServiceNameAction.setStatus("current")
_JuniPPPoEServiceNameRowStatus_Type = RowStatus
_JuniPPPoEServiceNameRowStatus_Object = MibTableColumn
juniPPPoEServiceNameRowStatus = _JuniPPPoEServiceNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 1, 6, 3, 1, 3),
    _JuniPPPoEServiceNameRowStatus_Type()
)
juniPPPoEServiceNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPPPoEServiceNameRowStatus.setStatus("current")
_JuniPPPoEConformance_ObjectIdentity = ObjectIdentity
juniPPPoEConformance = _JuniPPPoEConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4)
)
_JuniPPPoEGroups_ObjectIdentity = ObjectIdentity
juniPPPoEGroups = _JuniPPPoEGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4)
)
_JuniPPPoECompliances_ObjectIdentity = ObjectIdentity
juniPPPoECompliances = _JuniPPPoECompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5)
)

# Managed Objects groups

juniPPPoEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 1)
)
juniPPPoEGroup.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoENextIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfMaxNumSessions"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLowerIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADI"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADO"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADR"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADS"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvVersion"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvCode"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTags"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvSession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTypes"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPackets"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInsufficientResources"))
)
if mibBuilder.loadTexts:
    juniPPPoEGroup.setStatus("obsolete")

juniPPPoESubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 2)
)
juniPPPoESubIfGroup.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoESubIfNextIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoESubIfRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoESubIfLowerIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoESubIfId"),
        ("Juniper-PPPOE-MIB", "juniPPPoESubIfSessionId"))
)
if mibBuilder.loadTexts:
    juniPPPoESubIfGroup.setStatus("obsolete")

juniPPPoEProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 3)
)
juniPPPoEProfileGroup.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoEProfileRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEProfileUrl"),
        ("Juniper-PPPOE-MIB", "juniPPPoEProfileMotm"))
)
if mibBuilder.loadTexts:
    juniPPPoEProfileGroup.setStatus("deprecated")

juniPPPoEGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 4)
)
juniPPPoEGroup2.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoENextIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfMaxNumSessions"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLowerIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADI"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADO"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADR"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADS"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvVersion"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvCode"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTags"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvSession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTypes"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPackets"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInsufficientResources"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADM"),
        ("Juniper-PPPOE-MIB", "juniPPPoEGlobalMotm"))
)
if mibBuilder.loadTexts:
    juniPPPoEGroup2.setStatus("obsolete")

juniPPPoESubIfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 5)
)
juniPPPoESubIfGroup2.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoESubIfNextIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoESubIfRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoESubIfLowerIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoESubIfId"),
        ("Juniper-PPPOE-MIB", "juniPPPoESubIfSessionId"),
        ("Juniper-PPPOE-MIB", "juniPPPoESubIfUrl"),
        ("Juniper-PPPOE-MIB", "juniPPPoESubIfMotm"))
)
if mibBuilder.loadTexts:
    juniPPPoESubIfGroup2.setStatus("current")

juniPPPoESummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 6)
)
juniPPPoESummaryGroup.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoEMajorInterfaceCount"),
        ("Juniper-PPPOE-MIB", "juniPPPoESummaryMajorIfAdminUp"),
        ("Juniper-PPPOE-MIB", "juniPPPoESummaryMajorIfAdminDown"),
        ("Juniper-PPPOE-MIB", "juniPPPoESummaryMajorIfOperUp"),
        ("Juniper-PPPOE-MIB", "juniPPPoESummaryMajorIfOperDown"),
        ("Juniper-PPPOE-MIB", "juniPPPoESummaryMajorIfNotPresent"),
        ("Juniper-PPPOE-MIB", "juniPPPoESummaryMajorIfLowerLayerDown"),
        ("Juniper-PPPOE-MIB", "juniPPPoESummarySubInterfaceCount"),
        ("Juniper-PPPOE-MIB", "juniPPPoESummarySubIfAdminUp"),
        ("Juniper-PPPOE-MIB", "juniPPPoESummarySubIfAdminDown"),
        ("Juniper-PPPOE-MIB", "juniPPPoESummarySubIfOperUp"),
        ("Juniper-PPPOE-MIB", "juniPPPoESummarySubIfOperDown"),
        ("Juniper-PPPOE-MIB", "juniPPPoESummarySubIfNotPresent"),
        ("Juniper-PPPOE-MIB", "juniPPPoESummarySubIfLowerLayerDown"))
)
if mibBuilder.loadTexts:
    juniPPPoESummaryGroup.setStatus("current")

juniPPPoEGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 7)
)
juniPPPoEGroup3.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoENextIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfMaxNumSessions"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLowerIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAcName"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfDupProtect"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADI"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADO"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADR"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADS"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvVersion"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvCode"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTags"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvSession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTypes"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPackets"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInsufficientResources"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADM"),
        ("Juniper-PPPOE-MIB", "juniPPPoEGlobalMotm"))
)
if mibBuilder.loadTexts:
    juniPPPoEGroup3.setStatus("obsolete")

juniPPPoEGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 8)
)
juniPPPoEGroup4.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoENextIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfMaxNumSessions"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLowerIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAcName"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfDupProtect"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfPADIFlag"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAutoconfig"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADI"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADO"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADR"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADS"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvVersion"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvCode"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTags"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvSession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTypes"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPackets"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInsufficientResources"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADM"),
        ("Juniper-PPPOE-MIB", "juniPPPoEGlobalMotm"))
)
if mibBuilder.loadTexts:
    juniPPPoEGroup4.setStatus("obsolete")

juniPPPoEGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 9)
)
juniPPPoEGroup5.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoENextIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfMaxNumSessions"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLowerIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAcName"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfDupProtect"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfPADIFlag"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAutoconfig"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADI"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADO"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADR"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADS"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvVersion"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvCode"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTags"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvSession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTypes"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPackets"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInsufficientResources"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADM"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADN"),
        ("Juniper-PPPOE-MIB", "juniPPPoEGlobalMotm"))
)
if mibBuilder.loadTexts:
    juniPPPoEGroup5.setStatus("obsolete")

juniPPPoEGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 10)
)
juniPPPoEGroup6.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoENextIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfMaxNumSessions"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLowerIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAcName"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfDupProtect"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfPADIFlag"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAutoconfig"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfServiceNameTable"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADI"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADO"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADR"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADS"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvVersion"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvCode"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTags"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTagLength"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvLength"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTypes"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPackets"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInsufficientResources"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADM"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADN"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPadISession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPadRSession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEGlobalMotm"))
)
if mibBuilder.loadTexts:
    juniPPPoEGroup6.setStatus("obsolete")

juniPPPoEServiceNameTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 11)
)
juniPPPoEServiceNameTableGroup.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoEServiceNameTableNextIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEServiceNameTableName"),
        ("Juniper-PPPOE-MIB", "juniPPPoEServiceNameTableEmptyAction"),
        ("Juniper-PPPOE-MIB", "juniPPPoEServiceNameTableRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEServiceNameAction"),
        ("Juniper-PPPOE-MIB", "juniPPPoEServiceNameRowStatus"))
)
if mibBuilder.loadTexts:
    juniPPPoEServiceNameTableGroup.setStatus("obsolete")

juniPPPoEGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 12)
)
juniPPPoEGroup7.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoENextIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfMaxNumSessions"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLowerIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAcName"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfDupProtect"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfPADIFlag"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAutoconfig"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfServiceNameTable"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfPadrRemoteCircuitIdCapture"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADI"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADO"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADR"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADS"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvVersion"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvCode"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTags"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTagLength"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvLength"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTypes"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPackets"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInsufficientResources"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADM"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADN"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPadISession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPadRSession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEGlobalMotm"))
)
if mibBuilder.loadTexts:
    juniPPPoEGroup7.setStatus("obsolete")

juniPPPoEGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 13)
)
juniPPPoEGroup8.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoENextIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfMaxNumSessions"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLowerIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAcName"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfDupProtect"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfPADIFlag"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAutoconfig"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfServiceNameTable"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfPadrRemoteCircuitIdCapture"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfMtu"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADI"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADO"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADR"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADS"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvVersion"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvCode"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTags"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTagLength"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvLength"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTypes"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPackets"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInsufficientResources"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADM"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADN"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPadISession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPadRSession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEGlobalMotm"))
)
if mibBuilder.loadTexts:
    juniPPPoEGroup8.setStatus("current")

juniPPPoELockoutTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 14)
)
juniPPPoELockoutTableGroup.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoEIfLockoutTime"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLockoutElapsedTime"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLockoutNextTime"))
)
if mibBuilder.loadTexts:
    juniPPPoELockoutTableGroup.setStatus("current")

juniPPPoEGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 15)
)
juniPPPoEGroup9.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoENextIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfMaxNumSessions"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLowerIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAcName"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfDupProtect"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfPADIFlag"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAutoconfig"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfServiceNameTable"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfPadrRemoteCircuitIdCapture"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfMtu"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLockoutMin"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLockoutMax"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADI"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADO"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADR"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADS"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvVersion"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvCode"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTags"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTagLength"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvLength"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTypes"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPackets"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInsufficientResources"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADM"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADN"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPadISession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPadRSession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEGlobalMotm"))
)
if mibBuilder.loadTexts:
    juniPPPoEGroup9.setStatus("obsolete")

juniPPPoEGroup10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 16)
)
juniPPPoEGroup10.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoENextIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfMaxNumSessions"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLowerIfIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAcName"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfDupProtect"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfPADIFlag"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfAutoconfig"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfServiceNameTable"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfPadrRemoteCircuitIdCapture"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfMtu"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLockoutMin"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfLockoutMax"),
        ("Juniper-PPPOE-MIB", "juniPPPoEMaxSessionVsa"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADI"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADO"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADR"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADS"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADT"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvVersion"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvCode"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTags"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTagLength"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvLength"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvTypes"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPackets"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInsufficientResources"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADM"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsTxPADN"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPadISession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEIfStatsRxInvPadRSession"),
        ("Juniper-PPPOE-MIB", "juniPPPoEGlobalMotm"))
)
if mibBuilder.loadTexts:
    juniPPPoEGroup10.setStatus("current")

juniPPPoEServiceNameTableGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 4, 17)
)
juniPPPoEServiceNameTableGroup1.setObjects(
      *(("Juniper-PPPOE-MIB", "juniPPPoEServiceNameTableNextIndex"),
        ("Juniper-PPPOE-MIB", "juniPPPoEServiceNameTableName"),
        ("Juniper-PPPOE-MIB", "juniPPPoEServiceNameTableEmptyAction"),
        ("Juniper-PPPOE-MIB", "juniPPPoEServiceNameTableRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEServiceNameAction"),
        ("Juniper-PPPOE-MIB", "juniPPPoEServiceNameRowStatus"),
        ("Juniper-PPPOE-MIB", "juniPPPoEServiceNameTableUnknownAction"))
)
if mibBuilder.loadTexts:
    juniPPPoEServiceNameTableGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniPPPoECompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 1)
)
if mibBuilder.loadTexts:
    juniPPPoECompliance.setStatus(
        "obsolete"
    )

juniPPPoECompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 2)
)
if mibBuilder.loadTexts:
    juniPPPoECompliance2.setStatus(
        "obsolete"
    )

juniPPPoECompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 3)
)
if mibBuilder.loadTexts:
    juniPPPoECompliance3.setStatus(
        "obsolete"
    )

juniPPPoECompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 4)
)
if mibBuilder.loadTexts:
    juniPPPoECompliance4.setStatus(
        "obsolete"
    )

juniPPPoECompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 5)
)
if mibBuilder.loadTexts:
    juniPPPoECompliance5.setStatus(
        "obsolete"
    )

juniPPPoECompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 6)
)
if mibBuilder.loadTexts:
    juniPPPoECompliance6.setStatus(
        "obsolete"
    )

juniPPPoECompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 7)
)
if mibBuilder.loadTexts:
    juniPPPoECompliance7.setStatus(
        "obsolete"
    )

juniPPPoECompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 8)
)
if mibBuilder.loadTexts:
    juniPPPoECompliance8.setStatus(
        "obsolete"
    )

juniPPPoECompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 9)
)
if mibBuilder.loadTexts:
    juniPPPoECompliance9.setStatus(
        "obsolete"
    )

juniPPPoECompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 10)
)
if mibBuilder.loadTexts:
    juniPPPoECompliance10.setStatus(
        "obsolete"
    )

juniPPPoECompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 11)
)
if mibBuilder.loadTexts:
    juniPPPoECompliance11.setStatus(
        "obsolete"
    )

juniPPPoECompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 12)
)
if mibBuilder.loadTexts:
    juniPPPoECompliance12.setStatus(
        "obsolete"
    )

juniPPPoECompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 18, 4, 5, 13)
)
if mibBuilder.loadTexts:
    juniPPPoECompliance13.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-PPPOE-MIB",
    **{"JuniPPPoEServiceNameAction": JuniPPPoEServiceNameAction,
       "juniPPPoEMIB": juniPPPoEMIB,
       "juniPPPoEObjects": juniPPPoEObjects,
       "juniPPPoEIfLayer": juniPPPoEIfLayer,
       "juniPPPoENextIfIndex": juniPPPoENextIfIndex,
       "juniPPPoEIfTable": juniPPPoEIfTable,
       "juniPPPoEIfEntry": juniPPPoEIfEntry,
       "juniPPPoEIfIfIndex": juniPPPoEIfIfIndex,
       "juniPPPoEIfMaxNumSessions": juniPPPoEIfMaxNumSessions,
       "juniPPPoEIfRowStatus": juniPPPoEIfRowStatus,
       "juniPPPoEIfLowerIfIndex": juniPPPoEIfLowerIfIndex,
       "juniPPPoEIfAcName": juniPPPoEIfAcName,
       "juniPPPoEIfDupProtect": juniPPPoEIfDupProtect,
       "juniPPPoEIfPADIFlag": juniPPPoEIfPADIFlag,
       "juniPPPoEIfAutoconfig": juniPPPoEIfAutoconfig,
       "juniPPPoEIfServiceNameTable": juniPPPoEIfServiceNameTable,
       "juniPPPoEIfPadrRemoteCircuitIdCapture": juniPPPoEIfPadrRemoteCircuitIdCapture,
       "juniPPPoEIfMtu": juniPPPoEIfMtu,
       "juniPPPoEIfLockoutMin": juniPPPoEIfLockoutMin,
       "juniPPPoEIfLockoutMax": juniPPPoEIfLockoutMax,
       "juniPPPoEMaxSessionVsa": juniPPPoEMaxSessionVsa,
       "juniPPPoEIfStatsTable": juniPPPoEIfStatsTable,
       "juniPPPoEIfStatsEntry": juniPPPoEIfStatsEntry,
       "juniPPPoEIfStatsRxPADI": juniPPPoEIfStatsRxPADI,
       "juniPPPoEIfStatsTxPADO": juniPPPoEIfStatsTxPADO,
       "juniPPPoEIfStatsRxPADR": juniPPPoEIfStatsRxPADR,
       "juniPPPoEIfStatsTxPADS": juniPPPoEIfStatsTxPADS,
       "juniPPPoEIfStatsRxPADT": juniPPPoEIfStatsRxPADT,
       "juniPPPoEIfStatsTxPADT": juniPPPoEIfStatsTxPADT,
       "juniPPPoEIfStatsRxInvVersion": juniPPPoEIfStatsRxInvVersion,
       "juniPPPoEIfStatsRxInvCode": juniPPPoEIfStatsRxInvCode,
       "juniPPPoEIfStatsRxInvTags": juniPPPoEIfStatsRxInvTags,
       "juniPPPoEIfStatsRxInvSession": juniPPPoEIfStatsRxInvSession,
       "juniPPPoEIfStatsRxInvTypes": juniPPPoEIfStatsRxInvTypes,
       "juniPPPoEIfStatsRxInvPackets": juniPPPoEIfStatsRxInvPackets,
       "juniPPPoEIfStatsRxInsufficientResources": juniPPPoEIfStatsRxInsufficientResources,
       "juniPPPoEIfStatsTxPADM": juniPPPoEIfStatsTxPADM,
       "juniPPPoEIfStatsTxPADN": juniPPPoEIfStatsTxPADN,
       "juniPPPoEIfStatsRxInvTagLength": juniPPPoEIfStatsRxInvTagLength,
       "juniPPPoEIfStatsRxInvLength": juniPPPoEIfStatsRxInvLength,
       "juniPPPoEIfStatsRxInvPadISession": juniPPPoEIfStatsRxInvPadISession,
       "juniPPPoEIfStatsRxInvPadRSession": juniPPPoEIfStatsRxInvPadRSession,
       "juniPPPoEIfLockoutTable": juniPPPoEIfLockoutTable,
       "juniPPPoEIfLockoutEntry": juniPPPoEIfLockoutEntry,
       "juniPPPoEIfLockoutClientAddress": juniPPPoEIfLockoutClientAddress,
       "juniPPPoEIfLockoutTime": juniPPPoEIfLockoutTime,
       "juniPPPoEIfLockoutElapsedTime": juniPPPoEIfLockoutElapsedTime,
       "juniPPPoEIfLockoutNextTime": juniPPPoEIfLockoutNextTime,
       "juniPPPoESubIfLayer": juniPPPoESubIfLayer,
       "juniPPPoESubIfNextIfIndex": juniPPPoESubIfNextIfIndex,
       "juniPPPoESubIfTable": juniPPPoESubIfTable,
       "juniPPPoESubIfEntry": juniPPPoESubIfEntry,
       "juniPPPoESubIfIndex": juniPPPoESubIfIndex,
       "juniPPPoESubIfRowStatus": juniPPPoESubIfRowStatus,
       "juniPPPoESubIfLowerIfIndex": juniPPPoESubIfLowerIfIndex,
       "juniPPPoESubIfId": juniPPPoESubIfId,
       "juniPPPoESubIfSessionId": juniPPPoESubIfSessionId,
       "juniPPPoESubIfMotm": juniPPPoESubIfMotm,
       "juniPPPoESubIfUrl": juniPPPoESubIfUrl,
       "juniPPPoEGlobal": juniPPPoEGlobal,
       "juniPPPoEGlobalMotm": juniPPPoEGlobalMotm,
       "juniPPPoEProfile": juniPPPoEProfile,
       "juniPPPoEProfileTable": juniPPPoEProfileTable,
       "juniPPPoEProfileEntry": juniPPPoEProfileEntry,
       "juniPPPoEProfileIndex": juniPPPoEProfileIndex,
       "juniPPPoEProfileRowStatus": juniPPPoEProfileRowStatus,
       "juniPPPoEProfileMotm": juniPPPoEProfileMotm,
       "juniPPPoEProfileUrl": juniPPPoEProfileUrl,
       "juniPPPoESummary": juniPPPoESummary,
       "juniPPPoEMajorInterfaceCount": juniPPPoEMajorInterfaceCount,
       "juniPPPoESummaryMajorIfAdminUp": juniPPPoESummaryMajorIfAdminUp,
       "juniPPPoESummaryMajorIfAdminDown": juniPPPoESummaryMajorIfAdminDown,
       "juniPPPoESummaryMajorIfOperUp": juniPPPoESummaryMajorIfOperUp,
       "juniPPPoESummaryMajorIfOperDown": juniPPPoESummaryMajorIfOperDown,
       "juniPPPoESummaryMajorIfLowerLayerDown": juniPPPoESummaryMajorIfLowerLayerDown,
       "juniPPPoESummaryMajorIfNotPresent": juniPPPoESummaryMajorIfNotPresent,
       "juniPPPoESummarySubInterfaceCount": juniPPPoESummarySubInterfaceCount,
       "juniPPPoESummarySubIfAdminUp": juniPPPoESummarySubIfAdminUp,
       "juniPPPoESummarySubIfAdminDown": juniPPPoESummarySubIfAdminDown,
       "juniPPPoESummarySubIfOperUp": juniPPPoESummarySubIfOperUp,
       "juniPPPoESummarySubIfOperDown": juniPPPoESummarySubIfOperDown,
       "juniPPPoESummarySubIfLowerLayerDown": juniPPPoESummarySubIfLowerLayerDown,
       "juniPPPoESummarySubIfNotPresent": juniPPPoESummarySubIfNotPresent,
       "juniPPPoEServices": juniPPPoEServices,
       "juniPPPoEServiceNameTableNextIndex": juniPPPoEServiceNameTableNextIndex,
       "juniPPPoEServiceNameTableTable": juniPPPoEServiceNameTableTable,
       "juniPPPoEServiceNameTableEntry": juniPPPoEServiceNameTableEntry,
       "juniPPPoEServiceNameTableIndex": juniPPPoEServiceNameTableIndex,
       "juniPPPoEServiceNameTableName": juniPPPoEServiceNameTableName,
       "juniPPPoEServiceNameTableEmptyAction": juniPPPoEServiceNameTableEmptyAction,
       "juniPPPoEServiceNameTableRowStatus": juniPPPoEServiceNameTableRowStatus,
       "juniPPPoEServiceNameTableUnknownAction": juniPPPoEServiceNameTableUnknownAction,
       "juniPPPoEServiceNameTable": juniPPPoEServiceNameTable,
       "juniPPPoEServiceNameEntry": juniPPPoEServiceNameEntry,
       "juniPPPoEServiceName": juniPPPoEServiceName,
       "juniPPPoEServiceNameAction": juniPPPoEServiceNameAction,
       "juniPPPoEServiceNameRowStatus": juniPPPoEServiceNameRowStatus,
       "juniPPPoEConformance": juniPPPoEConformance,
       "juniPPPoEGroups": juniPPPoEGroups,
       "juniPPPoEGroup": juniPPPoEGroup,
       "juniPPPoESubIfGroup": juniPPPoESubIfGroup,
       "juniPPPoEProfileGroup": juniPPPoEProfileGroup,
       "juniPPPoEGroup2": juniPPPoEGroup2,
       "juniPPPoESubIfGroup2": juniPPPoESubIfGroup2,
       "juniPPPoESummaryGroup": juniPPPoESummaryGroup,
       "juniPPPoEGroup3": juniPPPoEGroup3,
       "juniPPPoEGroup4": juniPPPoEGroup4,
       "juniPPPoEGroup5": juniPPPoEGroup5,
       "juniPPPoEGroup6": juniPPPoEGroup6,
       "juniPPPoEServiceNameTableGroup": juniPPPoEServiceNameTableGroup,
       "juniPPPoEGroup7": juniPPPoEGroup7,
       "juniPPPoEGroup8": juniPPPoEGroup8,
       "juniPPPoELockoutTableGroup": juniPPPoELockoutTableGroup,
       "juniPPPoEGroup9": juniPPPoEGroup9,
       "juniPPPoEGroup10": juniPPPoEGroup10,
       "juniPPPoEServiceNameTableGroup1": juniPPPoEServiceNameTableGroup1,
       "juniPPPoECompliances": juniPPPoECompliances,
       "juniPPPoECompliance": juniPPPoECompliance,
       "juniPPPoECompliance2": juniPPPoECompliance2,
       "juniPPPoECompliance3": juniPPPoECompliance3,
       "juniPPPoECompliance4": juniPPPoECompliance4,
       "juniPPPoECompliance5": juniPPPoECompliance5,
       "juniPPPoECompliance6": juniPPPoECompliance6,
       "juniPPPoECompliance7": juniPPPoECompliance7,
       "juniPPPoECompliance8": juniPPPoECompliance8,
       "juniPPPoECompliance9": juniPPPoECompliance9,
       "juniPPPoECompliance10": juniPPPoECompliance10,
       "juniPPPoECompliance11": juniPPPoECompliance11,
       "juniPPPoECompliance12": juniPPPoECompliance12,
       "juniPPPoECompliance13": juniPPPoECompliance13}
)
