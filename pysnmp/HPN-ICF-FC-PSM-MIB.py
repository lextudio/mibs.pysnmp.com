# SNMP MIB module (HPN-ICF-FC-PSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-FC-PSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:18 2024
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

(HpnicfFcNameIdOrZero,) = mibBuilder.importSymbols(
    "HPN-ICF-FC-TC-MIB",
    "HpnicfFcNameIdOrZero")

(hpnicfSan,) = mibBuilder.importSymbols(
    "HPN-ICF-VSAN-MIB",
    "hpnicfSan")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifDescr) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifDescr")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hpnicfFcPsm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8)
)
hpnicfFcPsm.setRevisions(
        ("2013-10-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfFcPsmPortBindDevType(Integer32, TextualConvention):
    status = "current"
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
        *(("nWWN", 1),
          ("pWWN", 2),
          ("sWWN", 3),
          ("wildCard", 4))
    )



class HpnicfFcPsmClearEntryType(Integer32, TextualConvention):
    status = "current"
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
        *(("clearAll", 3),
          ("clearAutoLearn", 2),
          ("clearStatic", 1),
          ("noop", 4))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfFcPsmNotifications_ObjectIdentity = ObjectIdentity
hpnicfFcPsmNotifications = _HpnicfFcPsmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 0)
)
_HpnicfFcPsmObjects_ObjectIdentity = ObjectIdentity
hpnicfFcPsmObjects = _HpnicfFcPsmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1)
)
_HpnicfFcPsmScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfFcPsmScalarObjects = _HpnicfFcPsmScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 1)
)


class _HpnicfFcPsmNotifyEnable_Type(TruthValue):
    """Custom type hpnicfFcPsmNotifyEnable based on TruthValue"""


_HpnicfFcPsmNotifyEnable_Object = MibScalar
hpnicfFcPsmNotifyEnable = _HpnicfFcPsmNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 1, 1),
    _HpnicfFcPsmNotifyEnable_Type()
)
hpnicfFcPsmNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcPsmNotifyEnable.setStatus("current")
_HpnicfFcPsmConfiguration_ObjectIdentity = ObjectIdentity
hpnicfFcPsmConfiguration = _HpnicfFcPsmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2)
)
_HpnicfFcPsmEnableTable_Object = MibTable
hpnicfFcPsmEnableTable = _HpnicfFcPsmEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfFcPsmEnableTable.setStatus("current")
_HpnicfFcPsmEnableEntry_Object = MibTableRow
hpnicfFcPsmEnableEntry = _HpnicfFcPsmEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 1, 1)
)
hpnicfFcPsmEnableEntry.setIndexNames(
    (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcPsmEnableEntry.setStatus("current")


class _HpnicfFcPsmEnableVsanIndex_Type(Unsigned32):
    """Custom type hpnicfFcPsmEnableVsanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_HpnicfFcPsmEnableVsanIndex_Type.__name__ = "Unsigned32"
_HpnicfFcPsmEnableVsanIndex_Object = MibTableColumn
hpnicfFcPsmEnableVsanIndex = _HpnicfFcPsmEnableVsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 1, 1, 1),
    _HpnicfFcPsmEnableVsanIndex_Type()
)
hpnicfFcPsmEnableVsanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFcPsmEnableVsanIndex.setStatus("current")


class _HpnicfFcPsmEnable_Type(Integer32):
    """Custom type hpnicfFcPsmEnable based on Integer32"""
    defaultValue = 4

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
        *(("disable", 3),
          ("enable", 1),
          ("enableWithAutoLearn", 2),
          ("noop", 4))
    )


_HpnicfFcPsmEnable_Type.__name__ = "Integer32"
_HpnicfFcPsmEnable_Object = MibTableColumn
hpnicfFcPsmEnable = _HpnicfFcPsmEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 1, 1, 2),
    _HpnicfFcPsmEnable_Type()
)
hpnicfFcPsmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcPsmEnable.setStatus("current")


class _HpnicfFcPsmEnableState_Type(TruthValue):
    """Custom type hpnicfFcPsmEnableState based on TruthValue"""


_HpnicfFcPsmEnableState_Object = MibTableColumn
hpnicfFcPsmEnableState = _HpnicfFcPsmEnableState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 1, 1, 3),
    _HpnicfFcPsmEnableState_Type()
)
hpnicfFcPsmEnableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPsmEnableState.setStatus("current")
_HpnicfFcPsmConfigTable_Object = MibTable
hpnicfFcPsmConfigTable = _HpnicfFcPsmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfFcPsmConfigTable.setStatus("current")
_HpnicfFcPsmConfigEntry_Object = MibTableRow
hpnicfFcPsmConfigEntry = _HpnicfFcPsmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2, 1)
)
hpnicfFcPsmConfigEntry.setIndexNames(
    (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"),
    (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcPsmConfigEntry.setStatus("current")


class _HpnicfFcPsmIndex_Type(Unsigned32):
    """Custom type hpnicfFcPsmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_HpnicfFcPsmIndex_Type.__name__ = "Unsigned32"
_HpnicfFcPsmIndex_Object = MibTableColumn
hpnicfFcPsmIndex = _HpnicfFcPsmIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2, 1, 1),
    _HpnicfFcPsmIndex_Type()
)
hpnicfFcPsmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFcPsmIndex.setStatus("current")
_HpnicfFcPsmLoginDevType_Type = HpnicfFcPsmPortBindDevType
_HpnicfFcPsmLoginDevType_Object = MibTableColumn
hpnicfFcPsmLoginDevType = _HpnicfFcPsmLoginDevType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2, 1, 2),
    _HpnicfFcPsmLoginDevType_Type()
)
hpnicfFcPsmLoginDevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcPsmLoginDevType.setStatus("current")
_HpnicfFcPsmLoginDev_Type = HpnicfFcNameIdOrZero
_HpnicfFcPsmLoginDev_Object = MibTableColumn
hpnicfFcPsmLoginDev = _HpnicfFcPsmLoginDev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2, 1, 3),
    _HpnicfFcPsmLoginDev_Type()
)
hpnicfFcPsmLoginDev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcPsmLoginDev.setStatus("current")
_HpnicfFcPsmLoginPoint_Type = InterfaceIndexOrZero
_HpnicfFcPsmLoginPoint_Object = MibTableColumn
hpnicfFcPsmLoginPoint = _HpnicfFcPsmLoginPoint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2, 1, 4),
    _HpnicfFcPsmLoginPoint_Type()
)
hpnicfFcPsmLoginPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcPsmLoginPoint.setStatus("current")
_HpnicfFcPsmRowStatus_Type = RowStatus
_HpnicfFcPsmRowStatus_Object = MibTableColumn
hpnicfFcPsmRowStatus = _HpnicfFcPsmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 2, 1, 5),
    _HpnicfFcPsmRowStatus_Type()
)
hpnicfFcPsmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFcPsmRowStatus.setStatus("current")
_HpnicfFcPsmEnfTable_Object = MibTable
hpnicfFcPsmEnfTable = _HpnicfFcPsmEnfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfFcPsmEnfTable.setStatus("current")
_HpnicfFcPsmEnfEntry_Object = MibTableRow
hpnicfFcPsmEnfEntry = _HpnicfFcPsmEnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3, 1)
)
hpnicfFcPsmEnfEntry.setIndexNames(
    (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"),
    (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcPsmEnfEntry.setStatus("current")


class _HpnicfFcPsmEnfIndex_Type(Unsigned32):
    """Custom type hpnicfFcPsmEnfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_HpnicfFcPsmEnfIndex_Type.__name__ = "Unsigned32"
_HpnicfFcPsmEnfIndex_Object = MibTableColumn
hpnicfFcPsmEnfIndex = _HpnicfFcPsmEnfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3, 1, 1),
    _HpnicfFcPsmEnfIndex_Type()
)
hpnicfFcPsmEnfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFcPsmEnfIndex.setStatus("current")
_HpnicfFcPsmEnfLoginDevType_Type = HpnicfFcPsmPortBindDevType
_HpnicfFcPsmEnfLoginDevType_Object = MibTableColumn
hpnicfFcPsmEnfLoginDevType = _HpnicfFcPsmEnfLoginDevType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3, 1, 2),
    _HpnicfFcPsmEnfLoginDevType_Type()
)
hpnicfFcPsmEnfLoginDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPsmEnfLoginDevType.setStatus("current")
_HpnicfFcPsmEnfLoginDev_Type = HpnicfFcNameIdOrZero
_HpnicfFcPsmEnfLoginDev_Object = MibTableColumn
hpnicfFcPsmEnfLoginDev = _HpnicfFcPsmEnfLoginDev_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3, 1, 3),
    _HpnicfFcPsmEnfLoginDev_Type()
)
hpnicfFcPsmEnfLoginDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPsmEnfLoginDev.setStatus("current")
_HpnicfFcPsmEnfLoginPoint_Type = InterfaceIndexOrZero
_HpnicfFcPsmEnfLoginPoint_Object = MibTableColumn
hpnicfFcPsmEnfLoginPoint = _HpnicfFcPsmEnfLoginPoint_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3, 1, 4),
    _HpnicfFcPsmEnfLoginPoint_Type()
)
hpnicfFcPsmEnfLoginPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPsmEnfLoginPoint.setStatus("current")


class _HpnicfFcPsmEnfEntryType_Type(Integer32):
    """Custom type hpnicfFcPsmEnfEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("learning", 1),
          ("learnt", 2),
          ("static", 3))
    )


_HpnicfFcPsmEnfEntryType_Type.__name__ = "Integer32"
_HpnicfFcPsmEnfEntryType_Object = MibTableColumn
hpnicfFcPsmEnfEntryType = _HpnicfFcPsmEnfEntryType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 3, 1, 5),
    _HpnicfFcPsmEnfEntryType_Type()
)
hpnicfFcPsmEnfEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPsmEnfEntryType.setStatus("current")
_HpnicfFcPsmCopyToConfigTable_Object = MibTable
hpnicfFcPsmCopyToConfigTable = _HpnicfFcPsmCopyToConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfFcPsmCopyToConfigTable.setStatus("current")
_HpnicfFcPsmCopyToConfigEntry_Object = MibTableRow
hpnicfFcPsmCopyToConfigEntry = _HpnicfFcPsmCopyToConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 4, 1)
)
hpnicfFcPsmCopyToConfigEntry.setIndexNames(
    (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcPsmCopyToConfigEntry.setStatus("current")


class _HpnicfFcPsmCopyToConfig_Type(Integer32):
    """Custom type hpnicfFcPsmCopyToConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copy", 1),
          ("noop", 2))
    )


_HpnicfFcPsmCopyToConfig_Type.__name__ = "Integer32"
_HpnicfFcPsmCopyToConfig_Object = MibTableColumn
hpnicfFcPsmCopyToConfig = _HpnicfFcPsmCopyToConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 4, 1, 1),
    _HpnicfFcPsmCopyToConfig_Type()
)
hpnicfFcPsmCopyToConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcPsmCopyToConfig.setStatus("current")
_HpnicfFcPsmAutoLearnTable_Object = MibTable
hpnicfFcPsmAutoLearnTable = _HpnicfFcPsmAutoLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfFcPsmAutoLearnTable.setStatus("current")
_HpnicfFcPsmAutoLearnEntry_Object = MibTableRow
hpnicfFcPsmAutoLearnEntry = _HpnicfFcPsmAutoLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 5, 1)
)
hpnicfFcPsmAutoLearnEntry.setIndexNames(
    (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcPsmAutoLearnEntry.setStatus("current")


class _HpnicfFcPsmAutoLearnEnable_Type(TruthValue):
    """Custom type hpnicfFcPsmAutoLearnEnable based on TruthValue"""


_HpnicfFcPsmAutoLearnEnable_Object = MibTableColumn
hpnicfFcPsmAutoLearnEnable = _HpnicfFcPsmAutoLearnEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 5, 1, 1),
    _HpnicfFcPsmAutoLearnEnable_Type()
)
hpnicfFcPsmAutoLearnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcPsmAutoLearnEnable.setStatus("current")
_HpnicfFcPsmClearTable_Object = MibTable
hpnicfFcPsmClearTable = _HpnicfFcPsmClearTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfFcPsmClearTable.setStatus("current")
_HpnicfFcPsmClearEntry_Object = MibTableRow
hpnicfFcPsmClearEntry = _HpnicfFcPsmClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 6, 1)
)
hpnicfFcPsmClearEntry.setIndexNames(
    (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcPsmClearEntry.setStatus("current")


class _HpnicfFcPsmClearType_Type(HpnicfFcPsmClearEntryType):
    """Custom type hpnicfFcPsmClearType based on HpnicfFcPsmClearEntryType"""


_HpnicfFcPsmClearType_Object = MibTableColumn
hpnicfFcPsmClearType = _HpnicfFcPsmClearType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 6, 1, 1),
    _HpnicfFcPsmClearType_Type()
)
hpnicfFcPsmClearType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcPsmClearType.setStatus("current")
_HpnicfFcPsmClearIntf_Type = InterfaceIndexOrZero
_HpnicfFcPsmClearIntf_Object = MibTableColumn
hpnicfFcPsmClearIntf = _HpnicfFcPsmClearIntf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 2, 6, 1, 2),
    _HpnicfFcPsmClearIntf_Type()
)
hpnicfFcPsmClearIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcPsmClearIntf.setStatus("current")
_HpnicfFcPsmStats_ObjectIdentity = ObjectIdentity
hpnicfFcPsmStats = _HpnicfFcPsmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3)
)
_HpnicfFcPsmStatsTable_Object = MibTable
hpnicfFcPsmStatsTable = _HpnicfFcPsmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfFcPsmStatsTable.setStatus("current")
_HpnicfFcPsmStatsEntry_Object = MibTableRow
hpnicfFcPsmStatsEntry = _HpnicfFcPsmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 1, 1)
)
hpnicfFcPsmStatsEntry.setIndexNames(
    (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcPsmStatsEntry.setStatus("current")
_HpnicfFcPsmAllowedLogins_Type = Counter32
_HpnicfFcPsmAllowedLogins_Object = MibTableColumn
hpnicfFcPsmAllowedLogins = _HpnicfFcPsmAllowedLogins_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 1, 1, 1),
    _HpnicfFcPsmAllowedLogins_Type()
)
hpnicfFcPsmAllowedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPsmAllowedLogins.setStatus("current")
_HpnicfFcPsmDeniedLogins_Type = Counter32
_HpnicfFcPsmDeniedLogins_Object = MibTableColumn
hpnicfFcPsmDeniedLogins = _HpnicfFcPsmDeniedLogins_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 1, 1, 2),
    _HpnicfFcPsmDeniedLogins_Type()
)
hpnicfFcPsmDeniedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPsmDeniedLogins.setStatus("current")


class _HpnicfFcPsmStatsClear_Type(Integer32):
    """Custom type hpnicfFcPsmStatsClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noop", 2))
    )


_HpnicfFcPsmStatsClear_Type.__name__ = "Integer32"
_HpnicfFcPsmStatsClear_Object = MibTableColumn
hpnicfFcPsmStatsClear = _HpnicfFcPsmStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 1, 1, 3),
    _HpnicfFcPsmStatsClear_Type()
)
hpnicfFcPsmStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFcPsmStatsClear.setStatus("current")
_HpnicfFcPsmViolationTable_Object = MibTable
hpnicfFcPsmViolationTable = _HpnicfFcPsmViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfFcPsmViolationTable.setStatus("current")
_HpnicfFcPsmViolationEntry_Object = MibTableRow
hpnicfFcPsmViolationEntry = _HpnicfFcPsmViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1)
)
hpnicfFcPsmViolationEntry.setIndexNames(
    (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmEnableVsanIndex"),
    (0, "HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmViolationIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFcPsmViolationEntry.setStatus("current")


class _HpnicfFcPsmViolationIndex_Type(Unsigned32):
    """Custom type hpnicfFcPsmViolationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfFcPsmViolationIndex_Type.__name__ = "Unsigned32"
_HpnicfFcPsmViolationIndex_Object = MibTableColumn
hpnicfFcPsmViolationIndex = _HpnicfFcPsmViolationIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 1),
    _HpnicfFcPsmViolationIndex_Type()
)
hpnicfFcPsmViolationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFcPsmViolationIndex.setStatus("current")
_HpnicfFcPsmLoginPWWN_Type = HpnicfFcNameIdOrZero
_HpnicfFcPsmLoginPWWN_Object = MibTableColumn
hpnicfFcPsmLoginPWWN = _HpnicfFcPsmLoginPWWN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 2),
    _HpnicfFcPsmLoginPWWN_Type()
)
hpnicfFcPsmLoginPWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPsmLoginPWWN.setStatus("current")
_HpnicfFcPsmLoginNWWN_Type = HpnicfFcNameIdOrZero
_HpnicfFcPsmLoginNWWN_Object = MibTableColumn
hpnicfFcPsmLoginNWWN = _HpnicfFcPsmLoginNWWN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 3),
    _HpnicfFcPsmLoginNWWN_Type()
)
hpnicfFcPsmLoginNWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPsmLoginNWWN.setStatus("current")
_HpnicfFcPsmLoginSWWN_Type = HpnicfFcNameIdOrZero
_HpnicfFcPsmLoginSWWN_Object = MibTableColumn
hpnicfFcPsmLoginSWWN = _HpnicfFcPsmLoginSWWN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 4),
    _HpnicfFcPsmLoginSWWN_Type()
)
hpnicfFcPsmLoginSWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPsmLoginSWWN.setStatus("current")
_HpnicfFcPsmLoginIntf_Type = InterfaceIndex
_HpnicfFcPsmLoginIntf_Object = MibTableColumn
hpnicfFcPsmLoginIntf = _HpnicfFcPsmLoginIntf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 5),
    _HpnicfFcPsmLoginIntf_Type()
)
hpnicfFcPsmLoginIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPsmLoginIntf.setStatus("current")
_HpnicfFcPsmLoginTime_Type = TimeStamp
_HpnicfFcPsmLoginTime_Object = MibTableColumn
hpnicfFcPsmLoginTime = _HpnicfFcPsmLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 6),
    _HpnicfFcPsmLoginTime_Type()
)
hpnicfFcPsmLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPsmLoginTime.setStatus("current")
_HpnicfFcPsmLoginCount_Type = Counter32
_HpnicfFcPsmLoginCount_Object = MibTableColumn
hpnicfFcPsmLoginCount = _HpnicfFcPsmLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 1, 3, 2, 1, 7),
    _HpnicfFcPsmLoginCount_Type()
)
hpnicfFcPsmLoginCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFcPsmLoginCount.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfFcPsmFPortDenyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 0, 1)
)
hpnicfFcPsmFPortDenyNotify.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmLoginPWWN"),
        ("HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmLoginIntf"),
        ("HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmLoginTime"))
)
if mibBuilder.loadTexts:
    hpnicfFcPsmFPortDenyNotify.setStatus(
        "current"
    )

hpnicfFcPsmEPortDenyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 8, 0, 2)
)
hpnicfFcPsmEPortDenyNotify.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmLoginSWWN"),
        ("HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmLoginIntf"),
        ("HPN-ICF-FC-PSM-MIB", "hpnicfFcPsmLoginTime"))
)
if mibBuilder.loadTexts:
    hpnicfFcPsmEPortDenyNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-FC-PSM-MIB",
    **{"HpnicfFcPsmPortBindDevType": HpnicfFcPsmPortBindDevType,
       "HpnicfFcPsmClearEntryType": HpnicfFcPsmClearEntryType,
       "hpnicfFcPsm": hpnicfFcPsm,
       "hpnicfFcPsmNotifications": hpnicfFcPsmNotifications,
       "hpnicfFcPsmFPortDenyNotify": hpnicfFcPsmFPortDenyNotify,
       "hpnicfFcPsmEPortDenyNotify": hpnicfFcPsmEPortDenyNotify,
       "hpnicfFcPsmObjects": hpnicfFcPsmObjects,
       "hpnicfFcPsmScalarObjects": hpnicfFcPsmScalarObjects,
       "hpnicfFcPsmNotifyEnable": hpnicfFcPsmNotifyEnable,
       "hpnicfFcPsmConfiguration": hpnicfFcPsmConfiguration,
       "hpnicfFcPsmEnableTable": hpnicfFcPsmEnableTable,
       "hpnicfFcPsmEnableEntry": hpnicfFcPsmEnableEntry,
       "hpnicfFcPsmEnableVsanIndex": hpnicfFcPsmEnableVsanIndex,
       "hpnicfFcPsmEnable": hpnicfFcPsmEnable,
       "hpnicfFcPsmEnableState": hpnicfFcPsmEnableState,
       "hpnicfFcPsmConfigTable": hpnicfFcPsmConfigTable,
       "hpnicfFcPsmConfigEntry": hpnicfFcPsmConfigEntry,
       "hpnicfFcPsmIndex": hpnicfFcPsmIndex,
       "hpnicfFcPsmLoginDevType": hpnicfFcPsmLoginDevType,
       "hpnicfFcPsmLoginDev": hpnicfFcPsmLoginDev,
       "hpnicfFcPsmLoginPoint": hpnicfFcPsmLoginPoint,
       "hpnicfFcPsmRowStatus": hpnicfFcPsmRowStatus,
       "hpnicfFcPsmEnfTable": hpnicfFcPsmEnfTable,
       "hpnicfFcPsmEnfEntry": hpnicfFcPsmEnfEntry,
       "hpnicfFcPsmEnfIndex": hpnicfFcPsmEnfIndex,
       "hpnicfFcPsmEnfLoginDevType": hpnicfFcPsmEnfLoginDevType,
       "hpnicfFcPsmEnfLoginDev": hpnicfFcPsmEnfLoginDev,
       "hpnicfFcPsmEnfLoginPoint": hpnicfFcPsmEnfLoginPoint,
       "hpnicfFcPsmEnfEntryType": hpnicfFcPsmEnfEntryType,
       "hpnicfFcPsmCopyToConfigTable": hpnicfFcPsmCopyToConfigTable,
       "hpnicfFcPsmCopyToConfigEntry": hpnicfFcPsmCopyToConfigEntry,
       "hpnicfFcPsmCopyToConfig": hpnicfFcPsmCopyToConfig,
       "hpnicfFcPsmAutoLearnTable": hpnicfFcPsmAutoLearnTable,
       "hpnicfFcPsmAutoLearnEntry": hpnicfFcPsmAutoLearnEntry,
       "hpnicfFcPsmAutoLearnEnable": hpnicfFcPsmAutoLearnEnable,
       "hpnicfFcPsmClearTable": hpnicfFcPsmClearTable,
       "hpnicfFcPsmClearEntry": hpnicfFcPsmClearEntry,
       "hpnicfFcPsmClearType": hpnicfFcPsmClearType,
       "hpnicfFcPsmClearIntf": hpnicfFcPsmClearIntf,
       "hpnicfFcPsmStats": hpnicfFcPsmStats,
       "hpnicfFcPsmStatsTable": hpnicfFcPsmStatsTable,
       "hpnicfFcPsmStatsEntry": hpnicfFcPsmStatsEntry,
       "hpnicfFcPsmAllowedLogins": hpnicfFcPsmAllowedLogins,
       "hpnicfFcPsmDeniedLogins": hpnicfFcPsmDeniedLogins,
       "hpnicfFcPsmStatsClear": hpnicfFcPsmStatsClear,
       "hpnicfFcPsmViolationTable": hpnicfFcPsmViolationTable,
       "hpnicfFcPsmViolationEntry": hpnicfFcPsmViolationEntry,
       "hpnicfFcPsmViolationIndex": hpnicfFcPsmViolationIndex,
       "hpnicfFcPsmLoginPWWN": hpnicfFcPsmLoginPWWN,
       "hpnicfFcPsmLoginNWWN": hpnicfFcPsmLoginNWWN,
       "hpnicfFcPsmLoginSWWN": hpnicfFcPsmLoginSWWN,
       "hpnicfFcPsmLoginIntf": hpnicfFcPsmLoginIntf,
       "hpnicfFcPsmLoginTime": hpnicfFcPsmLoginTime,
       "hpnicfFcPsmLoginCount": hpnicfFcPsmLoginCount}
)
