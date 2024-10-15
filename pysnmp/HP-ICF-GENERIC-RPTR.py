# SNMP MIB module (HP-ICF-GENERIC-RPTR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-GENERIC-RPTR
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:26 2024
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

(hpicfGenRptrTrapsPrefix,
 hpicfGenericRepeater,
 hpicfObjectModules,
 icfHub) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfGenRptrTrapsPrefix",
    "hpicfGenericRepeater",
    "hpicfObjectModules",
    "icfHub")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

hpicfGenRptrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8)
)
hpicfGenRptrMib.setRevisions(
        ("2009-10-26 12:03",
         "2003-06-09 22:37",
         "2000-11-03 07:17",
         "1998-07-23 01:03",
         "1997-03-06 03:37",
         "1996-09-10 02:28",
         "1995-10-23 23:47",
         "1995-01-18 00:00",
         "1993-07-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HubSecurity_ObjectIdentity = ObjectIdentity
hubSecurity = _HubSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10)
)
_HubSecurePortTable_Object = MibTable
hubSecurePortTable = _HubSecurePortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1)
)
if mibBuilder.loadTexts:
    hubSecurePortTable.setStatus("current")
_HubSecurePortEntry_Object = MibTableRow
hubSecurePortEntry = _HubSecurePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1)
)
hubSecurePortEntry.setIndexNames(
    (0, "HP-ICF-GENERIC-RPTR", "hubSecPtGroupIndex"),
    (0, "HP-ICF-GENERIC-RPTR", "hubSecPtPortIndex"),
)
if mibBuilder.loadTexts:
    hubSecurePortEntry.setStatus("current")


class _HubSecPtGroupIndex_Type(Integer32):
    """Custom type hubSecPtGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HubSecPtGroupIndex_Type.__name__ = "Integer32"
_HubSecPtGroupIndex_Object = MibTableColumn
hubSecPtGroupIndex = _HubSecPtGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 1),
    _HubSecPtGroupIndex_Type()
)
hubSecPtGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubSecPtGroupIndex.setStatus("current")


class _HubSecPtPortIndex_Type(Integer32):
    """Custom type hubSecPtPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HubSecPtPortIndex_Type.__name__ = "Integer32"
_HubSecPtPortIndex_Object = MibTableColumn
hubSecPtPortIndex = _HubSecPtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 2),
    _HubSecPtPortIndex_Type()
)
hubSecPtPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubSecPtPortIndex.setStatus("current")
_HubSecPtSecurityAddress_Type = MacAddress
_HubSecPtSecurityAddress_Object = MibTableColumn
hubSecPtSecurityAddress = _HubSecPtSecurityAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 3),
    _HubSecPtSecurityAddress_Type()
)
hubSecPtSecurityAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubSecPtSecurityAddress.setStatus("current")
_HubSecPtAuthorizedAddress_Type = MacAddress
_HubSecPtAuthorizedAddress_Object = MibTableColumn
hubSecPtAuthorizedAddress = _HubSecPtAuthorizedAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 4),
    _HubSecPtAuthorizedAddress_Type()
)
hubSecPtAuthorizedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubSecPtAuthorizedAddress.setStatus("current")


class _HubSecPtPreventEavesdrop_Type(Integer32):
    """Custom type hubSecPtPreventEavesdrop based on Integer32"""
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


_HubSecPtPreventEavesdrop_Type.__name__ = "Integer32"
_HubSecPtPreventEavesdrop_Object = MibTableColumn
hubSecPtPreventEavesdrop = _HubSecPtPreventEavesdrop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 5),
    _HubSecPtPreventEavesdrop_Type()
)
hubSecPtPreventEavesdrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubSecPtPreventEavesdrop.setStatus("current")


class _HubSecPtAlarmEnable_Type(Integer32):
    """Custom type hubSecPtAlarmEnable based on Integer32"""
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


_HubSecPtAlarmEnable_Type.__name__ = "Integer32"
_HubSecPtAlarmEnable_Object = MibTableColumn
hubSecPtAlarmEnable = _HubSecPtAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 6),
    _HubSecPtAlarmEnable_Type()
)
hubSecPtAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubSecPtAlarmEnable.setStatus("current")


class _HubSecPtIntrusionFlag_Type(Integer32):
    """Custom type hubSecPtIntrusionFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intrusion", 1),
          ("noIntrusion", 2))
    )


_HubSecPtIntrusionFlag_Type.__name__ = "Integer32"
_HubSecPtIntrusionFlag_Object = MibTableColumn
hubSecPtIntrusionFlag = _HubSecPtIntrusionFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 1, 1, 7),
    _HubSecPtIntrusionFlag_Type()
)
hubSecPtIntrusionFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubSecPtIntrusionFlag.setStatus("current")
_HubIntruderLogTable_Object = MibTable
hubIntruderLogTable = _HubIntruderLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2)
)
if mibBuilder.loadTexts:
    hubIntruderLogTable.setStatus("current")
_HubIntruderLogEntry_Object = MibTableRow
hubIntruderLogEntry = _HubIntruderLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1)
)
hubIntruderLogEntry.setIndexNames(
    (0, "HP-ICF-GENERIC-RPTR", "hubIntruderIndex"),
)
if mibBuilder.loadTexts:
    hubIntruderLogEntry.setStatus("current")


class _HubIntruderIndex_Type(Integer32):
    """Custom type hubIntruderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HubIntruderIndex_Type.__name__ = "Integer32"
_HubIntruderIndex_Object = MibTableColumn
hubIntruderIndex = _HubIntruderIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1, 1),
    _HubIntruderIndex_Type()
)
hubIntruderIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIntruderIndex.setStatus("current")


class _HubIntruderGroup_Type(Integer32):
    """Custom type hubIntruderGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HubIntruderGroup_Type.__name__ = "Integer32"
_HubIntruderGroup_Object = MibTableColumn
hubIntruderGroup = _HubIntruderGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1, 2),
    _HubIntruderGroup_Type()
)
hubIntruderGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIntruderGroup.setStatus("current")


class _HubIntruderPort_Type(Integer32):
    """Custom type hubIntruderPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HubIntruderPort_Type.__name__ = "Integer32"
_HubIntruderPort_Object = MibTableColumn
hubIntruderPort = _HubIntruderPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1, 3),
    _HubIntruderPort_Type()
)
hubIntruderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIntruderPort.setStatus("current")
_HubIntruderAddress_Type = MacAddress
_HubIntruderAddress_Object = MibTableColumn
hubIntruderAddress = _HubIntruderAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1, 4),
    _HubIntruderAddress_Type()
)
hubIntruderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIntruderAddress.setStatus("current")
_HubIntruderTime_Type = TimeStamp
_HubIntruderTime_Object = MibTableColumn
hubIntruderTime = _HubIntruderTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1, 5),
    _HubIntruderTime_Type()
)
hubIntruderTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIntruderTime.setStatus("current")


class _HubIntruderType_Type(Integer32):
    """Custom type hubIntruderType based on Integer32"""
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
        *(("address", 1),
          ("both", 3),
          ("none", 4),
          ("training", 2))
    )


_HubIntruderType_Type.__name__ = "Integer32"
_HubIntruderType_Object = MibTableColumn
hubIntruderType = _HubIntruderType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1, 6),
    _HubIntruderType_Type()
)
hubIntruderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIntruderType.setStatus("current")


class _HubIntruderTrainingViolation_Type(Integer32):
    """Custom type hubIntruderTrainingViolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noViolation", 1),
          ("promiscuousViolation", 2),
          ("repeaterViolation", 3))
    )


_HubIntruderTrainingViolation_Type.__name__ = "Integer32"
_HubIntruderTrainingViolation_Object = MibTableColumn
hubIntruderTrainingViolation = _HubIntruderTrainingViolation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 2, 1, 7),
    _HubIntruderTrainingViolation_Type()
)
hubIntruderTrainingViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubIntruderTrainingViolation.setStatus("current")
_HpSecurePortTable_Object = MibTable
hpSecurePortTable = _HpSecurePortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 3)
)
if mibBuilder.loadTexts:
    hpSecurePortTable.setStatus("current")
_HpSecurePortEntry_Object = MibTableRow
hpSecurePortEntry = _HpSecurePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 3, 1)
)
hpSecurePortEntry.setIndexNames(
    (0, "HP-ICF-GENERIC-RPTR", "hpSecPtGroupIndex"),
    (0, "HP-ICF-GENERIC-RPTR", "hpSecPtPortIndex"),
)
if mibBuilder.loadTexts:
    hpSecurePortEntry.setStatus("current")


class _HpSecPtGroupIndex_Type(Integer32):
    """Custom type hpSecPtGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpSecPtGroupIndex_Type.__name__ = "Integer32"
_HpSecPtGroupIndex_Object = MibTableColumn
hpSecPtGroupIndex = _HpSecPtGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 3, 1, 1),
    _HpSecPtGroupIndex_Type()
)
hpSecPtGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSecPtGroupIndex.setStatus("current")


class _HpSecPtPortIndex_Type(Integer32):
    """Custom type hpSecPtPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpSecPtPortIndex_Type.__name__ = "Integer32"
_HpSecPtPortIndex_Object = MibTableColumn
hpSecPtPortIndex = _HpSecPtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 3, 1, 2),
    _HpSecPtPortIndex_Type()
)
hpSecPtPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSecPtPortIndex.setStatus("current")


class _HpSecPtAddressLimit_Type(Integer32):
    """Custom type hpSecPtAddressLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HpSecPtAddressLimit_Type.__name__ = "Integer32"
_HpSecPtAddressLimit_Object = MibTableColumn
hpSecPtAddressLimit = _HpSecPtAddressLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 3, 1, 3),
    _HpSecPtAddressLimit_Type()
)
hpSecPtAddressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSecPtAddressLimit.setStatus("deprecated")


class _HpSecPtLearnMode_Type(Integer32):
    """Custom type hpSecPtLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("configureSpecific", 4),
          ("learn8021xAuthorized", 5),
          ("learnContinuous", 1),
          ("learnFirstN", 2),
          ("learnFirstNConditionally", 3),
          ("learnLimitedContinuous", 6))
    )


_HpSecPtLearnMode_Type.__name__ = "Integer32"
_HpSecPtLearnMode_Object = MibTableColumn
hpSecPtLearnMode = _HpSecPtLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 3, 1, 4),
    _HpSecPtLearnMode_Type()
)
hpSecPtLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSecPtLearnMode.setStatus("current")


class _HpSecPtPreventEavesdrop_Type(Integer32):
    """Custom type hpSecPtPreventEavesdrop based on Integer32"""
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


_HpSecPtPreventEavesdrop_Type.__name__ = "Integer32"
_HpSecPtPreventEavesdrop_Object = MibTableColumn
hpSecPtPreventEavesdrop = _HpSecPtPreventEavesdrop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 3, 1, 5),
    _HpSecPtPreventEavesdrop_Type()
)
hpSecPtPreventEavesdrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSecPtPreventEavesdrop.setStatus("deprecated")


class _HpSecPtAlarmEnable_Type(Integer32):
    """Custom type hpSecPtAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("sendTrap", 2),
          ("sendTrapAndDisablePort", 3))
    )


_HpSecPtAlarmEnable_Type.__name__ = "Integer32"
_HpSecPtAlarmEnable_Object = MibTableColumn
hpSecPtAlarmEnable = _HpSecPtAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 3, 1, 6),
    _HpSecPtAlarmEnable_Type()
)
hpSecPtAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSecPtAlarmEnable.setStatus("current")


class _HpSecPtIntrusionFlag_Type(Integer32):
    """Custom type hpSecPtIntrusionFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intrusion", 1),
          ("noIntrusion", 2))
    )


_HpSecPtIntrusionFlag_Type.__name__ = "Integer32"
_HpSecPtIntrusionFlag_Object = MibTableColumn
hpSecPtIntrusionFlag = _HpSecPtIntrusionFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 3, 1, 7),
    _HpSecPtIntrusionFlag_Type()
)
hpSecPtIntrusionFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSecPtIntrusionFlag.setStatus("current")


class _HpSecPtAddressLimit2_Type(Integer32):
    """Custom type hpSecPtAddressLimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSecPtAddressLimit2_Type.__name__ = "Integer32"
_HpSecPtAddressLimit2_Object = MibTableColumn
hpSecPtAddressLimit2 = _HpSecPtAddressLimit2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 3, 1, 8),
    _HpSecPtAddressLimit2_Type()
)
hpSecPtAddressLimit2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSecPtAddressLimit2.setStatus("current")
_HpSecureCfgAddrTable_Object = MibTable
hpSecureCfgAddrTable = _HpSecureCfgAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 4)
)
if mibBuilder.loadTexts:
    hpSecureCfgAddrTable.setStatus("current")
_HpSecureCfgAddrEntry_Object = MibTableRow
hpSecureCfgAddrEntry = _HpSecureCfgAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 4, 1)
)
hpSecureCfgAddrEntry.setIndexNames(
    (0, "HP-ICF-GENERIC-RPTR", "hpSecCfgAddrGroupIndex"),
    (0, "HP-ICF-GENERIC-RPTR", "hpSecCfgAddrPortIndex"),
    (0, "HP-ICF-GENERIC-RPTR", "hpSecCfgAddress"),
)
if mibBuilder.loadTexts:
    hpSecureCfgAddrEntry.setStatus("current")


class _HpSecCfgAddrGroupIndex_Type(Integer32):
    """Custom type hpSecCfgAddrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpSecCfgAddrGroupIndex_Type.__name__ = "Integer32"
_HpSecCfgAddrGroupIndex_Object = MibTableColumn
hpSecCfgAddrGroupIndex = _HpSecCfgAddrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 4, 1, 1),
    _HpSecCfgAddrGroupIndex_Type()
)
hpSecCfgAddrGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSecCfgAddrGroupIndex.setStatus("current")


class _HpSecCfgAddrPortIndex_Type(Integer32):
    """Custom type hpSecCfgAddrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpSecCfgAddrPortIndex_Type.__name__ = "Integer32"
_HpSecCfgAddrPortIndex_Object = MibTableColumn
hpSecCfgAddrPortIndex = _HpSecCfgAddrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 4, 1, 2),
    _HpSecCfgAddrPortIndex_Type()
)
hpSecCfgAddrPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSecCfgAddrPortIndex.setStatus("current")
_HpSecCfgAddress_Type = MacAddress
_HpSecCfgAddress_Object = MibTableColumn
hpSecCfgAddress = _HpSecCfgAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 4, 1, 3),
    _HpSecCfgAddress_Type()
)
hpSecCfgAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSecCfgAddress.setStatus("current")
_HpSecCfgStatus_Type = RowStatus
_HpSecCfgStatus_Object = MibTableColumn
hpSecCfgStatus = _HpSecCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 4, 1, 4),
    _HpSecCfgStatus_Type()
)
hpSecCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSecCfgStatus.setStatus("current")
_HpSecureAuthAddrTable_Object = MibTable
hpSecureAuthAddrTable = _HpSecureAuthAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 5)
)
if mibBuilder.loadTexts:
    hpSecureAuthAddrTable.setStatus("current")
_HpSecureAuthAddrEntry_Object = MibTableRow
hpSecureAuthAddrEntry = _HpSecureAuthAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 5, 1)
)
hpSecureAuthAddrEntry.setIndexNames(
    (0, "HP-ICF-GENERIC-RPTR", "hpSecAuthAddrGroupIndex"),
    (0, "HP-ICF-GENERIC-RPTR", "hpSecAuthAddrPortIndex"),
    (0, "HP-ICF-GENERIC-RPTR", "hpSecAuthAddress"),
)
if mibBuilder.loadTexts:
    hpSecureAuthAddrEntry.setStatus("current")


class _HpSecAuthAddrGroupIndex_Type(Integer32):
    """Custom type hpSecAuthAddrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpSecAuthAddrGroupIndex_Type.__name__ = "Integer32"
_HpSecAuthAddrGroupIndex_Object = MibTableColumn
hpSecAuthAddrGroupIndex = _HpSecAuthAddrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 5, 1, 1),
    _HpSecAuthAddrGroupIndex_Type()
)
hpSecAuthAddrGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSecAuthAddrGroupIndex.setStatus("current")


class _HpSecAuthAddrPortIndex_Type(Integer32):
    """Custom type hpSecAuthAddrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpSecAuthAddrPortIndex_Type.__name__ = "Integer32"
_HpSecAuthAddrPortIndex_Object = MibTableColumn
hpSecAuthAddrPortIndex = _HpSecAuthAddrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 5, 1, 2),
    _HpSecAuthAddrPortIndex_Type()
)
hpSecAuthAddrPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSecAuthAddrPortIndex.setStatus("current")
_HpSecAuthAddress_Type = MacAddress
_HpSecAuthAddress_Object = MibTableColumn
hpSecAuthAddress = _HpSecAuthAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2, 10, 5, 1, 3),
    _HpSecAuthAddress_Type()
)
hpSecAuthAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSecAuthAddress.setStatus("current")
_HpicfGenRptrConformance_ObjectIdentity = ObjectIdentity
hpicfGenRptrConformance = _HpicfGenRptrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1)
)
_HpicfGenRptrCompliances_ObjectIdentity = ObjectIdentity
hpicfGenRptrCompliances = _HpicfGenRptrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 1)
)
_HpicfGenRptrGroups_ObjectIdentity = ObjectIdentity
hpicfGenRptrGroups = _HpicfGenRptrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2)
)
_HpGRpBasic_ObjectIdentity = ObjectIdentity
hpGRpBasic = _HpGRpBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1)
)
_HpGRpBasicGlobal_ObjectIdentity = ObjectIdentity
hpGRpBasicGlobal = _HpGRpBasicGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1, 1)
)


class _HpGRpSelfHealEnable_Type(Integer32):
    """Custom type hpGRpSelfHealEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpGRpSelfHealEnable_Type.__name__ = "Integer32"
_HpGRpSelfHealEnable_Object = MibScalar
hpGRpSelfHealEnable = _HpGRpSelfHealEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1, 1, 1),
    _HpGRpSelfHealEnable_Type()
)
hpGRpSelfHealEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpGRpSelfHealEnable.setStatus("current")
_HpGRpRepeaterTable_Object = MibTable
hpGRpRepeaterTable = _HpGRpRepeaterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpGRpRepeaterTable.setStatus("current")
_HpGRpRepeaterEntry_Object = MibTableRow
hpGRpRepeaterEntry = _HpGRpRepeaterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1, 1, 2, 1)
)
hpGRpRepeaterEntry.setIndexNames(
    (0, "HP-ICF-GENERIC-RPTR", "hpGRpRepeaterIndex"),
)
if mibBuilder.loadTexts:
    hpGRpRepeaterEntry.setStatus("current")


class _HpGRpRepeaterIndex_Type(Integer32):
    """Custom type hpGRpRepeaterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpGRpRepeaterIndex_Type.__name__ = "Integer32"
_HpGRpRepeaterIndex_Object = MibTableColumn
hpGRpRepeaterIndex = _HpGRpRepeaterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1, 1, 2, 1, 1),
    _HpGRpRepeaterIndex_Type()
)
hpGRpRepeaterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpGRpRepeaterIndex.setStatus("current")


class _HpGRpRepeaterIfIndex_Type(Integer32):
    """Custom type hpGRpRepeaterIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpGRpRepeaterIfIndex_Type.__name__ = "Integer32"
_HpGRpRepeaterIfIndex_Object = MibTableColumn
hpGRpRepeaterIfIndex = _HpGRpRepeaterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1, 1, 2, 1, 2),
    _HpGRpRepeaterIfIndex_Type()
)
hpGRpRepeaterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGRpRepeaterIfIndex.setStatus("current")


class _HpGRpRepeaterName_Type(DisplayString):
    """Custom type hpGRpRepeaterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HpGRpRepeaterName_Type.__name__ = "DisplayString"
_HpGRpRepeaterName_Object = MibTableColumn
hpGRpRepeaterName = _HpGRpRepeaterName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1, 1, 2, 1, 3),
    _HpGRpRepeaterName_Type()
)
hpGRpRepeaterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpGRpRepeaterName.setStatus("current")


class _HpGRpRepeaterVlanIndex_Type(Integer32):
    """Custom type hpGRpRepeaterVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpGRpRepeaterVlanIndex_Type.__name__ = "Integer32"
_HpGRpRepeaterVlanIndex_Object = MibTableColumn
hpGRpRepeaterVlanIndex = _HpGRpRepeaterVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 1, 1, 2, 1, 4),
    _HpGRpRepeaterVlanIndex_Type()
)
hpGRpRepeaterVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpGRpRepeaterVlanIndex.setStatus("current")
_HpicfGRpBackupLinks_ObjectIdentity = ObjectIdentity
hpicfGRpBackupLinks = _HpicfGRpBackupLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2)
)


class _HpicfBackupLinkNextIndex_Type(Integer32):
    """Custom type hpicfBackupLinkNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfBackupLinkNextIndex_Type.__name__ = "Integer32"
_HpicfBackupLinkNextIndex_Object = MibScalar
hpicfBackupLinkNextIndex = _HpicfBackupLinkNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 1),
    _HpicfBackupLinkNextIndex_Type()
)
hpicfBackupLinkNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBackupLinkNextIndex.setStatus("current")
_HpicfBackupLinkTable_Object = MibTable
hpicfBackupLinkTable = _HpicfBackupLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfBackupLinkTable.setStatus("current")
_HpicfBackupLinkEntry_Object = MibTableRow
hpicfBackupLinkEntry = _HpicfBackupLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 2, 1)
)
hpicfBackupLinkEntry.setIndexNames(
    (0, "HP-ICF-GENERIC-RPTR", "hpicfBackupLinkIndex"),
)
if mibBuilder.loadTexts:
    hpicfBackupLinkEntry.setStatus("current")


class _HpicfBackupLinkIndex_Type(Integer32):
    """Custom type hpicfBackupLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfBackupLinkIndex_Type.__name__ = "Integer32"
_HpicfBackupLinkIndex_Object = MibTableColumn
hpicfBackupLinkIndex = _HpicfBackupLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 2, 1, 1),
    _HpicfBackupLinkIndex_Type()
)
hpicfBackupLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfBackupLinkIndex.setStatus("current")


class _HpicfBackupLinkPrimaryGroup_Type(Integer32):
    """Custom type hpicfBackupLinkPrimaryGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfBackupLinkPrimaryGroup_Type.__name__ = "Integer32"
_HpicfBackupLinkPrimaryGroup_Object = MibTableColumn
hpicfBackupLinkPrimaryGroup = _HpicfBackupLinkPrimaryGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 2, 1, 2),
    _HpicfBackupLinkPrimaryGroup_Type()
)
hpicfBackupLinkPrimaryGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBackupLinkPrimaryGroup.setStatus("current")


class _HpicfBackupLinkPrimaryPort_Type(Integer32):
    """Custom type hpicfBackupLinkPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfBackupLinkPrimaryPort_Type.__name__ = "Integer32"
_HpicfBackupLinkPrimaryPort_Object = MibTableColumn
hpicfBackupLinkPrimaryPort = _HpicfBackupLinkPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 2, 1, 3),
    _HpicfBackupLinkPrimaryPort_Type()
)
hpicfBackupLinkPrimaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBackupLinkPrimaryPort.setStatus("current")


class _HpicfBackupLinkBackupGroup_Type(Integer32):
    """Custom type hpicfBackupLinkBackupGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfBackupLinkBackupGroup_Type.__name__ = "Integer32"
_HpicfBackupLinkBackupGroup_Object = MibTableColumn
hpicfBackupLinkBackupGroup = _HpicfBackupLinkBackupGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 2, 1, 4),
    _HpicfBackupLinkBackupGroup_Type()
)
hpicfBackupLinkBackupGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBackupLinkBackupGroup.setStatus("current")


class _HpicfBackupLinkBackupPort_Type(Integer32):
    """Custom type hpicfBackupLinkBackupPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfBackupLinkBackupPort_Type.__name__ = "Integer32"
_HpicfBackupLinkBackupPort_Object = MibTableColumn
hpicfBackupLinkBackupPort = _HpicfBackupLinkBackupPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 2, 1, 5),
    _HpicfBackupLinkBackupPort_Type()
)
hpicfBackupLinkBackupPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBackupLinkBackupPort.setStatus("current")
_HpicfBackupLinkAddress_Type = MacAddress
_HpicfBackupLinkAddress_Object = MibTableColumn
hpicfBackupLinkAddress = _HpicfBackupLinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 2, 1, 6),
    _HpicfBackupLinkAddress_Type()
)
hpicfBackupLinkAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBackupLinkAddress.setStatus("current")


class _HpicfBackupLinkTestTime_Type(Integer32):
    """Custom type hpicfBackupLinkTestTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpicfBackupLinkTestTime_Type.__name__ = "Integer32"
_HpicfBackupLinkTestTime_Object = MibTableColumn
hpicfBackupLinkTestTime = _HpicfBackupLinkTestTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 2, 1, 7),
    _HpicfBackupLinkTestTime_Type()
)
hpicfBackupLinkTestTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBackupLinkTestTime.setStatus("current")


class _HpicfBackupLinkConsecFailures_Type(Integer32):
    """Custom type hpicfBackupLinkConsecFailures based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfBackupLinkConsecFailures_Type.__name__ = "Integer32"
_HpicfBackupLinkConsecFailures_Object = MibTableColumn
hpicfBackupLinkConsecFailures = _HpicfBackupLinkConsecFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 2, 1, 8),
    _HpicfBackupLinkConsecFailures_Type()
)
hpicfBackupLinkConsecFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBackupLinkConsecFailures.setStatus("current")


class _HpicfBackupLinkState_Type(Integer32):
    """Custom type hpicfBackupLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 1),
          ("usingBackup", 3),
          ("usingPrimary", 2))
    )


_HpicfBackupLinkState_Type.__name__ = "Integer32"
_HpicfBackupLinkState_Object = MibTableColumn
hpicfBackupLinkState = _HpicfBackupLinkState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 2, 1, 9),
    _HpicfBackupLinkState_Type()
)
hpicfBackupLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBackupLinkState.setStatus("current")


class _HpicfBackupLinkFailEventIndex_Type(Integer32):
    """Custom type hpicfBackupLinkFailEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfBackupLinkFailEventIndex_Type.__name__ = "Integer32"
_HpicfBackupLinkFailEventIndex_Object = MibTableColumn
hpicfBackupLinkFailEventIndex = _HpicfBackupLinkFailEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 2, 1, 10),
    _HpicfBackupLinkFailEventIndex_Type()
)
hpicfBackupLinkFailEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBackupLinkFailEventIndex.setStatus("current")
_HpicfBackupLinkStatus_Type = RowStatus
_HpicfBackupLinkStatus_Object = MibTableColumn
hpicfBackupLinkStatus = _HpicfBackupLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 2, 2, 1, 11),
    _HpicfBackupLinkStatus_Type()
)
hpicfBackupLinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBackupLinkStatus.setStatus("current")
_HpGRpPortMapping_ObjectIdentity = ObjectIdentity
hpGRpPortMapping = _HpGRpPortMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3)
)
_HpGRpPMSegmentTable_Object = MibTable
hpGRpPMSegmentTable = _HpGRpPMSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 1)
)
if mibBuilder.loadTexts:
    hpGRpPMSegmentTable.setStatus("current")
_HpGRpPMSegmentEntry_Object = MibTableRow
hpGRpPMSegmentEntry = _HpGRpPMSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 1, 1)
)
hpGRpPMSegmentEntry.setIndexNames(
    (0, "HP-ICF-GENERIC-RPTR", "hpGRpPMSegmentIndex"),
)
if mibBuilder.loadTexts:
    hpGRpPMSegmentEntry.setStatus("current")


class _HpGRpPMSegmentIndex_Type(Integer32):
    """Custom type hpGRpPMSegmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpGRpPMSegmentIndex_Type.__name__ = "Integer32"
_HpGRpPMSegmentIndex_Object = MibTableColumn
hpGRpPMSegmentIndex = _HpGRpPMSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 1, 1, 1),
    _HpGRpPMSegmentIndex_Type()
)
hpGRpPMSegmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpGRpPMSegmentIndex.setStatus("current")


class _HpGRpPMCurrentRptrIndex_Type(Integer32):
    """Custom type hpGRpPMCurrentRptrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpGRpPMCurrentRptrIndex_Type.__name__ = "Integer32"
_HpGRpPMCurrentRptrIndex_Object = MibTableColumn
hpGRpPMCurrentRptrIndex = _HpGRpPMCurrentRptrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 1, 1, 3),
    _HpGRpPMCurrentRptrIndex_Type()
)
hpGRpPMCurrentRptrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpGRpPMCurrentRptrIndex.setStatus("current")
_HpGRpPMSegAllowedRptrTable_Object = MibTable
hpGRpPMSegAllowedRptrTable = _HpGRpPMSegAllowedRptrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 2)
)
if mibBuilder.loadTexts:
    hpGRpPMSegAllowedRptrTable.setStatus("current")
_HpGRpPMSegAllowedRptrEntry_Object = MibTableRow
hpGRpPMSegAllowedRptrEntry = _HpGRpPMSegAllowedRptrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 2, 1)
)
hpGRpPMSegAllowedRptrEntry.setIndexNames(
    (0, "HP-ICF-GENERIC-RPTR", "hpGRpPMSegmentIndex"),
    (0, "HP-ICF-GENERIC-RPTR", "hpGRpPMSegAllowedRptrIndex"),
)
if mibBuilder.loadTexts:
    hpGRpPMSegAllowedRptrEntry.setStatus("current")


class _HpGRpPMSegAllowedRptrIndex_Type(Integer32):
    """Custom type hpGRpPMSegAllowedRptrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpGRpPMSegAllowedRptrIndex_Type.__name__ = "Integer32"
_HpGRpPMSegAllowedRptrIndex_Object = MibTableColumn
hpGRpPMSegAllowedRptrIndex = _HpGRpPMSegAllowedRptrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 2, 1, 1),
    _HpGRpPMSegAllowedRptrIndex_Type()
)
hpGRpPMSegAllowedRptrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGRpPMSegAllowedRptrIndex.setStatus("current")
_HpGRpPMPortTable_Object = MibTable
hpGRpPMPortTable = _HpGRpPMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 3)
)
if mibBuilder.loadTexts:
    hpGRpPMPortTable.setStatus("current")
_HpGRpPMPortEntry_Object = MibTableRow
hpGRpPMPortEntry = _HpGRpPMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 3, 1)
)
hpGRpPMPortEntry.setIndexNames(
    (0, "HP-ICF-GENERIC-RPTR", "hpGRpPMPortGroupIndex"),
    (0, "HP-ICF-GENERIC-RPTR", "hpGRpPMPortIndex"),
)
if mibBuilder.loadTexts:
    hpGRpPMPortEntry.setStatus("current")


class _HpGRpPMPortGroupIndex_Type(Integer32):
    """Custom type hpGRpPMPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpGRpPMPortGroupIndex_Type.__name__ = "Integer32"
_HpGRpPMPortGroupIndex_Object = MibTableColumn
hpGRpPMPortGroupIndex = _HpGRpPMPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 3, 1, 1),
    _HpGRpPMPortGroupIndex_Type()
)
hpGRpPMPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpGRpPMPortGroupIndex.setStatus("current")


class _HpGRpPMPortIndex_Type(Integer32):
    """Custom type hpGRpPMPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpGRpPMPortIndex_Type.__name__ = "Integer32"
_HpGRpPMPortIndex_Object = MibTableColumn
hpGRpPMPortIndex = _HpGRpPMPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 3, 1, 2),
    _HpGRpPMPortIndex_Type()
)
hpGRpPMPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpGRpPMPortIndex.setStatus("current")


class _HpGRpPMPortEntPhysicalIndex_Type(Integer32):
    """Custom type hpGRpPMPortEntPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpGRpPMPortEntPhysicalIndex_Type.__name__ = "Integer32"
_HpGRpPMPortEntPhysicalIndex_Object = MibTableColumn
hpGRpPMPortEntPhysicalIndex = _HpGRpPMPortEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 3, 1, 3),
    _HpGRpPMPortEntPhysicalIndex_Type()
)
hpGRpPMPortEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGRpPMPortEntPhysicalIndex.setStatus("current")


class _HpGRpPMPortCurrentRptrIndex_Type(Integer32):
    """Custom type hpGRpPMPortCurrentRptrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpGRpPMPortCurrentRptrIndex_Type.__name__ = "Integer32"
_HpGRpPMPortCurrentRptrIndex_Object = MibTableColumn
hpGRpPMPortCurrentRptrIndex = _HpGRpPMPortCurrentRptrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 3, 1, 4),
    _HpGRpPMPortCurrentRptrIndex_Type()
)
hpGRpPMPortCurrentRptrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpGRpPMPortCurrentRptrIndex.setStatus("current")
_HpGRpPMPortAllowedRptrTable_Object = MibTable
hpGRpPMPortAllowedRptrTable = _HpGRpPMPortAllowedRptrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 4)
)
if mibBuilder.loadTexts:
    hpGRpPMPortAllowedRptrTable.setStatus("current")
_HpGRpPMPortAllowedRptrEntry_Object = MibTableRow
hpGRpPMPortAllowedRptrEntry = _HpGRpPMPortAllowedRptrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 4, 1)
)
hpGRpPMPortAllowedRptrEntry.setIndexNames(
    (0, "HP-ICF-GENERIC-RPTR", "hpGRpPMPortGroupIndex"),
    (0, "HP-ICF-GENERIC-RPTR", "hpGRpPMPortIndex"),
    (0, "HP-ICF-GENERIC-RPTR", "hpGRpPMPortAllowedRptrIndex"),
)
if mibBuilder.loadTexts:
    hpGRpPMPortAllowedRptrEntry.setStatus("current")


class _HpGRpPMPortAllowedRptrIndex_Type(Integer32):
    """Custom type hpGRpPMPortAllowedRptrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpGRpPMPortAllowedRptrIndex_Type.__name__ = "Integer32"
_HpGRpPMPortAllowedRptrIndex_Object = MibTableColumn
hpGRpPMPortAllowedRptrIndex = _HpGRpPMPortAllowedRptrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 3, 4, 1, 1),
    _HpGRpPMPortAllowedRptrIndex_Type()
)
hpGRpPMPortAllowedRptrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGRpPMPortAllowedRptrIndex.setStatus("current")
_HpGRpLoadBalancing_ObjectIdentity = ObjectIdentity
hpGRpLoadBalancing = _HpGRpLoadBalancing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 4)
)


class _HpGRpPortMapAutoConfigEnable_Type(Integer32):
    """Custom type hpGRpPortMapAutoConfigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpGRpPortMapAutoConfigEnable_Type.__name__ = "Integer32"
_HpGRpPortMapAutoConfigEnable_Object = MibScalar
hpGRpPortMapAutoConfigEnable = _HpGRpPortMapAutoConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 4, 1),
    _HpGRpPortMapAutoConfigEnable_Type()
)
hpGRpPortMapAutoConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpGRpPortMapAutoConfigEnable.setStatus("current")


class _HpGRpLoadBalanceNow_Type(Integer32):
    """Custom type hpGRpLoadBalanceNow based on Integer32"""
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
        *(("balancing", 2),
          ("cantUndo", 1),
          ("completed", 3),
          ("undoLast", 4))
    )


_HpGRpLoadBalanceNow_Type.__name__ = "Integer32"
_HpGRpLoadBalanceNow_Object = MibScalar
hpGRpLoadBalanceNow = _HpGRpLoadBalanceNow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 4, 2),
    _HpGRpLoadBalanceNow_Type()
)
hpGRpLoadBalanceNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpGRpLoadBalanceNow.setStatus("current")
_HpGRpLastLoadBalanceTime_Type = TimeStamp
_HpGRpLastLoadBalanceTime_Object = MibScalar
hpGRpLastLoadBalanceTime = _HpGRpLastLoadBalanceTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 4, 3),
    _HpGRpLastLoadBalanceTime_Type()
)
hpGRpLastLoadBalanceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpGRpLastLoadBalanceTime.setStatus("current")
_HpicfGRpSwitchConfig_ObjectIdentity = ObjectIdentity
hpicfGRpSwitchConfig = _HpicfGRpSwitchConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5)
)
_HpicfGRpSwitchTable_Object = MibTable
hpicfGRpSwitchTable = _HpicfGRpSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 1)
)
if mibBuilder.loadTexts:
    hpicfGRpSwitchTable.setStatus("current")
_HpicfGRpSwitchEntry_Object = MibTableRow
hpicfGRpSwitchEntry = _HpicfGRpSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 1, 1)
)
hpicfGRpSwitchEntry.setIndexNames(
    (0, "HP-ICF-GENERIC-RPTR", "hpicfGRpSwitchIndex"),
)
if mibBuilder.loadTexts:
    hpicfGRpSwitchEntry.setStatus("current")


class _HpicfGRpSwitchIndex_Type(Integer32):
    """Custom type hpicfGRpSwitchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_HpicfGRpSwitchIndex_Type.__name__ = "Integer32"
_HpicfGRpSwitchIndex_Object = MibTableColumn
hpicfGRpSwitchIndex = _HpicfGRpSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 1, 1, 1),
    _HpicfGRpSwitchIndex_Type()
)
hpicfGRpSwitchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGRpSwitchIndex.setStatus("current")


class _HpicfGRpSwitchType_Type(Integer32):
    """Custom type hpicfGRpSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_HpicfGRpSwitchType_Type.__name__ = "Integer32"
_HpicfGRpSwitchType_Object = MibTableColumn
hpicfGRpSwitchType = _HpicfGRpSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 1, 1, 2),
    _HpicfGRpSwitchType_Type()
)
hpicfGRpSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfGRpSwitchType.setStatus("current")


class _HpicfGRpSwitchEntPhysicalIndex_Type(Integer32):
    """Custom type hpicfGRpSwitchEntPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfGRpSwitchEntPhysicalIndex_Type.__name__ = "Integer32"
_HpicfGRpSwitchEntPhysicalIndex_Object = MibTableColumn
hpicfGRpSwitchEntPhysicalIndex = _HpicfGRpSwitchEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 1, 1, 3),
    _HpicfGRpSwitchEntPhysicalIndex_Type()
)
hpicfGRpSwitchEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfGRpSwitchEntPhysicalIndex.setStatus("current")


class _HpicfGRpSwitchLinkCount_Type(Integer32):
    """Custom type hpicfGRpSwitchLinkCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfGRpSwitchLinkCount_Type.__name__ = "Integer32"
_HpicfGRpSwitchLinkCount_Object = MibTableColumn
hpicfGRpSwitchLinkCount = _HpicfGRpSwitchLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 1, 1, 4),
    _HpicfGRpSwitchLinkCount_Type()
)
hpicfGRpSwitchLinkCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGRpSwitchLinkCount.setStatus("current")
_HpicfGRpSwitchStatus_Type = RowStatus
_HpicfGRpSwitchStatus_Object = MibTableColumn
hpicfGRpSwitchStatus = _HpicfGRpSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 1, 1, 5),
    _HpicfGRpSwitchStatus_Type()
)
hpicfGRpSwitchStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGRpSwitchStatus.setStatus("current")
_HpicfGRpSwitchLinkTable_Object = MibTable
hpicfGRpSwitchLinkTable = _HpicfGRpSwitchLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 2)
)
if mibBuilder.loadTexts:
    hpicfGRpSwitchLinkTable.setStatus("current")
_HpicfGRpSwitchLinkEntry_Object = MibTableRow
hpicfGRpSwitchLinkEntry = _HpicfGRpSwitchLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 2, 1)
)
hpicfGRpSwitchLinkEntry.setIndexNames(
    (0, "HP-ICF-GENERIC-RPTR", "hpicfGRpSwitchIndex"),
    (0, "HP-ICF-GENERIC-RPTR", "hpicfGRpSwitchLinkIndex"),
)
if mibBuilder.loadTexts:
    hpicfGRpSwitchLinkEntry.setStatus("current")


class _HpicfGRpSwitchLinkIndex_Type(Integer32):
    """Custom type hpicfGRpSwitchLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpicfGRpSwitchLinkIndex_Type.__name__ = "Integer32"
_HpicfGRpSwitchLinkIndex_Object = MibTableColumn
hpicfGRpSwitchLinkIndex = _HpicfGRpSwitchLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 2, 1, 1),
    _HpicfGRpSwitchLinkIndex_Type()
)
hpicfGRpSwitchLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGRpSwitchLinkIndex.setStatus("current")


class _HpicfGRpSwitchLinkRptrGroup_Type(Integer32):
    """Custom type hpicfGRpSwitchLinkRptrGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfGRpSwitchLinkRptrGroup_Type.__name__ = "Integer32"
_HpicfGRpSwitchLinkRptrGroup_Object = MibTableColumn
hpicfGRpSwitchLinkRptrGroup = _HpicfGRpSwitchLinkRptrGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 2, 1, 2),
    _HpicfGRpSwitchLinkRptrGroup_Type()
)
hpicfGRpSwitchLinkRptrGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfGRpSwitchLinkRptrGroup.setStatus("current")


class _HpicfGRpSwitchLinkRptrPort_Type(Integer32):
    """Custom type hpicfGRpSwitchLinkRptrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfGRpSwitchLinkRptrPort_Type.__name__ = "Integer32"
_HpicfGRpSwitchLinkRptrPort_Object = MibTableColumn
hpicfGRpSwitchLinkRptrPort = _HpicfGRpSwitchLinkRptrPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 2, 1, 3),
    _HpicfGRpSwitchLinkRptrPort_Type()
)
hpicfGRpSwitchLinkRptrPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfGRpSwitchLinkRptrPort.setStatus("current")


class _HpicfGRpSwitchLinkState_Type(Integer32):
    """Custom type hpicfGRpSwitchLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("redundant", 2))
    )


_HpicfGRpSwitchLinkState_Type.__name__ = "Integer32"
_HpicfGRpSwitchLinkState_Object = MibTableColumn
hpicfGRpSwitchLinkState = _HpicfGRpSwitchLinkState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 2, 1, 4),
    _HpicfGRpSwitchLinkState_Type()
)
hpicfGRpSwitchLinkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfGRpSwitchLinkState.setStatus("current")


class _HpicfGRpCurrentPrimarySwitch_Type(Integer32):
    """Custom type hpicfGRpCurrentPrimarySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_HpicfGRpCurrentPrimarySwitch_Type.__name__ = "Integer32"
_HpicfGRpCurrentPrimarySwitch_Object = MibScalar
hpicfGRpCurrentPrimarySwitch = _HpicfGRpCurrentPrimarySwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 3),
    _HpicfGRpCurrentPrimarySwitch_Type()
)
hpicfGRpCurrentPrimarySwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfGRpCurrentPrimarySwitch.setStatus("current")


class _HpicfGRpDesiredPrimarySwitch_Type(Integer32):
    """Custom type hpicfGRpDesiredPrimarySwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_HpicfGRpDesiredPrimarySwitch_Type.__name__ = "Integer32"
_HpicfGRpDesiredPrimarySwitch_Object = MibScalar
hpicfGRpDesiredPrimarySwitch = _HpicfGRpDesiredPrimarySwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 5, 4),
    _HpicfGRpDesiredPrimarySwitch_Type()
)
hpicfGRpDesiredPrimarySwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfGRpDesiredPrimarySwitch.setStatus("current")
_HpicfGRpBridge_ObjectIdentity = ObjectIdentity
hpicfGRpBridge = _HpicfGRpBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 6)
)


class _HpGRpBridgeAdminStatus_Type(Integer32):
    """Custom type hpGRpBridgeAdminStatus based on Integer32"""
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


_HpGRpBridgeAdminStatus_Type.__name__ = "Integer32"
_HpGRpBridgeAdminStatus_Object = MibScalar
hpGRpBridgeAdminStatus = _HpGRpBridgeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4, 6, 1),
    _HpGRpBridgeAdminStatus_Type()
)
hpGRpBridgeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpGRpBridgeAdminStatus.setStatus("current")

# Managed Objects groups

hpicfHubSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 1)
)
hpicfHubSecurityGroup.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hubSecPtGroupIndex"),
        ("HP-ICF-GENERIC-RPTR", "hubSecPtPortIndex"),
        ("HP-ICF-GENERIC-RPTR", "hubSecPtSecurityAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubSecPtAuthorizedAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubSecPtPreventEavesdrop"),
        ("HP-ICF-GENERIC-RPTR", "hubSecPtAlarmEnable"),
        ("HP-ICF-GENERIC-RPTR", "hubSecPtIntrusionFlag"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderIndex"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderGroup"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderPort"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderTime"))
)
if mibBuilder.loadTexts:
    hpicfHubSecurityGroup.setStatus("deprecated")

hpicfGenRptrBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 2)
)
hpicfGenRptrBasicGroup.setObjects(
    ("HP-ICF-GENERIC-RPTR", "hpGRpSelfHealEnable")
)
if mibBuilder.loadTexts:
    hpicfGenRptrBasicGroup.setStatus("current")

hpicfGenRptrSecPtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 3)
)
hpicfGenRptrSecPtGroup.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hubSecPtGroupIndex"),
        ("HP-ICF-GENERIC-RPTR", "hubSecPtPortIndex"),
        ("HP-ICF-GENERIC-RPTR", "hubSecPtSecurityAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubSecPtAuthorizedAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubSecPtPreventEavesdrop"),
        ("HP-ICF-GENERIC-RPTR", "hubSecPtAlarmEnable"),
        ("HP-ICF-GENERIC-RPTR", "hubSecPtIntrusionFlag"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderIndex"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderGroup"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderPort"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderTime"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderType"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderTrainingViolation"))
)
if mibBuilder.loadTexts:
    hpicfGenRptrSecPtGroup.setStatus("current")

hpicfGenRptrInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 4)
)
hpicfGenRptrInfoGroup.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hpGRpRepeaterIfIndex"),
        ("HP-ICF-GENERIC-RPTR", "hpGRpRepeaterName"),
        ("HP-ICF-GENERIC-RPTR", "hpGRpRepeaterVlanIndex"))
)
if mibBuilder.loadTexts:
    hpicfGenRptrInfoGroup.setStatus("current")

hpicfGenRptrBkpLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 5)
)
hpicfGenRptrBkpLinkGroup.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hpicfBackupLinkNextIndex"),
        ("HP-ICF-GENERIC-RPTR", "hpicfBackupLinkPrimaryGroup"),
        ("HP-ICF-GENERIC-RPTR", "hpicfBackupLinkPrimaryPort"),
        ("HP-ICF-GENERIC-RPTR", "hpicfBackupLinkBackupGroup"),
        ("HP-ICF-GENERIC-RPTR", "hpicfBackupLinkBackupPort"),
        ("HP-ICF-GENERIC-RPTR", "hpicfBackupLinkAddress"),
        ("HP-ICF-GENERIC-RPTR", "hpicfBackupLinkTestTime"),
        ("HP-ICF-GENERIC-RPTR", "hpicfBackupLinkConsecFailures"),
        ("HP-ICF-GENERIC-RPTR", "hpicfBackupLinkState"),
        ("HP-ICF-GENERIC-RPTR", "hpicfBackupLinkFailEventIndex"),
        ("HP-ICF-GENERIC-RPTR", "hpicfBackupLinkStatus"))
)
if mibBuilder.loadTexts:
    hpicfGenRptrBkpLinkGroup.setStatus("current")

hpicfGenRptrPortMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 6)
)
hpicfGenRptrPortMappingGroup.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hpGRpPMCurrentRptrIndex"),
        ("HP-ICF-GENERIC-RPTR", "hpGRpPMSegAllowedRptrIndex"),
        ("HP-ICF-GENERIC-RPTR", "hpGRpPMPortEntPhysicalIndex"),
        ("HP-ICF-GENERIC-RPTR", "hpGRpPMPortCurrentRptrIndex"),
        ("HP-ICF-GENERIC-RPTR", "hpGRpPMPortAllowedRptrIndex"),
        ("HP-ICF-GENERIC-RPTR", "hpGRpPortMapAutoConfigEnable"))
)
if mibBuilder.loadTexts:
    hpicfGenRptrPortMappingGroup.setStatus("current")

hpicfGenRptrLoadBalanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 7)
)
hpicfGenRptrLoadBalanceGroup.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hpGRpLoadBalanceNow"),
        ("HP-ICF-GENERIC-RPTR", "hpGRpLastLoadBalanceTime"))
)
if mibBuilder.loadTexts:
    hpicfGenRptrLoadBalanceGroup.setStatus("current")

hpicfGenRptrSwitchConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 8)
)
hpicfGenRptrSwitchConfigGroup.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hpicfGRpSwitchType"),
        ("HP-ICF-GENERIC-RPTR", "hpicfGRpSwitchEntPhysicalIndex"),
        ("HP-ICF-GENERIC-RPTR", "hpicfGRpSwitchLinkCount"),
        ("HP-ICF-GENERIC-RPTR", "hpicfGRpSwitchStatus"),
        ("HP-ICF-GENERIC-RPTR", "hpicfGRpSwitchLinkRptrGroup"),
        ("HP-ICF-GENERIC-RPTR", "hpicfGRpSwitchLinkRptrPort"),
        ("HP-ICF-GENERIC-RPTR", "hpicfGRpSwitchLinkState"),
        ("HP-ICF-GENERIC-RPTR", "hpicfGRpCurrentPrimarySwitch"),
        ("HP-ICF-GENERIC-RPTR", "hpicfGRpDesiredPrimarySwitch"))
)
if mibBuilder.loadTexts:
    hpicfGenRptrSwitchConfigGroup.setStatus("current")

hpicfSecPtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 11)
)
hpicfSecPtGroup.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hpSecPtAddressLimit"),
        ("HP-ICF-GENERIC-RPTR", "hpSecPtLearnMode"),
        ("HP-ICF-GENERIC-RPTR", "hpSecPtPreventEavesdrop"),
        ("HP-ICF-GENERIC-RPTR", "hpSecPtAlarmEnable"),
        ("HP-ICF-GENERIC-RPTR", "hpSecPtIntrusionFlag"),
        ("HP-ICF-GENERIC-RPTR", "hpSecCfgStatus"),
        ("HP-ICF-GENERIC-RPTR", "hpSecAuthAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderIndex"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderGroup"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderPort"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderTime"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderType"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderTrainingViolation"))
)
if mibBuilder.loadTexts:
    hpicfSecPtGroup.setStatus("deprecated")

hpicfGenRptrBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 12)
)
hpicfGenRptrBridgeGroup.setObjects(
    ("HP-ICF-GENERIC-RPTR", "hpGRpBridgeAdminStatus")
)
if mibBuilder.loadTexts:
    hpicfGenRptrBridgeGroup.setStatus("current")

hpicfSecPtGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 13)
)
hpicfSecPtGroup2.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hpSecPtAddressLimit"),
        ("HP-ICF-GENERIC-RPTR", "hpSecPtLearnMode"),
        ("HP-ICF-GENERIC-RPTR", "hpSecPtAlarmEnable"),
        ("HP-ICF-GENERIC-RPTR", "hpSecPtIntrusionFlag"),
        ("HP-ICF-GENERIC-RPTR", "hpSecCfgStatus"),
        ("HP-ICF-GENERIC-RPTR", "hpSecAuthAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderIndex"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderGroup"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderPort"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderTime"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderType"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderTrainingViolation"))
)
if mibBuilder.loadTexts:
    hpicfSecPtGroup2.setStatus("deprecated")

hpicfSecPtGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 14)
)
hpicfSecPtGroup3.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hpSecPtAddressLimit"),
        ("HP-ICF-GENERIC-RPTR", "hpSecPtLearnMode"),
        ("HP-ICF-GENERIC-RPTR", "hpSecPtAlarmEnable"),
        ("HP-ICF-GENERIC-RPTR", "hpSecPtIntrusionFlag"),
        ("HP-ICF-GENERIC-RPTR", "hpSecCfgStatus"),
        ("HP-ICF-GENERIC-RPTR", "hpSecAuthAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderIndex"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderGroup"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderPort"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderTime"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderType"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderTrainingViolation"),
        ("HP-ICF-GENERIC-RPTR", "hpSecPtAddressLimit2"))
)
if mibBuilder.loadTexts:
    hpicfSecPtGroup3.setStatus("current")


# Notification objects

hpicfIntrusionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 4, 0, 1)
)
hpicfIntrusionTrap.setObjects(
      *(("HP-ICF-GENERIC-RPTR", "hubIntruderGroup"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderPort"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderAddress"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderType"),
        ("HP-ICF-GENERIC-RPTR", "hubIntruderTrainingViolation"))
)
if mibBuilder.loadTexts:
    hpicfIntrusionTrap.setStatus(
        "current"
    )

hpicfBackupLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 4, 0, 2)
)
hpicfBackupLinkTrap.setObjects(
    ("HP-ICF-GENERIC-RPTR", "hpicfBackupLinkState")
)
if mibBuilder.loadTexts:
    hpicfBackupLinkTrap.setStatus(
        "current"
    )


# Notifications groups

hpicfGenRptrSecNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 9)
)
hpicfGenRptrSecNotifyGroup.setObjects(
    ("HP-ICF-GENERIC-RPTR", "hpicfIntrusionTrap")
)
if mibBuilder.loadTexts:
    hpicfGenRptrSecNotifyGroup.setStatus(
        "current"
    )

hpicfGenRptrBkpLinkNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 2, 10)
)
hpicfGenRptrBkpLinkNotifyGroup.setObjects(
    ("HP-ICF-GENERIC-RPTR", "hpicfBackupLinkTrap")
)
if mibBuilder.loadTexts:
    hpicfGenRptrBkpLinkNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfHubSecurityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfHubSecurityCompliance.setStatus(
        "deprecated"
    )

hpicfGenRptrBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfGenRptrBasicCompliance.setStatus(
        "deprecated"
    )

hpicfGenRptrSecurityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfGenRptrSecurityCompliance.setStatus(
        "deprecated"
    )

hpicfGenRptrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfGenRptrCompliance.setStatus(
        "deprecated"
    )

hpicfGenRptrCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfGenRptrCompliance2.setStatus(
        "current"
    )

hpicfGenRptrCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfGenRptrCompliance3.setStatus(
        "current"
    )

hpicfGenRptrMultiSecOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfGenRptrMultiSecOnlyCompliance.setStatus(
        "deprecated"
    )

hpicfGenRptrMultiSecOnlyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfGenRptrMultiSecOnlyCompliance2.setStatus(
        "deprecated"
    )

hpicfGenRptrMultiSecOnlyCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hpicfGenRptrMultiSecOnlyCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-GENERIC-RPTR",
    **{"hubSecurity": hubSecurity,
       "hubSecurePortTable": hubSecurePortTable,
       "hubSecurePortEntry": hubSecurePortEntry,
       "hubSecPtGroupIndex": hubSecPtGroupIndex,
       "hubSecPtPortIndex": hubSecPtPortIndex,
       "hubSecPtSecurityAddress": hubSecPtSecurityAddress,
       "hubSecPtAuthorizedAddress": hubSecPtAuthorizedAddress,
       "hubSecPtPreventEavesdrop": hubSecPtPreventEavesdrop,
       "hubSecPtAlarmEnable": hubSecPtAlarmEnable,
       "hubSecPtIntrusionFlag": hubSecPtIntrusionFlag,
       "hubIntruderLogTable": hubIntruderLogTable,
       "hubIntruderLogEntry": hubIntruderLogEntry,
       "hubIntruderIndex": hubIntruderIndex,
       "hubIntruderGroup": hubIntruderGroup,
       "hubIntruderPort": hubIntruderPort,
       "hubIntruderAddress": hubIntruderAddress,
       "hubIntruderTime": hubIntruderTime,
       "hubIntruderType": hubIntruderType,
       "hubIntruderTrainingViolation": hubIntruderTrainingViolation,
       "hpSecurePortTable": hpSecurePortTable,
       "hpSecurePortEntry": hpSecurePortEntry,
       "hpSecPtGroupIndex": hpSecPtGroupIndex,
       "hpSecPtPortIndex": hpSecPtPortIndex,
       "hpSecPtAddressLimit": hpSecPtAddressLimit,
       "hpSecPtLearnMode": hpSecPtLearnMode,
       "hpSecPtPreventEavesdrop": hpSecPtPreventEavesdrop,
       "hpSecPtAlarmEnable": hpSecPtAlarmEnable,
       "hpSecPtIntrusionFlag": hpSecPtIntrusionFlag,
       "hpSecPtAddressLimit2": hpSecPtAddressLimit2,
       "hpSecureCfgAddrTable": hpSecureCfgAddrTable,
       "hpSecureCfgAddrEntry": hpSecureCfgAddrEntry,
       "hpSecCfgAddrGroupIndex": hpSecCfgAddrGroupIndex,
       "hpSecCfgAddrPortIndex": hpSecCfgAddrPortIndex,
       "hpSecCfgAddress": hpSecCfgAddress,
       "hpSecCfgStatus": hpSecCfgStatus,
       "hpSecureAuthAddrTable": hpSecureAuthAddrTable,
       "hpSecureAuthAddrEntry": hpSecureAuthAddrEntry,
       "hpSecAuthAddrGroupIndex": hpSecAuthAddrGroupIndex,
       "hpSecAuthAddrPortIndex": hpSecAuthAddrPortIndex,
       "hpSecAuthAddress": hpSecAuthAddress,
       "hpicfGenRptrMib": hpicfGenRptrMib,
       "hpicfGenRptrConformance": hpicfGenRptrConformance,
       "hpicfGenRptrCompliances": hpicfGenRptrCompliances,
       "hpicfHubSecurityCompliance": hpicfHubSecurityCompliance,
       "hpicfGenRptrBasicCompliance": hpicfGenRptrBasicCompliance,
       "hpicfGenRptrSecurityCompliance": hpicfGenRptrSecurityCompliance,
       "hpicfGenRptrCompliance": hpicfGenRptrCompliance,
       "hpicfGenRptrCompliance2": hpicfGenRptrCompliance2,
       "hpicfGenRptrCompliance3": hpicfGenRptrCompliance3,
       "hpicfGenRptrMultiSecOnlyCompliance": hpicfGenRptrMultiSecOnlyCompliance,
       "hpicfGenRptrMultiSecOnlyCompliance2": hpicfGenRptrMultiSecOnlyCompliance2,
       "hpicfGenRptrMultiSecOnlyCompliance3": hpicfGenRptrMultiSecOnlyCompliance3,
       "hpicfGenRptrGroups": hpicfGenRptrGroups,
       "hpicfHubSecurityGroup": hpicfHubSecurityGroup,
       "hpicfGenRptrBasicGroup": hpicfGenRptrBasicGroup,
       "hpicfGenRptrSecPtGroup": hpicfGenRptrSecPtGroup,
       "hpicfGenRptrInfoGroup": hpicfGenRptrInfoGroup,
       "hpicfGenRptrBkpLinkGroup": hpicfGenRptrBkpLinkGroup,
       "hpicfGenRptrPortMappingGroup": hpicfGenRptrPortMappingGroup,
       "hpicfGenRptrLoadBalanceGroup": hpicfGenRptrLoadBalanceGroup,
       "hpicfGenRptrSwitchConfigGroup": hpicfGenRptrSwitchConfigGroup,
       "hpicfGenRptrSecNotifyGroup": hpicfGenRptrSecNotifyGroup,
       "hpicfGenRptrBkpLinkNotifyGroup": hpicfGenRptrBkpLinkNotifyGroup,
       "hpicfSecPtGroup": hpicfSecPtGroup,
       "hpicfGenRptrBridgeGroup": hpicfGenRptrBridgeGroup,
       "hpicfSecPtGroup2": hpicfSecPtGroup2,
       "hpicfSecPtGroup3": hpicfSecPtGroup3,
       "hpGRpBasic": hpGRpBasic,
       "hpGRpBasicGlobal": hpGRpBasicGlobal,
       "hpGRpSelfHealEnable": hpGRpSelfHealEnable,
       "hpGRpRepeaterTable": hpGRpRepeaterTable,
       "hpGRpRepeaterEntry": hpGRpRepeaterEntry,
       "hpGRpRepeaterIndex": hpGRpRepeaterIndex,
       "hpGRpRepeaterIfIndex": hpGRpRepeaterIfIndex,
       "hpGRpRepeaterName": hpGRpRepeaterName,
       "hpGRpRepeaterVlanIndex": hpGRpRepeaterVlanIndex,
       "hpicfGRpBackupLinks": hpicfGRpBackupLinks,
       "hpicfBackupLinkNextIndex": hpicfBackupLinkNextIndex,
       "hpicfBackupLinkTable": hpicfBackupLinkTable,
       "hpicfBackupLinkEntry": hpicfBackupLinkEntry,
       "hpicfBackupLinkIndex": hpicfBackupLinkIndex,
       "hpicfBackupLinkPrimaryGroup": hpicfBackupLinkPrimaryGroup,
       "hpicfBackupLinkPrimaryPort": hpicfBackupLinkPrimaryPort,
       "hpicfBackupLinkBackupGroup": hpicfBackupLinkBackupGroup,
       "hpicfBackupLinkBackupPort": hpicfBackupLinkBackupPort,
       "hpicfBackupLinkAddress": hpicfBackupLinkAddress,
       "hpicfBackupLinkTestTime": hpicfBackupLinkTestTime,
       "hpicfBackupLinkConsecFailures": hpicfBackupLinkConsecFailures,
       "hpicfBackupLinkState": hpicfBackupLinkState,
       "hpicfBackupLinkFailEventIndex": hpicfBackupLinkFailEventIndex,
       "hpicfBackupLinkStatus": hpicfBackupLinkStatus,
       "hpGRpPortMapping": hpGRpPortMapping,
       "hpGRpPMSegmentTable": hpGRpPMSegmentTable,
       "hpGRpPMSegmentEntry": hpGRpPMSegmentEntry,
       "hpGRpPMSegmentIndex": hpGRpPMSegmentIndex,
       "hpGRpPMCurrentRptrIndex": hpGRpPMCurrentRptrIndex,
       "hpGRpPMSegAllowedRptrTable": hpGRpPMSegAllowedRptrTable,
       "hpGRpPMSegAllowedRptrEntry": hpGRpPMSegAllowedRptrEntry,
       "hpGRpPMSegAllowedRptrIndex": hpGRpPMSegAllowedRptrIndex,
       "hpGRpPMPortTable": hpGRpPMPortTable,
       "hpGRpPMPortEntry": hpGRpPMPortEntry,
       "hpGRpPMPortGroupIndex": hpGRpPMPortGroupIndex,
       "hpGRpPMPortIndex": hpGRpPMPortIndex,
       "hpGRpPMPortEntPhysicalIndex": hpGRpPMPortEntPhysicalIndex,
       "hpGRpPMPortCurrentRptrIndex": hpGRpPMPortCurrentRptrIndex,
       "hpGRpPMPortAllowedRptrTable": hpGRpPMPortAllowedRptrTable,
       "hpGRpPMPortAllowedRptrEntry": hpGRpPMPortAllowedRptrEntry,
       "hpGRpPMPortAllowedRptrIndex": hpGRpPMPortAllowedRptrIndex,
       "hpGRpLoadBalancing": hpGRpLoadBalancing,
       "hpGRpPortMapAutoConfigEnable": hpGRpPortMapAutoConfigEnable,
       "hpGRpLoadBalanceNow": hpGRpLoadBalanceNow,
       "hpGRpLastLoadBalanceTime": hpGRpLastLoadBalanceTime,
       "hpicfGRpSwitchConfig": hpicfGRpSwitchConfig,
       "hpicfGRpSwitchTable": hpicfGRpSwitchTable,
       "hpicfGRpSwitchEntry": hpicfGRpSwitchEntry,
       "hpicfGRpSwitchIndex": hpicfGRpSwitchIndex,
       "hpicfGRpSwitchType": hpicfGRpSwitchType,
       "hpicfGRpSwitchEntPhysicalIndex": hpicfGRpSwitchEntPhysicalIndex,
       "hpicfGRpSwitchLinkCount": hpicfGRpSwitchLinkCount,
       "hpicfGRpSwitchStatus": hpicfGRpSwitchStatus,
       "hpicfGRpSwitchLinkTable": hpicfGRpSwitchLinkTable,
       "hpicfGRpSwitchLinkEntry": hpicfGRpSwitchLinkEntry,
       "hpicfGRpSwitchLinkIndex": hpicfGRpSwitchLinkIndex,
       "hpicfGRpSwitchLinkRptrGroup": hpicfGRpSwitchLinkRptrGroup,
       "hpicfGRpSwitchLinkRptrPort": hpicfGRpSwitchLinkRptrPort,
       "hpicfGRpSwitchLinkState": hpicfGRpSwitchLinkState,
       "hpicfGRpCurrentPrimarySwitch": hpicfGRpCurrentPrimarySwitch,
       "hpicfGRpDesiredPrimarySwitch": hpicfGRpDesiredPrimarySwitch,
       "hpicfGRpBridge": hpicfGRpBridge,
       "hpGRpBridgeAdminStatus": hpGRpBridgeAdminStatus,
       "hpicfIntrusionTrap": hpicfIntrusionTrap,
       "hpicfBackupLinkTrap": hpicfBackupLinkTrap}
)
