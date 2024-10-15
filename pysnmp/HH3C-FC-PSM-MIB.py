# SNMP MIB module (HH3C-FC-PSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-FC-PSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:18 2024
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

(Hh3cFcNameIdOrZero,) = mibBuilder.importSymbols(
    "HH3C-FC-TC-MIB",
    "Hh3cFcNameIdOrZero")

(hh3cSan,) = mibBuilder.importSymbols(
    "HH3C-VSAN-MIB",
    "hh3cSan")

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

hh3cFcPsm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8)
)
hh3cFcPsm.setRevisions(
        ("2013-10-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cFcPsmPortBindDevType(Integer32, TextualConvention):
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



class Hh3cFcPsmClearEntryType(Integer32, TextualConvention):
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

_Hh3cFcPsmNotifications_ObjectIdentity = ObjectIdentity
hh3cFcPsmNotifications = _Hh3cFcPsmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 0)
)
_Hh3cFcPsmObjects_ObjectIdentity = ObjectIdentity
hh3cFcPsmObjects = _Hh3cFcPsmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1)
)
_Hh3cFcPsmScalarObjects_ObjectIdentity = ObjectIdentity
hh3cFcPsmScalarObjects = _Hh3cFcPsmScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 1)
)


class _Hh3cFcPsmNotifyEnable_Type(TruthValue):
    """Custom type hh3cFcPsmNotifyEnable based on TruthValue"""


_Hh3cFcPsmNotifyEnable_Object = MibScalar
hh3cFcPsmNotifyEnable = _Hh3cFcPsmNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 1, 1),
    _Hh3cFcPsmNotifyEnable_Type()
)
hh3cFcPsmNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcPsmNotifyEnable.setStatus("current")
_Hh3cFcPsmConfiguration_ObjectIdentity = ObjectIdentity
hh3cFcPsmConfiguration = _Hh3cFcPsmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2)
)
_Hh3cFcPsmEnableTable_Object = MibTable
hh3cFcPsmEnableTable = _Hh3cFcPsmEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cFcPsmEnableTable.setStatus("current")
_Hh3cFcPsmEnableEntry_Object = MibTableRow
hh3cFcPsmEnableEntry = _Hh3cFcPsmEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 1, 1)
)
hh3cFcPsmEnableEntry.setIndexNames(
    (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcPsmEnableEntry.setStatus("current")


class _Hh3cFcPsmEnableVsanIndex_Type(Unsigned32):
    """Custom type hh3cFcPsmEnableVsanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_Hh3cFcPsmEnableVsanIndex_Type.__name__ = "Unsigned32"
_Hh3cFcPsmEnableVsanIndex_Object = MibTableColumn
hh3cFcPsmEnableVsanIndex = _Hh3cFcPsmEnableVsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 1, 1, 1),
    _Hh3cFcPsmEnableVsanIndex_Type()
)
hh3cFcPsmEnableVsanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFcPsmEnableVsanIndex.setStatus("current")


class _Hh3cFcPsmEnable_Type(Integer32):
    """Custom type hh3cFcPsmEnable based on Integer32"""
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


_Hh3cFcPsmEnable_Type.__name__ = "Integer32"
_Hh3cFcPsmEnable_Object = MibTableColumn
hh3cFcPsmEnable = _Hh3cFcPsmEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 1, 1, 2),
    _Hh3cFcPsmEnable_Type()
)
hh3cFcPsmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcPsmEnable.setStatus("current")


class _Hh3cFcPsmEnableState_Type(TruthValue):
    """Custom type hh3cFcPsmEnableState based on TruthValue"""


_Hh3cFcPsmEnableState_Object = MibTableColumn
hh3cFcPsmEnableState = _Hh3cFcPsmEnableState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 1, 1, 3),
    _Hh3cFcPsmEnableState_Type()
)
hh3cFcPsmEnableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPsmEnableState.setStatus("current")
_Hh3cFcPsmConfigTable_Object = MibTable
hh3cFcPsmConfigTable = _Hh3cFcPsmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cFcPsmConfigTable.setStatus("current")
_Hh3cFcPsmConfigEntry_Object = MibTableRow
hh3cFcPsmConfigEntry = _Hh3cFcPsmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2, 1)
)
hh3cFcPsmConfigEntry.setIndexNames(
    (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"),
    (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcPsmConfigEntry.setStatus("current")


class _Hh3cFcPsmIndex_Type(Unsigned32):
    """Custom type hh3cFcPsmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_Hh3cFcPsmIndex_Type.__name__ = "Unsigned32"
_Hh3cFcPsmIndex_Object = MibTableColumn
hh3cFcPsmIndex = _Hh3cFcPsmIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2, 1, 1),
    _Hh3cFcPsmIndex_Type()
)
hh3cFcPsmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFcPsmIndex.setStatus("current")
_Hh3cFcPsmLoginDevType_Type = Hh3cFcPsmPortBindDevType
_Hh3cFcPsmLoginDevType_Object = MibTableColumn
hh3cFcPsmLoginDevType = _Hh3cFcPsmLoginDevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2, 1, 2),
    _Hh3cFcPsmLoginDevType_Type()
)
hh3cFcPsmLoginDevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcPsmLoginDevType.setStatus("current")
_Hh3cFcPsmLoginDev_Type = Hh3cFcNameIdOrZero
_Hh3cFcPsmLoginDev_Object = MibTableColumn
hh3cFcPsmLoginDev = _Hh3cFcPsmLoginDev_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2, 1, 3),
    _Hh3cFcPsmLoginDev_Type()
)
hh3cFcPsmLoginDev.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcPsmLoginDev.setStatus("current")
_Hh3cFcPsmLoginPoint_Type = InterfaceIndexOrZero
_Hh3cFcPsmLoginPoint_Object = MibTableColumn
hh3cFcPsmLoginPoint = _Hh3cFcPsmLoginPoint_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2, 1, 4),
    _Hh3cFcPsmLoginPoint_Type()
)
hh3cFcPsmLoginPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcPsmLoginPoint.setStatus("current")
_Hh3cFcPsmRowStatus_Type = RowStatus
_Hh3cFcPsmRowStatus_Object = MibTableColumn
hh3cFcPsmRowStatus = _Hh3cFcPsmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 2, 1, 5),
    _Hh3cFcPsmRowStatus_Type()
)
hh3cFcPsmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFcPsmRowStatus.setStatus("current")
_Hh3cFcPsmEnfTable_Object = MibTable
hh3cFcPsmEnfTable = _Hh3cFcPsmEnfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cFcPsmEnfTable.setStatus("current")
_Hh3cFcPsmEnfEntry_Object = MibTableRow
hh3cFcPsmEnfEntry = _Hh3cFcPsmEnfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3, 1)
)
hh3cFcPsmEnfEntry.setIndexNames(
    (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"),
    (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnfIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcPsmEnfEntry.setStatus("current")


class _Hh3cFcPsmEnfIndex_Type(Unsigned32):
    """Custom type hh3cFcPsmEnfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_Hh3cFcPsmEnfIndex_Type.__name__ = "Unsigned32"
_Hh3cFcPsmEnfIndex_Object = MibTableColumn
hh3cFcPsmEnfIndex = _Hh3cFcPsmEnfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3, 1, 1),
    _Hh3cFcPsmEnfIndex_Type()
)
hh3cFcPsmEnfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFcPsmEnfIndex.setStatus("current")
_Hh3cFcPsmEnfLoginDevType_Type = Hh3cFcPsmPortBindDevType
_Hh3cFcPsmEnfLoginDevType_Object = MibTableColumn
hh3cFcPsmEnfLoginDevType = _Hh3cFcPsmEnfLoginDevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3, 1, 2),
    _Hh3cFcPsmEnfLoginDevType_Type()
)
hh3cFcPsmEnfLoginDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPsmEnfLoginDevType.setStatus("current")
_Hh3cFcPsmEnfLoginDev_Type = Hh3cFcNameIdOrZero
_Hh3cFcPsmEnfLoginDev_Object = MibTableColumn
hh3cFcPsmEnfLoginDev = _Hh3cFcPsmEnfLoginDev_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3, 1, 3),
    _Hh3cFcPsmEnfLoginDev_Type()
)
hh3cFcPsmEnfLoginDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPsmEnfLoginDev.setStatus("current")
_Hh3cFcPsmEnfLoginPoint_Type = InterfaceIndexOrZero
_Hh3cFcPsmEnfLoginPoint_Object = MibTableColumn
hh3cFcPsmEnfLoginPoint = _Hh3cFcPsmEnfLoginPoint_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3, 1, 4),
    _Hh3cFcPsmEnfLoginPoint_Type()
)
hh3cFcPsmEnfLoginPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPsmEnfLoginPoint.setStatus("current")


class _Hh3cFcPsmEnfEntryType_Type(Integer32):
    """Custom type hh3cFcPsmEnfEntryType based on Integer32"""
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


_Hh3cFcPsmEnfEntryType_Type.__name__ = "Integer32"
_Hh3cFcPsmEnfEntryType_Object = MibTableColumn
hh3cFcPsmEnfEntryType = _Hh3cFcPsmEnfEntryType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 3, 1, 5),
    _Hh3cFcPsmEnfEntryType_Type()
)
hh3cFcPsmEnfEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPsmEnfEntryType.setStatus("current")
_Hh3cFcPsmCopyToConfigTable_Object = MibTable
hh3cFcPsmCopyToConfigTable = _Hh3cFcPsmCopyToConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cFcPsmCopyToConfigTable.setStatus("current")
_Hh3cFcPsmCopyToConfigEntry_Object = MibTableRow
hh3cFcPsmCopyToConfigEntry = _Hh3cFcPsmCopyToConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 4, 1)
)
hh3cFcPsmCopyToConfigEntry.setIndexNames(
    (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcPsmCopyToConfigEntry.setStatus("current")


class _Hh3cFcPsmCopyToConfig_Type(Integer32):
    """Custom type hh3cFcPsmCopyToConfig based on Integer32"""
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


_Hh3cFcPsmCopyToConfig_Type.__name__ = "Integer32"
_Hh3cFcPsmCopyToConfig_Object = MibTableColumn
hh3cFcPsmCopyToConfig = _Hh3cFcPsmCopyToConfig_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 4, 1, 1),
    _Hh3cFcPsmCopyToConfig_Type()
)
hh3cFcPsmCopyToConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcPsmCopyToConfig.setStatus("current")
_Hh3cFcPsmAutoLearnTable_Object = MibTable
hh3cFcPsmAutoLearnTable = _Hh3cFcPsmAutoLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cFcPsmAutoLearnTable.setStatus("current")
_Hh3cFcPsmAutoLearnEntry_Object = MibTableRow
hh3cFcPsmAutoLearnEntry = _Hh3cFcPsmAutoLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 5, 1)
)
hh3cFcPsmAutoLearnEntry.setIndexNames(
    (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcPsmAutoLearnEntry.setStatus("current")


class _Hh3cFcPsmAutoLearnEnable_Type(TruthValue):
    """Custom type hh3cFcPsmAutoLearnEnable based on TruthValue"""


_Hh3cFcPsmAutoLearnEnable_Object = MibTableColumn
hh3cFcPsmAutoLearnEnable = _Hh3cFcPsmAutoLearnEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 5, 1, 1),
    _Hh3cFcPsmAutoLearnEnable_Type()
)
hh3cFcPsmAutoLearnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcPsmAutoLearnEnable.setStatus("current")
_Hh3cFcPsmClearTable_Object = MibTable
hh3cFcPsmClearTable = _Hh3cFcPsmClearTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cFcPsmClearTable.setStatus("current")
_Hh3cFcPsmClearEntry_Object = MibTableRow
hh3cFcPsmClearEntry = _Hh3cFcPsmClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 6, 1)
)
hh3cFcPsmClearEntry.setIndexNames(
    (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcPsmClearEntry.setStatus("current")


class _Hh3cFcPsmClearType_Type(Hh3cFcPsmClearEntryType):
    """Custom type hh3cFcPsmClearType based on Hh3cFcPsmClearEntryType"""


_Hh3cFcPsmClearType_Object = MibTableColumn
hh3cFcPsmClearType = _Hh3cFcPsmClearType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 6, 1, 1),
    _Hh3cFcPsmClearType_Type()
)
hh3cFcPsmClearType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcPsmClearType.setStatus("current")
_Hh3cFcPsmClearIntf_Type = InterfaceIndexOrZero
_Hh3cFcPsmClearIntf_Object = MibTableColumn
hh3cFcPsmClearIntf = _Hh3cFcPsmClearIntf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 2, 6, 1, 2),
    _Hh3cFcPsmClearIntf_Type()
)
hh3cFcPsmClearIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcPsmClearIntf.setStatus("current")
_Hh3cFcPsmStats_ObjectIdentity = ObjectIdentity
hh3cFcPsmStats = _Hh3cFcPsmStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3)
)
_Hh3cFcPsmStatsTable_Object = MibTable
hh3cFcPsmStatsTable = _Hh3cFcPsmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cFcPsmStatsTable.setStatus("current")
_Hh3cFcPsmStatsEntry_Object = MibTableRow
hh3cFcPsmStatsEntry = _Hh3cFcPsmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 1, 1)
)
hh3cFcPsmStatsEntry.setIndexNames(
    (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcPsmStatsEntry.setStatus("current")
_Hh3cFcPsmAllowedLogins_Type = Counter32
_Hh3cFcPsmAllowedLogins_Object = MibTableColumn
hh3cFcPsmAllowedLogins = _Hh3cFcPsmAllowedLogins_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 1, 1, 1),
    _Hh3cFcPsmAllowedLogins_Type()
)
hh3cFcPsmAllowedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPsmAllowedLogins.setStatus("current")
_Hh3cFcPsmDeniedLogins_Type = Counter32
_Hh3cFcPsmDeniedLogins_Object = MibTableColumn
hh3cFcPsmDeniedLogins = _Hh3cFcPsmDeniedLogins_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 1, 1, 2),
    _Hh3cFcPsmDeniedLogins_Type()
)
hh3cFcPsmDeniedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPsmDeniedLogins.setStatus("current")


class _Hh3cFcPsmStatsClear_Type(Integer32):
    """Custom type hh3cFcPsmStatsClear based on Integer32"""
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


_Hh3cFcPsmStatsClear_Type.__name__ = "Integer32"
_Hh3cFcPsmStatsClear_Object = MibTableColumn
hh3cFcPsmStatsClear = _Hh3cFcPsmStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 1, 1, 3),
    _Hh3cFcPsmStatsClear_Type()
)
hh3cFcPsmStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcPsmStatsClear.setStatus("current")
_Hh3cFcPsmViolationTable_Object = MibTable
hh3cFcPsmViolationTable = _Hh3cFcPsmViolationTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cFcPsmViolationTable.setStatus("current")
_Hh3cFcPsmViolationEntry_Object = MibTableRow
hh3cFcPsmViolationEntry = _Hh3cFcPsmViolationEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1)
)
hh3cFcPsmViolationEntry.setIndexNames(
    (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmEnableVsanIndex"),
    (0, "HH3C-FC-PSM-MIB", "hh3cFcPsmViolationIndex"),
)
if mibBuilder.loadTexts:
    hh3cFcPsmViolationEntry.setStatus("current")


class _Hh3cFcPsmViolationIndex_Type(Unsigned32):
    """Custom type hh3cFcPsmViolationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cFcPsmViolationIndex_Type.__name__ = "Unsigned32"
_Hh3cFcPsmViolationIndex_Object = MibTableColumn
hh3cFcPsmViolationIndex = _Hh3cFcPsmViolationIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 1),
    _Hh3cFcPsmViolationIndex_Type()
)
hh3cFcPsmViolationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFcPsmViolationIndex.setStatus("current")
_Hh3cFcPsmLoginPWWN_Type = Hh3cFcNameIdOrZero
_Hh3cFcPsmLoginPWWN_Object = MibTableColumn
hh3cFcPsmLoginPWWN = _Hh3cFcPsmLoginPWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 2),
    _Hh3cFcPsmLoginPWWN_Type()
)
hh3cFcPsmLoginPWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPsmLoginPWWN.setStatus("current")
_Hh3cFcPsmLoginNWWN_Type = Hh3cFcNameIdOrZero
_Hh3cFcPsmLoginNWWN_Object = MibTableColumn
hh3cFcPsmLoginNWWN = _Hh3cFcPsmLoginNWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 3),
    _Hh3cFcPsmLoginNWWN_Type()
)
hh3cFcPsmLoginNWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPsmLoginNWWN.setStatus("current")
_Hh3cFcPsmLoginSWWN_Type = Hh3cFcNameIdOrZero
_Hh3cFcPsmLoginSWWN_Object = MibTableColumn
hh3cFcPsmLoginSWWN = _Hh3cFcPsmLoginSWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 4),
    _Hh3cFcPsmLoginSWWN_Type()
)
hh3cFcPsmLoginSWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPsmLoginSWWN.setStatus("current")
_Hh3cFcPsmLoginIntf_Type = InterfaceIndex
_Hh3cFcPsmLoginIntf_Object = MibTableColumn
hh3cFcPsmLoginIntf = _Hh3cFcPsmLoginIntf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 5),
    _Hh3cFcPsmLoginIntf_Type()
)
hh3cFcPsmLoginIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPsmLoginIntf.setStatus("current")
_Hh3cFcPsmLoginTime_Type = TimeStamp
_Hh3cFcPsmLoginTime_Object = MibTableColumn
hh3cFcPsmLoginTime = _Hh3cFcPsmLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 6),
    _Hh3cFcPsmLoginTime_Type()
)
hh3cFcPsmLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPsmLoginTime.setStatus("current")
_Hh3cFcPsmLoginCount_Type = Counter32
_Hh3cFcPsmLoginCount_Object = MibTableColumn
hh3cFcPsmLoginCount = _Hh3cFcPsmLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 1, 3, 2, 1, 7),
    _Hh3cFcPsmLoginCount_Type()
)
hh3cFcPsmLoginCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcPsmLoginCount.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cFcPsmFPortDenyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 0, 1)
)
hh3cFcPsmFPortDenyNotify.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HH3C-FC-PSM-MIB", "hh3cFcPsmLoginPWWN"),
        ("HH3C-FC-PSM-MIB", "hh3cFcPsmLoginIntf"),
        ("HH3C-FC-PSM-MIB", "hh3cFcPsmLoginTime"))
)
if mibBuilder.loadTexts:
    hh3cFcPsmFPortDenyNotify.setStatus(
        "current"
    )

hh3cFcPsmEPortDenyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 8, 0, 2)
)
hh3cFcPsmEPortDenyNotify.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HH3C-FC-PSM-MIB", "hh3cFcPsmLoginSWWN"),
        ("HH3C-FC-PSM-MIB", "hh3cFcPsmLoginIntf"),
        ("HH3C-FC-PSM-MIB", "hh3cFcPsmLoginTime"))
)
if mibBuilder.loadTexts:
    hh3cFcPsmEPortDenyNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FC-PSM-MIB",
    **{"Hh3cFcPsmPortBindDevType": Hh3cFcPsmPortBindDevType,
       "Hh3cFcPsmClearEntryType": Hh3cFcPsmClearEntryType,
       "hh3cFcPsm": hh3cFcPsm,
       "hh3cFcPsmNotifications": hh3cFcPsmNotifications,
       "hh3cFcPsmFPortDenyNotify": hh3cFcPsmFPortDenyNotify,
       "hh3cFcPsmEPortDenyNotify": hh3cFcPsmEPortDenyNotify,
       "hh3cFcPsmObjects": hh3cFcPsmObjects,
       "hh3cFcPsmScalarObjects": hh3cFcPsmScalarObjects,
       "hh3cFcPsmNotifyEnable": hh3cFcPsmNotifyEnable,
       "hh3cFcPsmConfiguration": hh3cFcPsmConfiguration,
       "hh3cFcPsmEnableTable": hh3cFcPsmEnableTable,
       "hh3cFcPsmEnableEntry": hh3cFcPsmEnableEntry,
       "hh3cFcPsmEnableVsanIndex": hh3cFcPsmEnableVsanIndex,
       "hh3cFcPsmEnable": hh3cFcPsmEnable,
       "hh3cFcPsmEnableState": hh3cFcPsmEnableState,
       "hh3cFcPsmConfigTable": hh3cFcPsmConfigTable,
       "hh3cFcPsmConfigEntry": hh3cFcPsmConfigEntry,
       "hh3cFcPsmIndex": hh3cFcPsmIndex,
       "hh3cFcPsmLoginDevType": hh3cFcPsmLoginDevType,
       "hh3cFcPsmLoginDev": hh3cFcPsmLoginDev,
       "hh3cFcPsmLoginPoint": hh3cFcPsmLoginPoint,
       "hh3cFcPsmRowStatus": hh3cFcPsmRowStatus,
       "hh3cFcPsmEnfTable": hh3cFcPsmEnfTable,
       "hh3cFcPsmEnfEntry": hh3cFcPsmEnfEntry,
       "hh3cFcPsmEnfIndex": hh3cFcPsmEnfIndex,
       "hh3cFcPsmEnfLoginDevType": hh3cFcPsmEnfLoginDevType,
       "hh3cFcPsmEnfLoginDev": hh3cFcPsmEnfLoginDev,
       "hh3cFcPsmEnfLoginPoint": hh3cFcPsmEnfLoginPoint,
       "hh3cFcPsmEnfEntryType": hh3cFcPsmEnfEntryType,
       "hh3cFcPsmCopyToConfigTable": hh3cFcPsmCopyToConfigTable,
       "hh3cFcPsmCopyToConfigEntry": hh3cFcPsmCopyToConfigEntry,
       "hh3cFcPsmCopyToConfig": hh3cFcPsmCopyToConfig,
       "hh3cFcPsmAutoLearnTable": hh3cFcPsmAutoLearnTable,
       "hh3cFcPsmAutoLearnEntry": hh3cFcPsmAutoLearnEntry,
       "hh3cFcPsmAutoLearnEnable": hh3cFcPsmAutoLearnEnable,
       "hh3cFcPsmClearTable": hh3cFcPsmClearTable,
       "hh3cFcPsmClearEntry": hh3cFcPsmClearEntry,
       "hh3cFcPsmClearType": hh3cFcPsmClearType,
       "hh3cFcPsmClearIntf": hh3cFcPsmClearIntf,
       "hh3cFcPsmStats": hh3cFcPsmStats,
       "hh3cFcPsmStatsTable": hh3cFcPsmStatsTable,
       "hh3cFcPsmStatsEntry": hh3cFcPsmStatsEntry,
       "hh3cFcPsmAllowedLogins": hh3cFcPsmAllowedLogins,
       "hh3cFcPsmDeniedLogins": hh3cFcPsmDeniedLogins,
       "hh3cFcPsmStatsClear": hh3cFcPsmStatsClear,
       "hh3cFcPsmViolationTable": hh3cFcPsmViolationTable,
       "hh3cFcPsmViolationEntry": hh3cFcPsmViolationEntry,
       "hh3cFcPsmViolationIndex": hh3cFcPsmViolationIndex,
       "hh3cFcPsmLoginPWWN": hh3cFcPsmLoginPWWN,
       "hh3cFcPsmLoginNWWN": hh3cFcPsmLoginNWWN,
       "hh3cFcPsmLoginSWWN": hh3cFcPsmLoginSWWN,
       "hh3cFcPsmLoginIntf": hh3cFcPsmLoginIntf,
       "hh3cFcPsmLoginTime": hh3cFcPsmLoginTime,
       "hh3cFcPsmLoginCount": hh3cFcPsmLoginCount}
)
