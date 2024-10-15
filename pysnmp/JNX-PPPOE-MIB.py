# SNMP MIB module (JNX-PPPOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JNX-PPPOE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:44 2024
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

(jnxPppoeMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxPppoeMibRoot")

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

jnxPPPoEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1)
)
jnxPPPoEMIB.setRevisions(
        ("2013-06-13 00:00",
         "2010-07-22 09:42")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxPPPoEServiceNameAction(Integer32, TextualConvention):
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

_JnxPPPoEObjects_ObjectIdentity = ObjectIdentity
jnxPPPoEObjects = _JnxPPPoEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1)
)
_JnxPPPoEIfLayer_ObjectIdentity = ObjectIdentity
jnxPPPoEIfLayer = _JnxPPPoEIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1)
)
_JnxPPPoENextIfIndex_Type = InterfaceIndexOrZero
_JnxPPPoENextIfIndex_Object = MibScalar
jnxPPPoENextIfIndex = _JnxPPPoENextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 1),
    _JnxPPPoENextIfIndex_Type()
)
jnxPPPoENextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoENextIfIndex.setStatus("current")
_JnxPPPoEIfTable_Object = MibTable
jnxPPPoEIfTable = _JnxPPPoEIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxPPPoEIfTable.setStatus("current")
_JnxPPPoEIfEntry_Object = MibTableRow
jnxPPPoEIfEntry = _JnxPPPoEIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1)
)
jnxPPPoEIfEntry.setIndexNames(
    (0, "JNX-PPPOE-MIB", "jnxPPPoEIfIfIndex"),
)
if mibBuilder.loadTexts:
    jnxPPPoEIfEntry.setStatus("current")
_JnxPPPoEIfIfIndex_Type = InterfaceIndex
_JnxPPPoEIfIfIndex_Object = MibTableColumn
jnxPPPoEIfIfIndex = _JnxPPPoEIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 1),
    _JnxPPPoEIfIfIndex_Type()
)
jnxPPPoEIfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPPPoEIfIfIndex.setStatus("current")


class _JnxPPPoEIfMaxNumSessions_Type(Integer32):
    """Custom type jnxPPPoEIfMaxNumSessions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65335),
    )


_JnxPPPoEIfMaxNumSessions_Type.__name__ = "Integer32"
_JnxPPPoEIfMaxNumSessions_Object = MibTableColumn
jnxPPPoEIfMaxNumSessions = _JnxPPPoEIfMaxNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 2),
    _JnxPPPoEIfMaxNumSessions_Type()
)
jnxPPPoEIfMaxNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfMaxNumSessions.setStatus("current")
_JnxPPPoEIfRowStatus_Type = RowStatus
_JnxPPPoEIfRowStatus_Object = MibTableColumn
jnxPPPoEIfRowStatus = _JnxPPPoEIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 3),
    _JnxPPPoEIfRowStatus_Type()
)
jnxPPPoEIfRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfRowStatus.setStatus("current")
_JnxPPPoEIfLowerIfIndex_Type = InterfaceIndexOrZero
_JnxPPPoEIfLowerIfIndex_Object = MibTableColumn
jnxPPPoEIfLowerIfIndex = _JnxPPPoEIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 4),
    _JnxPPPoEIfLowerIfIndex_Type()
)
jnxPPPoEIfLowerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfLowerIfIndex.setStatus("current")


class _JnxPPPoEIfAcName_Type(DisplayString):
    """Custom type jnxPPPoEIfAcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxPPPoEIfAcName_Type.__name__ = "DisplayString"
_JnxPPPoEIfAcName_Object = MibTableColumn
jnxPPPoEIfAcName = _JnxPPPoEIfAcName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 5),
    _JnxPPPoEIfAcName_Type()
)
jnxPPPoEIfAcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfAcName.setStatus("current")


class _JnxPPPoEIfDupProtect_Type(Integer32):
    """Custom type jnxPPPoEIfDupProtect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPPPoEIfDupProtect_Type.__name__ = "Integer32"
_JnxPPPoEIfDupProtect_Object = MibTableColumn
jnxPPPoEIfDupProtect = _JnxPPPoEIfDupProtect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 6),
    _JnxPPPoEIfDupProtect_Type()
)
jnxPPPoEIfDupProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfDupProtect.setStatus("current")


class _JnxPPPoEIfPADIFlag_Type(Integer32):
    """Custom type jnxPPPoEIfPADIFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPPPoEIfPADIFlag_Type.__name__ = "Integer32"
_JnxPPPoEIfPADIFlag_Object = MibTableColumn
jnxPPPoEIfPADIFlag = _JnxPPPoEIfPADIFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 7),
    _JnxPPPoEIfPADIFlag_Type()
)
jnxPPPoEIfPADIFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfPADIFlag.setStatus("current")


class _JnxPPPoEIfAutoconfig_Type(Integer32):
    """Custom type jnxPPPoEIfAutoconfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPPPoEIfAutoconfig_Type.__name__ = "Integer32"
_JnxPPPoEIfAutoconfig_Object = MibTableColumn
jnxPPPoEIfAutoconfig = _JnxPPPoEIfAutoconfig_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 8),
    _JnxPPPoEIfAutoconfig_Type()
)
jnxPPPoEIfAutoconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfAutoconfig.setStatus("current")


class _JnxPPPoEIfServiceNameTable_Type(DisplayString):
    """Custom type jnxPPPoEIfServiceNameTable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxPPPoEIfServiceNameTable_Type.__name__ = "DisplayString"
_JnxPPPoEIfServiceNameTable_Object = MibTableColumn
jnxPPPoEIfServiceNameTable = _JnxPPPoEIfServiceNameTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 9),
    _JnxPPPoEIfServiceNameTable_Type()
)
jnxPPPoEIfServiceNameTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfServiceNameTable.setStatus("current")


class _JnxPPPoEIfPadrRemoteCircuitIdCapture_Type(Integer32):
    """Custom type jnxPPPoEIfPadrRemoteCircuitIdCapture based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPPPoEIfPadrRemoteCircuitIdCapture_Type.__name__ = "Integer32"
_JnxPPPoEIfPadrRemoteCircuitIdCapture_Object = MibTableColumn
jnxPPPoEIfPadrRemoteCircuitIdCapture = _JnxPPPoEIfPadrRemoteCircuitIdCapture_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 10),
    _JnxPPPoEIfPadrRemoteCircuitIdCapture_Type()
)
jnxPPPoEIfPadrRemoteCircuitIdCapture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfPadrRemoteCircuitIdCapture.setStatus("current")


class _JnxPPPoEIfMtu_Type(Integer32):
    """Custom type jnxPPPoEIfMtu based on Integer32"""
    defaultValue = 1494

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(66, 65535),
    )


_JnxPPPoEIfMtu_Type.__name__ = "Integer32"
_JnxPPPoEIfMtu_Object = MibTableColumn
jnxPPPoEIfMtu = _JnxPPPoEIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 11),
    _JnxPPPoEIfMtu_Type()
)
jnxPPPoEIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfMtu.setStatus("current")


class _JnxPPPoEIfLockoutMin_Type(Integer32):
    """Custom type jnxPPPoEIfLockoutMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JnxPPPoEIfLockoutMin_Type.__name__ = "Integer32"
_JnxPPPoEIfLockoutMin_Object = MibTableColumn
jnxPPPoEIfLockoutMin = _JnxPPPoEIfLockoutMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 12),
    _JnxPPPoEIfLockoutMin_Type()
)
jnxPPPoEIfLockoutMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfLockoutMin.setStatus("current")


class _JnxPPPoEIfLockoutMax_Type(Integer32):
    """Custom type jnxPPPoEIfLockoutMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JnxPPPoEIfLockoutMax_Type.__name__ = "Integer32"
_JnxPPPoEIfLockoutMax_Object = MibTableColumn
jnxPPPoEIfLockoutMax = _JnxPPPoEIfLockoutMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 13),
    _JnxPPPoEIfLockoutMax_Type()
)
jnxPPPoEIfLockoutMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfLockoutMax.setStatus("current")


class _JnxPPPoEIfDynamicProfile_Type(DisplayString):
    """Custom type jnxPPPoEIfDynamicProfile based on DisplayString"""
    defaultValue = OctetString(" ")


_JnxPPPoEIfDynamicProfile_Object = MibTableColumn
jnxPPPoEIfDynamicProfile = _JnxPPPoEIfDynamicProfile_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 14),
    _JnxPPPoEIfDynamicProfile_Type()
)
jnxPPPoEIfDynamicProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfDynamicProfile.setStatus("current")
_JnxPPPoEIfStatsTable_Object = MibTable
jnxPPPoEIfStatsTable = _JnxPPPoEIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsTable.setStatus("current")
_JnxPPPoEIfStatsEntry_Object = MibTableRow
jnxPPPoEIfStatsEntry = _JnxPPPoEIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1)
)
jnxPPPoEIfStatsEntry.setIndexNames(
    (0, "JNX-PPPOE-MIB", "jnxPPPoEIfIfIndex"),
)
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsEntry.setStatus("current")
_JnxPPPoEIfStatsRxPADI_Type = Counter32
_JnxPPPoEIfStatsRxPADI_Object = MibTableColumn
jnxPPPoEIfStatsRxPADI = _JnxPPPoEIfStatsRxPADI_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 1),
    _JnxPPPoEIfStatsRxPADI_Type()
)
jnxPPPoEIfStatsRxPADI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxPADI.setStatus("current")
_JnxPPPoEIfStatsTxPADO_Type = Counter32
_JnxPPPoEIfStatsTxPADO_Object = MibTableColumn
jnxPPPoEIfStatsTxPADO = _JnxPPPoEIfStatsTxPADO_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 2),
    _JnxPPPoEIfStatsTxPADO_Type()
)
jnxPPPoEIfStatsTxPADO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsTxPADO.setStatus("current")
_JnxPPPoEIfStatsRxPADR_Type = Counter32
_JnxPPPoEIfStatsRxPADR_Object = MibTableColumn
jnxPPPoEIfStatsRxPADR = _JnxPPPoEIfStatsRxPADR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 3),
    _JnxPPPoEIfStatsRxPADR_Type()
)
jnxPPPoEIfStatsRxPADR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxPADR.setStatus("current")
_JnxPPPoEIfStatsTxPADS_Type = Counter32
_JnxPPPoEIfStatsTxPADS_Object = MibTableColumn
jnxPPPoEIfStatsTxPADS = _JnxPPPoEIfStatsTxPADS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 4),
    _JnxPPPoEIfStatsTxPADS_Type()
)
jnxPPPoEIfStatsTxPADS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsTxPADS.setStatus("current")
_JnxPPPoEIfStatsRxPADT_Type = Counter32
_JnxPPPoEIfStatsRxPADT_Object = MibTableColumn
jnxPPPoEIfStatsRxPADT = _JnxPPPoEIfStatsRxPADT_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 5),
    _JnxPPPoEIfStatsRxPADT_Type()
)
jnxPPPoEIfStatsRxPADT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxPADT.setStatus("current")
_JnxPPPoEIfStatsTxPADT_Type = Counter32
_JnxPPPoEIfStatsTxPADT_Object = MibTableColumn
jnxPPPoEIfStatsTxPADT = _JnxPPPoEIfStatsTxPADT_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 6),
    _JnxPPPoEIfStatsTxPADT_Type()
)
jnxPPPoEIfStatsTxPADT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsTxPADT.setStatus("current")
_JnxPPPoEIfStatsRxInvVersion_Type = Counter32
_JnxPPPoEIfStatsRxInvVersion_Object = MibTableColumn
jnxPPPoEIfStatsRxInvVersion = _JnxPPPoEIfStatsRxInvVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 7),
    _JnxPPPoEIfStatsRxInvVersion_Type()
)
jnxPPPoEIfStatsRxInvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxInvVersion.setStatus("current")
_JnxPPPoEIfStatsRxInvCode_Type = Counter32
_JnxPPPoEIfStatsRxInvCode_Object = MibTableColumn
jnxPPPoEIfStatsRxInvCode = _JnxPPPoEIfStatsRxInvCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 8),
    _JnxPPPoEIfStatsRxInvCode_Type()
)
jnxPPPoEIfStatsRxInvCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxInvCode.setStatus("current")
_JnxPPPoEIfStatsRxInvTags_Type = Counter32
_JnxPPPoEIfStatsRxInvTags_Object = MibTableColumn
jnxPPPoEIfStatsRxInvTags = _JnxPPPoEIfStatsRxInvTags_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 9),
    _JnxPPPoEIfStatsRxInvTags_Type()
)
jnxPPPoEIfStatsRxInvTags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxInvTags.setStatus("current")
_JnxPPPoEIfStatsRxInvSession_Type = Counter32
_JnxPPPoEIfStatsRxInvSession_Object = MibTableColumn
jnxPPPoEIfStatsRxInvSession = _JnxPPPoEIfStatsRxInvSession_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 10),
    _JnxPPPoEIfStatsRxInvSession_Type()
)
jnxPPPoEIfStatsRxInvSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxInvSession.setStatus("obsolete")
_JnxPPPoEIfStatsRxInvTypes_Type = Counter32
_JnxPPPoEIfStatsRxInvTypes_Object = MibTableColumn
jnxPPPoEIfStatsRxInvTypes = _JnxPPPoEIfStatsRxInvTypes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 11),
    _JnxPPPoEIfStatsRxInvTypes_Type()
)
jnxPPPoEIfStatsRxInvTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxInvTypes.setStatus("current")
_JnxPPPoEIfStatsRxInvPackets_Type = Counter32
_JnxPPPoEIfStatsRxInvPackets_Object = MibTableColumn
jnxPPPoEIfStatsRxInvPackets = _JnxPPPoEIfStatsRxInvPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 12),
    _JnxPPPoEIfStatsRxInvPackets_Type()
)
jnxPPPoEIfStatsRxInvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxInvPackets.setStatus("current")
_JnxPPPoEIfStatsRxInsufficientResources_Type = Counter32
_JnxPPPoEIfStatsRxInsufficientResources_Object = MibTableColumn
jnxPPPoEIfStatsRxInsufficientResources = _JnxPPPoEIfStatsRxInsufficientResources_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 13),
    _JnxPPPoEIfStatsRxInsufficientResources_Type()
)
jnxPPPoEIfStatsRxInsufficientResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxInsufficientResources.setStatus("current")
_JnxPPPoEIfStatsTxPADM_Type = Counter32
_JnxPPPoEIfStatsTxPADM_Object = MibTableColumn
jnxPPPoEIfStatsTxPADM = _JnxPPPoEIfStatsTxPADM_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 14),
    _JnxPPPoEIfStatsTxPADM_Type()
)
jnxPPPoEIfStatsTxPADM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsTxPADM.setStatus("current")
_JnxPPPoEIfStatsTxPADN_Type = Counter32
_JnxPPPoEIfStatsTxPADN_Object = MibTableColumn
jnxPPPoEIfStatsTxPADN = _JnxPPPoEIfStatsTxPADN_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 15),
    _JnxPPPoEIfStatsTxPADN_Type()
)
jnxPPPoEIfStatsTxPADN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsTxPADN.setStatus("current")
_JnxPPPoEIfStatsRxInvTagLength_Type = Counter32
_JnxPPPoEIfStatsRxInvTagLength_Object = MibTableColumn
jnxPPPoEIfStatsRxInvTagLength = _JnxPPPoEIfStatsRxInvTagLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 16),
    _JnxPPPoEIfStatsRxInvTagLength_Type()
)
jnxPPPoEIfStatsRxInvTagLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxInvTagLength.setStatus("current")
_JnxPPPoEIfStatsRxInvLength_Type = Counter32
_JnxPPPoEIfStatsRxInvLength_Object = MibTableColumn
jnxPPPoEIfStatsRxInvLength = _JnxPPPoEIfStatsRxInvLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 17),
    _JnxPPPoEIfStatsRxInvLength_Type()
)
jnxPPPoEIfStatsRxInvLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxInvLength.setStatus("current")
_JnxPPPoEIfStatsRxInvPadISession_Type = Counter32
_JnxPPPoEIfStatsRxInvPadISession_Object = MibTableColumn
jnxPPPoEIfStatsRxInvPadISession = _JnxPPPoEIfStatsRxInvPadISession_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 18),
    _JnxPPPoEIfStatsRxInvPadISession_Type()
)
jnxPPPoEIfStatsRxInvPadISession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxInvPadISession.setStatus("current")
_JnxPPPoEIfStatsRxInvPadRSession_Type = Counter32
_JnxPPPoEIfStatsRxInvPadRSession_Object = MibTableColumn
jnxPPPoEIfStatsRxInvPadRSession = _JnxPPPoEIfStatsRxInvPadRSession_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 19),
    _JnxPPPoEIfStatsRxInvPadRSession_Type()
)
jnxPPPoEIfStatsRxInvPadRSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfStatsRxInvPadRSession.setStatus("current")
_JnxPPPoEIfLockoutTable_Object = MibTable
jnxPPPoEIfLockoutTable = _JnxPPPoEIfLockoutTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxPPPoEIfLockoutTable.setStatus("current")
_JnxPPPoEIfLockoutEntry_Object = MibTableRow
jnxPPPoEIfLockoutEntry = _JnxPPPoEIfLockoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 4, 1)
)
jnxPPPoEIfLockoutEntry.setIndexNames(
    (0, "JNX-PPPOE-MIB", "jnxPPPoEIfIfIndex"),
    (0, "JNX-PPPOE-MIB", "jnxPPPoEIfLockoutClientAddress"),
)
if mibBuilder.loadTexts:
    jnxPPPoEIfLockoutEntry.setStatus("current")
_JnxPPPoEIfLockoutClientAddress_Type = MacAddress
_JnxPPPoEIfLockoutClientAddress_Object = MibTableColumn
jnxPPPoEIfLockoutClientAddress = _JnxPPPoEIfLockoutClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 4, 1, 1),
    _JnxPPPoEIfLockoutClientAddress_Type()
)
jnxPPPoEIfLockoutClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPPPoEIfLockoutClientAddress.setStatus("current")


class _JnxPPPoEIfLockoutTime_Type(Integer32):
    """Custom type jnxPPPoEIfLockoutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JnxPPPoEIfLockoutTime_Type.__name__ = "Integer32"
_JnxPPPoEIfLockoutTime_Object = MibTableColumn
jnxPPPoEIfLockoutTime = _JnxPPPoEIfLockoutTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 4, 1, 2),
    _JnxPPPoEIfLockoutTime_Type()
)
jnxPPPoEIfLockoutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfLockoutTime.setStatus("current")


class _JnxPPPoEIfLockoutElapsedTime_Type(Integer32):
    """Custom type jnxPPPoEIfLockoutElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JnxPPPoEIfLockoutElapsedTime_Type.__name__ = "Integer32"
_JnxPPPoEIfLockoutElapsedTime_Object = MibTableColumn
jnxPPPoEIfLockoutElapsedTime = _JnxPPPoEIfLockoutElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 4, 1, 3),
    _JnxPPPoEIfLockoutElapsedTime_Type()
)
jnxPPPoEIfLockoutElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfLockoutElapsedTime.setStatus("current")


class _JnxPPPoEIfLockoutNextTime_Type(Integer32):
    """Custom type jnxPPPoEIfLockoutNextTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JnxPPPoEIfLockoutNextTime_Type.__name__ = "Integer32"
_JnxPPPoEIfLockoutNextTime_Object = MibTableColumn
jnxPPPoEIfLockoutNextTime = _JnxPPPoEIfLockoutNextTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 4, 1, 4),
    _JnxPPPoEIfLockoutNextTime_Type()
)
jnxPPPoEIfLockoutNextTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEIfLockoutNextTime.setStatus("current")
_JnxPPPoESubIfLayer_ObjectIdentity = ObjectIdentity
jnxPPPoESubIfLayer = _JnxPPPoESubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2)
)
_JnxPPPoESubIfNextIfIndex_Type = InterfaceIndexOrZero
_JnxPPPoESubIfNextIfIndex_Object = MibScalar
jnxPPPoESubIfNextIfIndex = _JnxPPPoESubIfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 1),
    _JnxPPPoESubIfNextIfIndex_Type()
)
jnxPPPoESubIfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESubIfNextIfIndex.setStatus("current")
_JnxPPPoESubIfTable_Object = MibTable
jnxPPPoESubIfTable = _JnxPPPoESubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxPPPoESubIfTable.setStatus("current")
_JnxPPPoESubIfEntry_Object = MibTableRow
jnxPPPoESubIfEntry = _JnxPPPoESubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1)
)
jnxPPPoESubIfEntry.setIndexNames(
    (0, "JNX-PPPOE-MIB", "jnxPPPoESubIfIndex"),
)
if mibBuilder.loadTexts:
    jnxPPPoESubIfEntry.setStatus("current")
_JnxPPPoESubIfIndex_Type = InterfaceIndex
_JnxPPPoESubIfIndex_Object = MibTableColumn
jnxPPPoESubIfIndex = _JnxPPPoESubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 1),
    _JnxPPPoESubIfIndex_Type()
)
jnxPPPoESubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPPPoESubIfIndex.setStatus("current")
_JnxPPPoESubIfRowStatus_Type = RowStatus
_JnxPPPoESubIfRowStatus_Object = MibTableColumn
jnxPPPoESubIfRowStatus = _JnxPPPoESubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 2),
    _JnxPPPoESubIfRowStatus_Type()
)
jnxPPPoESubIfRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESubIfRowStatus.setStatus("current")
_JnxPPPoESubIfLowerIfIndex_Type = InterfaceIndexOrZero
_JnxPPPoESubIfLowerIfIndex_Object = MibTableColumn
jnxPPPoESubIfLowerIfIndex = _JnxPPPoESubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 3),
    _JnxPPPoESubIfLowerIfIndex_Type()
)
jnxPPPoESubIfLowerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESubIfLowerIfIndex.setStatus("current")


class _JnxPPPoESubIfId_Type(Integer32):
    """Custom type jnxPPPoESubIfId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_JnxPPPoESubIfId_Type.__name__ = "Integer32"
_JnxPPPoESubIfId_Object = MibTableColumn
jnxPPPoESubIfId = _JnxPPPoESubIfId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 4),
    _JnxPPPoESubIfId_Type()
)
jnxPPPoESubIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESubIfId.setStatus("current")


class _JnxPPPoESubIfSessionId_Type(Integer32):
    """Custom type jnxPPPoESubIfSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxPPPoESubIfSessionId_Type.__name__ = "Integer32"
_JnxPPPoESubIfSessionId_Object = MibTableColumn
jnxPPPoESubIfSessionId = _JnxPPPoESubIfSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 5),
    _JnxPPPoESubIfSessionId_Type()
)
jnxPPPoESubIfSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESubIfSessionId.setStatus("current")


class _JnxPPPoESubIfMotm_Type(DisplayString):
    """Custom type jnxPPPoESubIfMotm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JnxPPPoESubIfMotm_Type.__name__ = "DisplayString"
_JnxPPPoESubIfMotm_Object = MibTableColumn
jnxPPPoESubIfMotm = _JnxPPPoESubIfMotm_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 6),
    _JnxPPPoESubIfMotm_Type()
)
jnxPPPoESubIfMotm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESubIfMotm.setStatus("current")


class _JnxPPPoESubIfUrl_Type(DisplayString):
    """Custom type jnxPPPoESubIfUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JnxPPPoESubIfUrl_Type.__name__ = "DisplayString"
_JnxPPPoESubIfUrl_Object = MibTableColumn
jnxPPPoESubIfUrl = _JnxPPPoESubIfUrl_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 7),
    _JnxPPPoESubIfUrl_Type()
)
jnxPPPoESubIfUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESubIfUrl.setStatus("current")
_JnxPppoeSubIfQueueStatsTable_Object = MibTable
jnxPppoeSubIfQueueStatsTable = _JnxPppoeSubIfQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxPppoeSubIfQueueStatsTable.setStatus("current")
_JnxPppoeSubIfPerQueueStatsEntry_Object = MibTableRow
jnxPppoeSubIfPerQueueStatsEntry = _JnxPppoeSubIfPerQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1)
)
jnxPppoeSubIfPerQueueStatsEntry.setIndexNames(
    (0, "JNX-PPPOE-MIB", "jnxPPPoESubIfIndex"),
    (0, "JNX-PPPOE-MIB", "jnxPppoeSubIfQueueIndex"),
)
if mibBuilder.loadTexts:
    jnxPppoeSubIfPerQueueStatsEntry.setStatus("current")


class _JnxPppoeSubIfQueueIndex_Type(Integer32):
    """Custom type jnxPppoeSubIfQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_JnxPppoeSubIfQueueIndex_Type.__name__ = "Integer32"
_JnxPppoeSubIfQueueIndex_Object = MibTableColumn
jnxPppoeSubIfQueueIndex = _JnxPppoeSubIfQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 1),
    _JnxPppoeSubIfQueueIndex_Type()
)
jnxPppoeSubIfQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPppoeSubIfQueueIndex.setStatus("current")
_JnxPppoeSubIfQueueStatsPacketSent_Type = Counter64
_JnxPppoeSubIfQueueStatsPacketSent_Object = MibTableColumn
jnxPppoeSubIfQueueStatsPacketSent = _JnxPppoeSubIfQueueStatsPacketSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 2),
    _JnxPppoeSubIfQueueStatsPacketSent_Type()
)
jnxPppoeSubIfQueueStatsPacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppoeSubIfQueueStatsPacketSent.setStatus("current")
_JnxPppoeSubIfQueueStatsBytesSent_Type = Counter64
_JnxPppoeSubIfQueueStatsBytesSent_Object = MibTableColumn
jnxPppoeSubIfQueueStatsBytesSent = _JnxPppoeSubIfQueueStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 3),
    _JnxPppoeSubIfQueueStatsBytesSent_Type()
)
jnxPppoeSubIfQueueStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppoeSubIfQueueStatsBytesSent.setStatus("current")
_JnxPppoeSubIfQueueStatsPacketDropped_Type = Counter64
_JnxPppoeSubIfQueueStatsPacketDropped_Object = MibTableColumn
jnxPppoeSubIfQueueStatsPacketDropped = _JnxPppoeSubIfQueueStatsPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 4),
    _JnxPppoeSubIfQueueStatsPacketDropped_Type()
)
jnxPppoeSubIfQueueStatsPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppoeSubIfQueueStatsPacketDropped.setStatus("current")
_JnxPppoeSubIfQueueStatsBytesDropped_Type = Counter64
_JnxPppoeSubIfQueueStatsBytesDropped_Object = MibTableColumn
jnxPppoeSubIfQueueStatsBytesDropped = _JnxPppoeSubIfQueueStatsBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 5),
    _JnxPppoeSubIfQueueStatsBytesDropped_Type()
)
jnxPppoeSubIfQueueStatsBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppoeSubIfQueueStatsBytesDropped.setStatus("current")
_JnxPppoeSubIfQueueStatsActualBitRate_Type = Counter32
_JnxPppoeSubIfQueueStatsActualBitRate_Object = MibTableColumn
jnxPppoeSubIfQueueStatsActualBitRate = _JnxPppoeSubIfQueueStatsActualBitRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 6),
    _JnxPppoeSubIfQueueStatsActualBitRate_Type()
)
jnxPppoeSubIfQueueStatsActualBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppoeSubIfQueueStatsActualBitRate.setStatus("current")
_JnxPppoeSubIfQueueStatsActualDroppedBitRate_Type = Counter32
_JnxPppoeSubIfQueueStatsActualDroppedBitRate_Object = MibTableColumn
jnxPppoeSubIfQueueStatsActualDroppedBitRate = _JnxPppoeSubIfQueueStatsActualDroppedBitRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 7),
    _JnxPppoeSubIfQueueStatsActualDroppedBitRate_Type()
)
jnxPppoeSubIfQueueStatsActualDroppedBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppoeSubIfQueueStatsActualDroppedBitRate.setStatus("current")
_JnxPPPoESummary_ObjectIdentity = ObjectIdentity
jnxPPPoESummary = _JnxPPPoESummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3)
)
_JnxPPPoEMajorInterfaceCount_Type = Integer32
_JnxPPPoEMajorInterfaceCount_Object = MibScalar
jnxPPPoEMajorInterfaceCount = _JnxPPPoEMajorInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 1),
    _JnxPPPoEMajorInterfaceCount_Type()
)
jnxPPPoEMajorInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEMajorInterfaceCount.setStatus("current")
_JnxPPPoESummaryMajorIfAdminUp_Type = Integer32
_JnxPPPoESummaryMajorIfAdminUp_Object = MibScalar
jnxPPPoESummaryMajorIfAdminUp = _JnxPPPoESummaryMajorIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 2),
    _JnxPPPoESummaryMajorIfAdminUp_Type()
)
jnxPPPoESummaryMajorIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESummaryMajorIfAdminUp.setStatus("current")
_JnxPPPoESummaryMajorIfAdminDown_Type = Integer32
_JnxPPPoESummaryMajorIfAdminDown_Object = MibScalar
jnxPPPoESummaryMajorIfAdminDown = _JnxPPPoESummaryMajorIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 3),
    _JnxPPPoESummaryMajorIfAdminDown_Type()
)
jnxPPPoESummaryMajorIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESummaryMajorIfAdminDown.setStatus("current")
_JnxPPPoESummaryMajorIfOperUp_Type = Integer32
_JnxPPPoESummaryMajorIfOperUp_Object = MibScalar
jnxPPPoESummaryMajorIfOperUp = _JnxPPPoESummaryMajorIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 4),
    _JnxPPPoESummaryMajorIfOperUp_Type()
)
jnxPPPoESummaryMajorIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESummaryMajorIfOperUp.setStatus("current")
_JnxPPPoESummaryMajorIfOperDown_Type = Integer32
_JnxPPPoESummaryMajorIfOperDown_Object = MibScalar
jnxPPPoESummaryMajorIfOperDown = _JnxPPPoESummaryMajorIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 5),
    _JnxPPPoESummaryMajorIfOperDown_Type()
)
jnxPPPoESummaryMajorIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESummaryMajorIfOperDown.setStatus("current")
_JnxPPPoESummaryMajorIfLowerLayerDown_Type = Integer32
_JnxPPPoESummaryMajorIfLowerLayerDown_Object = MibScalar
jnxPPPoESummaryMajorIfLowerLayerDown = _JnxPPPoESummaryMajorIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 6),
    _JnxPPPoESummaryMajorIfLowerLayerDown_Type()
)
jnxPPPoESummaryMajorIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESummaryMajorIfLowerLayerDown.setStatus("current")
_JnxPPPoESummaryMajorIfNotPresent_Type = Integer32
_JnxPPPoESummaryMajorIfNotPresent_Object = MibScalar
jnxPPPoESummaryMajorIfNotPresent = _JnxPPPoESummaryMajorIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 7),
    _JnxPPPoESummaryMajorIfNotPresent_Type()
)
jnxPPPoESummaryMajorIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESummaryMajorIfNotPresent.setStatus("current")
_JnxPPPoESummarySubInterfaceCount_Type = Integer32
_JnxPPPoESummarySubInterfaceCount_Object = MibScalar
jnxPPPoESummarySubInterfaceCount = _JnxPPPoESummarySubInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 8),
    _JnxPPPoESummarySubInterfaceCount_Type()
)
jnxPPPoESummarySubInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESummarySubInterfaceCount.setStatus("current")
_JnxPPPoESummarySubIfAdminUp_Type = Integer32
_JnxPPPoESummarySubIfAdminUp_Object = MibScalar
jnxPPPoESummarySubIfAdminUp = _JnxPPPoESummarySubIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 9),
    _JnxPPPoESummarySubIfAdminUp_Type()
)
jnxPPPoESummarySubIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESummarySubIfAdminUp.setStatus("current")
_JnxPPPoESummarySubIfAdminDown_Type = Integer32
_JnxPPPoESummarySubIfAdminDown_Object = MibScalar
jnxPPPoESummarySubIfAdminDown = _JnxPPPoESummarySubIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 10),
    _JnxPPPoESummarySubIfAdminDown_Type()
)
jnxPPPoESummarySubIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESummarySubIfAdminDown.setStatus("current")
_JnxPPPoESummarySubIfOperUp_Type = Integer32
_JnxPPPoESummarySubIfOperUp_Object = MibScalar
jnxPPPoESummarySubIfOperUp = _JnxPPPoESummarySubIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 11),
    _JnxPPPoESummarySubIfOperUp_Type()
)
jnxPPPoESummarySubIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESummarySubIfOperUp.setStatus("current")
_JnxPPPoESummarySubIfOperDown_Type = Integer32
_JnxPPPoESummarySubIfOperDown_Object = MibScalar
jnxPPPoESummarySubIfOperDown = _JnxPPPoESummarySubIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 12),
    _JnxPPPoESummarySubIfOperDown_Type()
)
jnxPPPoESummarySubIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESummarySubIfOperDown.setStatus("current")
_JnxPPPoESummarySubIfLowerLayerDown_Type = Integer32
_JnxPPPoESummarySubIfLowerLayerDown_Object = MibScalar
jnxPPPoESummarySubIfLowerLayerDown = _JnxPPPoESummarySubIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 13),
    _JnxPPPoESummarySubIfLowerLayerDown_Type()
)
jnxPPPoESummarySubIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESummarySubIfLowerLayerDown.setStatus("current")
_JnxPPPoESummarySubIfNotPresent_Type = Integer32
_JnxPPPoESummarySubIfNotPresent_Object = MibScalar
jnxPPPoESummarySubIfNotPresent = _JnxPPPoESummarySubIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 14),
    _JnxPPPoESummarySubIfNotPresent_Type()
)
jnxPPPoESummarySubIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoESummarySubIfNotPresent.setStatus("current")
_JnxPPPoEServices_ObjectIdentity = ObjectIdentity
jnxPPPoEServices = _JnxPPPoEServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4)
)
_JnxPPPoEServiceNameTableTable_Object = MibTable
jnxPPPoEServiceNameTableTable = _JnxPPPoEServiceNameTableTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameTableTable.setStatus("current")
_JnxPPPoEServiceNameTableEntry_Object = MibTableRow
jnxPPPoEServiceNameTableEntry = _JnxPPPoEServiceNameTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 1, 1)
)
jnxPPPoEServiceNameTableEntry.setIndexNames(
    (0, "JNX-PPPOE-MIB", "jnxPPPoEServiceNameTableName"),
)
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameTableEntry.setStatus("current")


class _JnxPPPoEServiceNameTableName_Type(DisplayString):
    """Custom type jnxPPPoEServiceNameTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JnxPPPoEServiceNameTableName_Type.__name__ = "DisplayString"
_JnxPPPoEServiceNameTableName_Object = MibTableColumn
jnxPPPoEServiceNameTableName = _JnxPPPoEServiceNameTableName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 1, 1, 1),
    _JnxPPPoEServiceNameTableName_Type()
)
jnxPPPoEServiceNameTableName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameTableName.setStatus("current")
_JnxPPPoEServiceNameTableRowStatus_Type = RowStatus
_JnxPPPoEServiceNameTableRowStatus_Object = MibTableColumn
jnxPPPoEServiceNameTableRowStatus = _JnxPPPoEServiceNameTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 1, 1, 2),
    _JnxPPPoEServiceNameTableRowStatus_Type()
)
jnxPPPoEServiceNameTableRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameTableRowStatus.setStatus("current")
_JnxPPPoEServiceNameTable_Object = MibTable
jnxPPPoEServiceNameTable = _JnxPPPoEServiceNameTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameTable.setStatus("current")
_JnxPPPoEServiceNameEntry_Object = MibTableRow
jnxPPPoEServiceNameEntry = _JnxPPPoEServiceNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1)
)
jnxPPPoEServiceNameEntry.setIndexNames(
    (0, "JNX-PPPOE-MIB", "jnxPPPoEServiceNameTableName"),
    (0, "JNX-PPPOE-MIB", "jnxPPPoEServiceName"),
)
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameEntry.setStatus("current")


class _JnxPPPoEServiceName_Type(DisplayString):
    """Custom type jnxPPPoEServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxPPPoEServiceName_Type.__name__ = "DisplayString"
_JnxPPPoEServiceName_Object = MibTableColumn
jnxPPPoEServiceName = _JnxPPPoEServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1, 1),
    _JnxPPPoEServiceName_Type()
)
jnxPPPoEServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPPPoEServiceName.setStatus("current")
_JnxPPPoEServiceNameAction_Type = JnxPPPoEServiceNameAction
_JnxPPPoEServiceNameAction_Object = MibTableColumn
jnxPPPoEServiceNameAction = _JnxPPPoEServiceNameAction_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1, 2),
    _JnxPPPoEServiceNameAction_Type()
)
jnxPPPoEServiceNameAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameAction.setStatus("current")
_JnxPPPoEServiceNameDynamicProfile_Type = DisplayString
_JnxPPPoEServiceNameDynamicProfile_Object = MibTableColumn
jnxPPPoEServiceNameDynamicProfile = _JnxPPPoEServiceNameDynamicProfile_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1, 3),
    _JnxPPPoEServiceNameDynamicProfile_Type()
)
jnxPPPoEServiceNameDynamicProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameDynamicProfile.setStatus("current")
_JnxPPPoEServiceNameRoutingInstance_Type = DisplayString
_JnxPPPoEServiceNameRoutingInstance_Object = MibTableColumn
jnxPPPoEServiceNameRoutingInstance = _JnxPPPoEServiceNameRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1, 4),
    _JnxPPPoEServiceNameRoutingInstance_Type()
)
jnxPPPoEServiceNameRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameRoutingInstance.setStatus("current")
_JnxPPPoEServiceNameMaxSessions_Type = Unsigned32
_JnxPPPoEServiceNameMaxSessions_Object = MibTableColumn
jnxPPPoEServiceNameMaxSessions = _JnxPPPoEServiceNameMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1, 5),
    _JnxPPPoEServiceNameMaxSessions_Type()
)
jnxPPPoEServiceNameMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameMaxSessions.setStatus("current")
_JnxPPPoEServiceNameRowStatus_Type = RowStatus
_JnxPPPoEServiceNameRowStatus_Object = MibTableColumn
jnxPPPoEServiceNameRowStatus = _JnxPPPoEServiceNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1, 6),
    _JnxPPPoEServiceNameRowStatus_Type()
)
jnxPPPoEServiceNameRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameRowStatus.setStatus("current")
_JnxPPPoEServiceNameAciAriTable_Object = MibTable
jnxPPPoEServiceNameAciAriTable = _JnxPPPoEServiceNameAciAriTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameAciAriTable.setStatus("current")
_JnxPPPoEServiceNameAciAriEntry_Object = MibTableRow
jnxPPPoEServiceNameAciAriEntry = _JnxPPPoEServiceNameAciAriEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1)
)
jnxPPPoEServiceNameAciAriEntry.setIndexNames(
    (0, "JNX-PPPOE-MIB", "jnxPPPoEServiceNameTableName"),
    (0, "JNX-PPPOE-MIB", "jnxPPPoEServiceName"),
    (0, "JNX-PPPOE-MIB", "jnxPPPoEServiceNameAgentCircuitId"),
    (0, "JNX-PPPOE-MIB", "jnxPPPoEServiceNameAgentRemoteId"),
)
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameAciAriEntry.setStatus("current")


class _JnxPPPoEServiceNameAgentCircuitId_Type(DisplayString):
    """Custom type jnxPPPoEServiceNameAgentCircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxPPPoEServiceNameAgentCircuitId_Type.__name__ = "DisplayString"
_JnxPPPoEServiceNameAgentCircuitId_Object = MibTableColumn
jnxPPPoEServiceNameAgentCircuitId = _JnxPPPoEServiceNameAgentCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 1),
    _JnxPPPoEServiceNameAgentCircuitId_Type()
)
jnxPPPoEServiceNameAgentCircuitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameAgentCircuitId.setStatus("current")


class _JnxPPPoEServiceNameAgentRemoteId_Type(DisplayString):
    """Custom type jnxPPPoEServiceNameAgentRemoteId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxPPPoEServiceNameAgentRemoteId_Type.__name__ = "DisplayString"
_JnxPPPoEServiceNameAgentRemoteId_Object = MibTableColumn
jnxPPPoEServiceNameAgentRemoteId = _JnxPPPoEServiceNameAgentRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 2),
    _JnxPPPoEServiceNameAgentRemoteId_Type()
)
jnxPPPoEServiceNameAgentRemoteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameAgentRemoteId.setStatus("current")
_JnxPPPoEServiceNameAciAriAction_Type = JnxPPPoEServiceNameAction
_JnxPPPoEServiceNameAciAriAction_Object = MibTableColumn
jnxPPPoEServiceNameAciAriAction = _JnxPPPoEServiceNameAciAriAction_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 3),
    _JnxPPPoEServiceNameAciAriAction_Type()
)
jnxPPPoEServiceNameAciAriAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameAciAriAction.setStatus("current")
_JnxPPPoEServiceNameAciAriDynamicProfile_Type = DisplayString
_JnxPPPoEServiceNameAciAriDynamicProfile_Object = MibTableColumn
jnxPPPoEServiceNameAciAriDynamicProfile = _JnxPPPoEServiceNameAciAriDynamicProfile_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 4),
    _JnxPPPoEServiceNameAciAriDynamicProfile_Type()
)
jnxPPPoEServiceNameAciAriDynamicProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameAciAriDynamicProfile.setStatus("current")


class _JnxPPPoEServiceNameAciAriRoutingInstance_Type(DisplayString):
    """Custom type jnxPPPoEServiceNameAciAriRoutingInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_JnxPPPoEServiceNameAciAriRoutingInstance_Type.__name__ = "DisplayString"
_JnxPPPoEServiceNameAciAriRoutingInstance_Object = MibTableColumn
jnxPPPoEServiceNameAciAriRoutingInstance = _JnxPPPoEServiceNameAciAriRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 5),
    _JnxPPPoEServiceNameAciAriRoutingInstance_Type()
)
jnxPPPoEServiceNameAciAriRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameAciAriRoutingInstance.setStatus("current")
_JnxPPPoEServiceNameAciAriStaticInterface_Type = DisplayString
_JnxPPPoEServiceNameAciAriStaticInterface_Object = MibTableColumn
jnxPPPoEServiceNameAciAriStaticInterface = _JnxPPPoEServiceNameAciAriStaticInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 6),
    _JnxPPPoEServiceNameAciAriStaticInterface_Type()
)
jnxPPPoEServiceNameAciAriStaticInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameAciAriStaticInterface.setStatus("current")
_JnxPPPoEServiceNameAciAriRowStatus_Type = RowStatus
_JnxPPPoEServiceNameAciAriRowStatus_Object = MibTableColumn
jnxPPPoEServiceNameAciAriRowStatus = _JnxPPPoEServiceNameAciAriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 7),
    _JnxPPPoEServiceNameAciAriRowStatus_Type()
)
jnxPPPoEServiceNameAciAriRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPPPoEServiceNameAciAriRowStatus.setStatus("current")
_JnxPPPoEConformance_ObjectIdentity = ObjectIdentity
jnxPPPoEConformance = _JnxPPPoEConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 4)
)
_JnxPPPoECompliances_ObjectIdentity = ObjectIdentity
jnxPPPoECompliances = _JnxPPPoECompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 4, 1)
)
_JnxPPPoEGroups_ObjectIdentity = ObjectIdentity
jnxPPPoEGroups = _JnxPPPoEGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 4, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JNX-PPPOE-MIB",
    **{"JnxPPPoEServiceNameAction": JnxPPPoEServiceNameAction,
       "jnxPPPoEMIB": jnxPPPoEMIB,
       "jnxPPPoEObjects": jnxPPPoEObjects,
       "jnxPPPoEIfLayer": jnxPPPoEIfLayer,
       "jnxPPPoENextIfIndex": jnxPPPoENextIfIndex,
       "jnxPPPoEIfTable": jnxPPPoEIfTable,
       "jnxPPPoEIfEntry": jnxPPPoEIfEntry,
       "jnxPPPoEIfIfIndex": jnxPPPoEIfIfIndex,
       "jnxPPPoEIfMaxNumSessions": jnxPPPoEIfMaxNumSessions,
       "jnxPPPoEIfRowStatus": jnxPPPoEIfRowStatus,
       "jnxPPPoEIfLowerIfIndex": jnxPPPoEIfLowerIfIndex,
       "jnxPPPoEIfAcName": jnxPPPoEIfAcName,
       "jnxPPPoEIfDupProtect": jnxPPPoEIfDupProtect,
       "jnxPPPoEIfPADIFlag": jnxPPPoEIfPADIFlag,
       "jnxPPPoEIfAutoconfig": jnxPPPoEIfAutoconfig,
       "jnxPPPoEIfServiceNameTable": jnxPPPoEIfServiceNameTable,
       "jnxPPPoEIfPadrRemoteCircuitIdCapture": jnxPPPoEIfPadrRemoteCircuitIdCapture,
       "jnxPPPoEIfMtu": jnxPPPoEIfMtu,
       "jnxPPPoEIfLockoutMin": jnxPPPoEIfLockoutMin,
       "jnxPPPoEIfLockoutMax": jnxPPPoEIfLockoutMax,
       "jnxPPPoEIfDynamicProfile": jnxPPPoEIfDynamicProfile,
       "jnxPPPoEIfStatsTable": jnxPPPoEIfStatsTable,
       "jnxPPPoEIfStatsEntry": jnxPPPoEIfStatsEntry,
       "jnxPPPoEIfStatsRxPADI": jnxPPPoEIfStatsRxPADI,
       "jnxPPPoEIfStatsTxPADO": jnxPPPoEIfStatsTxPADO,
       "jnxPPPoEIfStatsRxPADR": jnxPPPoEIfStatsRxPADR,
       "jnxPPPoEIfStatsTxPADS": jnxPPPoEIfStatsTxPADS,
       "jnxPPPoEIfStatsRxPADT": jnxPPPoEIfStatsRxPADT,
       "jnxPPPoEIfStatsTxPADT": jnxPPPoEIfStatsTxPADT,
       "jnxPPPoEIfStatsRxInvVersion": jnxPPPoEIfStatsRxInvVersion,
       "jnxPPPoEIfStatsRxInvCode": jnxPPPoEIfStatsRxInvCode,
       "jnxPPPoEIfStatsRxInvTags": jnxPPPoEIfStatsRxInvTags,
       "jnxPPPoEIfStatsRxInvSession": jnxPPPoEIfStatsRxInvSession,
       "jnxPPPoEIfStatsRxInvTypes": jnxPPPoEIfStatsRxInvTypes,
       "jnxPPPoEIfStatsRxInvPackets": jnxPPPoEIfStatsRxInvPackets,
       "jnxPPPoEIfStatsRxInsufficientResources": jnxPPPoEIfStatsRxInsufficientResources,
       "jnxPPPoEIfStatsTxPADM": jnxPPPoEIfStatsTxPADM,
       "jnxPPPoEIfStatsTxPADN": jnxPPPoEIfStatsTxPADN,
       "jnxPPPoEIfStatsRxInvTagLength": jnxPPPoEIfStatsRxInvTagLength,
       "jnxPPPoEIfStatsRxInvLength": jnxPPPoEIfStatsRxInvLength,
       "jnxPPPoEIfStatsRxInvPadISession": jnxPPPoEIfStatsRxInvPadISession,
       "jnxPPPoEIfStatsRxInvPadRSession": jnxPPPoEIfStatsRxInvPadRSession,
       "jnxPPPoEIfLockoutTable": jnxPPPoEIfLockoutTable,
       "jnxPPPoEIfLockoutEntry": jnxPPPoEIfLockoutEntry,
       "jnxPPPoEIfLockoutClientAddress": jnxPPPoEIfLockoutClientAddress,
       "jnxPPPoEIfLockoutTime": jnxPPPoEIfLockoutTime,
       "jnxPPPoEIfLockoutElapsedTime": jnxPPPoEIfLockoutElapsedTime,
       "jnxPPPoEIfLockoutNextTime": jnxPPPoEIfLockoutNextTime,
       "jnxPPPoESubIfLayer": jnxPPPoESubIfLayer,
       "jnxPPPoESubIfNextIfIndex": jnxPPPoESubIfNextIfIndex,
       "jnxPPPoESubIfTable": jnxPPPoESubIfTable,
       "jnxPPPoESubIfEntry": jnxPPPoESubIfEntry,
       "jnxPPPoESubIfIndex": jnxPPPoESubIfIndex,
       "jnxPPPoESubIfRowStatus": jnxPPPoESubIfRowStatus,
       "jnxPPPoESubIfLowerIfIndex": jnxPPPoESubIfLowerIfIndex,
       "jnxPPPoESubIfId": jnxPPPoESubIfId,
       "jnxPPPoESubIfSessionId": jnxPPPoESubIfSessionId,
       "jnxPPPoESubIfMotm": jnxPPPoESubIfMotm,
       "jnxPPPoESubIfUrl": jnxPPPoESubIfUrl,
       "jnxPppoeSubIfQueueStatsTable": jnxPppoeSubIfQueueStatsTable,
       "jnxPppoeSubIfPerQueueStatsEntry": jnxPppoeSubIfPerQueueStatsEntry,
       "jnxPppoeSubIfQueueIndex": jnxPppoeSubIfQueueIndex,
       "jnxPppoeSubIfQueueStatsPacketSent": jnxPppoeSubIfQueueStatsPacketSent,
       "jnxPppoeSubIfQueueStatsBytesSent": jnxPppoeSubIfQueueStatsBytesSent,
       "jnxPppoeSubIfQueueStatsPacketDropped": jnxPppoeSubIfQueueStatsPacketDropped,
       "jnxPppoeSubIfQueueStatsBytesDropped": jnxPppoeSubIfQueueStatsBytesDropped,
       "jnxPppoeSubIfQueueStatsActualBitRate": jnxPppoeSubIfQueueStatsActualBitRate,
       "jnxPppoeSubIfQueueStatsActualDroppedBitRate": jnxPppoeSubIfQueueStatsActualDroppedBitRate,
       "jnxPPPoESummary": jnxPPPoESummary,
       "jnxPPPoEMajorInterfaceCount": jnxPPPoEMajorInterfaceCount,
       "jnxPPPoESummaryMajorIfAdminUp": jnxPPPoESummaryMajorIfAdminUp,
       "jnxPPPoESummaryMajorIfAdminDown": jnxPPPoESummaryMajorIfAdminDown,
       "jnxPPPoESummaryMajorIfOperUp": jnxPPPoESummaryMajorIfOperUp,
       "jnxPPPoESummaryMajorIfOperDown": jnxPPPoESummaryMajorIfOperDown,
       "jnxPPPoESummaryMajorIfLowerLayerDown": jnxPPPoESummaryMajorIfLowerLayerDown,
       "jnxPPPoESummaryMajorIfNotPresent": jnxPPPoESummaryMajorIfNotPresent,
       "jnxPPPoESummarySubInterfaceCount": jnxPPPoESummarySubInterfaceCount,
       "jnxPPPoESummarySubIfAdminUp": jnxPPPoESummarySubIfAdminUp,
       "jnxPPPoESummarySubIfAdminDown": jnxPPPoESummarySubIfAdminDown,
       "jnxPPPoESummarySubIfOperUp": jnxPPPoESummarySubIfOperUp,
       "jnxPPPoESummarySubIfOperDown": jnxPPPoESummarySubIfOperDown,
       "jnxPPPoESummarySubIfLowerLayerDown": jnxPPPoESummarySubIfLowerLayerDown,
       "jnxPPPoESummarySubIfNotPresent": jnxPPPoESummarySubIfNotPresent,
       "jnxPPPoEServices": jnxPPPoEServices,
       "jnxPPPoEServiceNameTableTable": jnxPPPoEServiceNameTableTable,
       "jnxPPPoEServiceNameTableEntry": jnxPPPoEServiceNameTableEntry,
       "jnxPPPoEServiceNameTableName": jnxPPPoEServiceNameTableName,
       "jnxPPPoEServiceNameTableRowStatus": jnxPPPoEServiceNameTableRowStatus,
       "jnxPPPoEServiceNameTable": jnxPPPoEServiceNameTable,
       "jnxPPPoEServiceNameEntry": jnxPPPoEServiceNameEntry,
       "jnxPPPoEServiceName": jnxPPPoEServiceName,
       "jnxPPPoEServiceNameAction": jnxPPPoEServiceNameAction,
       "jnxPPPoEServiceNameDynamicProfile": jnxPPPoEServiceNameDynamicProfile,
       "jnxPPPoEServiceNameRoutingInstance": jnxPPPoEServiceNameRoutingInstance,
       "jnxPPPoEServiceNameMaxSessions": jnxPPPoEServiceNameMaxSessions,
       "jnxPPPoEServiceNameRowStatus": jnxPPPoEServiceNameRowStatus,
       "jnxPPPoEServiceNameAciAriTable": jnxPPPoEServiceNameAciAriTable,
       "jnxPPPoEServiceNameAciAriEntry": jnxPPPoEServiceNameAciAriEntry,
       "jnxPPPoEServiceNameAgentCircuitId": jnxPPPoEServiceNameAgentCircuitId,
       "jnxPPPoEServiceNameAgentRemoteId": jnxPPPoEServiceNameAgentRemoteId,
       "jnxPPPoEServiceNameAciAriAction": jnxPPPoEServiceNameAciAriAction,
       "jnxPPPoEServiceNameAciAriDynamicProfile": jnxPPPoEServiceNameAciAriDynamicProfile,
       "jnxPPPoEServiceNameAciAriRoutingInstance": jnxPPPoEServiceNameAciAriRoutingInstance,
       "jnxPPPoEServiceNameAciAriStaticInterface": jnxPPPoEServiceNameAciAriStaticInterface,
       "jnxPPPoEServiceNameAciAriRowStatus": jnxPPPoEServiceNameAciAriRowStatus,
       "jnxPPPoEConformance": jnxPPPoEConformance,
       "jnxPPPoECompliances": jnxPPPoECompliances,
       "jnxPPPoEGroups": jnxPPPoEGroups}
)
