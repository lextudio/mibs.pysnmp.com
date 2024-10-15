# SNMP MIB module (SRED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SRED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:38 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

swSredMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 51)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSredCtrl_ObjectIdentity = ObjectIdentity
swSredCtrl = _SwSredCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 1)
)


class _SwSredGlobalState_Type(Integer32):
    """Custom type swSredGlobalState based on Integer32"""
    defaultValue = 2

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


_SwSredGlobalState_Type.__name__ = "Integer32"
_SwSredGlobalState_Object = MibScalar
swSredGlobalState = _SwSredGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 1, 1),
    _SwSredGlobalState_Type()
)
swSredGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSredGlobalState.setStatus("current")
_SwSredInfo_ObjectIdentity = ObjectIdentity
swSredInfo = _SwSredInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 2)
)
_SwSredDropCounterTable_Object = MibTable
swSredDropCounterTable = _SwSredDropCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 2, 1)
)
if mibBuilder.loadTexts:
    swSredDropCounterTable.setStatus("current")
_SwSredDropCounterEntry_Object = MibTableRow
swSredDropCounterEntry = _SwSredDropCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 2, 1, 1)
)
swSredDropCounterEntry.setIndexNames(
    (0, "SRED-MIB", "swSredPortIndex"),
)
if mibBuilder.loadTexts:
    swSredDropCounterEntry.setStatus("current")
_SwSredPortIndex_Type = Integer32
_SwSredPortIndex_Object = MibTableColumn
swSredPortIndex = _SwSredPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 2, 1, 1, 1),
    _SwSredPortIndex_Type()
)
swSredPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSredPortIndex.setStatus("current")
_SwSredLowDropCounter_Type = Counter32
_SwSredLowDropCounter_Object = MibTableColumn
swSredLowDropCounter = _SwSredLowDropCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 2, 1, 1, 2),
    _SwSredLowDropCounter_Type()
)
swSredLowDropCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSredLowDropCounter.setStatus("current")
_SwSredHighDropCounter_Type = Counter32
_SwSredHighDropCounter_Object = MibTableColumn
swSredHighDropCounter = _SwSredHighDropCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 2, 1, 1, 3),
    _SwSredHighDropCounter_Type()
)
swSredHighDropCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSredHighDropCounter.setStatus("current")
_SwSredMgmt_ObjectIdentity = ObjectIdentity
swSredMgmt = _SwSredMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3)
)
_SwSredCtrlTable_Object = MibTable
swSredCtrlTable = _SwSredCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1)
)
if mibBuilder.loadTexts:
    swSredCtrlTable.setStatus("current")
_SwSredCtrlEntry_Object = MibTableRow
swSredCtrlEntry = _SwSredCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1)
)
swSredCtrlEntry.setIndexNames(
    (0, "SRED-MIB", "swSredCtrlPortIndex"),
    (0, "SRED-MIB", "swSredCtrlClassIndex"),
)
if mibBuilder.loadTexts:
    swSredCtrlEntry.setStatus("current")
_SwSredCtrlPortIndex_Type = Integer32
_SwSredCtrlPortIndex_Object = MibTableColumn
swSredCtrlPortIndex = _SwSredCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 1),
    _SwSredCtrlPortIndex_Type()
)
swSredCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSredCtrlPortIndex.setStatus("current")
_SwSredCtrlClassIndex_Type = Integer32
_SwSredCtrlClassIndex_Object = MibTableColumn
swSredCtrlClassIndex = _SwSredCtrlClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 2),
    _SwSredCtrlClassIndex_Type()
)
swSredCtrlClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSredCtrlClassIndex.setStatus("current")


class _SwSredCtrlThresholdLow_Type(Integer32):
    """Custom type swSredCtrlThresholdLow based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwSredCtrlThresholdLow_Type.__name__ = "Integer32"
_SwSredCtrlThresholdLow_Object = MibTableColumn
swSredCtrlThresholdLow = _SwSredCtrlThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 3),
    _SwSredCtrlThresholdLow_Type()
)
swSredCtrlThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSredCtrlThresholdLow.setStatus("current")


class _SwSredCtrlThresholdHigh_Type(Integer32):
    """Custom type swSredCtrlThresholdHigh based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwSredCtrlThresholdHigh_Type.__name__ = "Integer32"
_SwSredCtrlThresholdHigh_Object = MibTableColumn
swSredCtrlThresholdHigh = _SwSredCtrlThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 4),
    _SwSredCtrlThresholdHigh_Type()
)
swSredCtrlThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSredCtrlThresholdHigh.setStatus("current")


class _SwSredCtrlDropRateLow_Type(Integer32):
    """Custom type swSredCtrlDropRateLow based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SwSredCtrlDropRateLow_Type.__name__ = "Integer32"
_SwSredCtrlDropRateLow_Object = MibTableColumn
swSredCtrlDropRateLow = _SwSredCtrlDropRateLow_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 5),
    _SwSredCtrlDropRateLow_Type()
)
swSredCtrlDropRateLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSredCtrlDropRateLow.setStatus("current")


class _SwSredCtrlDropRateHigh_Type(Integer32):
    """Custom type swSredCtrlDropRateHigh based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SwSredCtrlDropRateHigh_Type.__name__ = "Integer32"
_SwSredCtrlDropRateHigh_Object = MibTableColumn
swSredCtrlDropRateHigh = _SwSredCtrlDropRateHigh_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 6),
    _SwSredCtrlDropRateHigh_Type()
)
swSredCtrlDropRateHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSredCtrlDropRateHigh.setStatus("current")


class _SwSredCtrlDropGreenState_Type(Integer32):
    """Custom type swSredCtrlDropGreenState based on Integer32"""
    defaultValue = 2

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


_SwSredCtrlDropGreenState_Type.__name__ = "Integer32"
_SwSredCtrlDropGreenState_Object = MibTableColumn
swSredCtrlDropGreenState = _SwSredCtrlDropGreenState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 1, 1, 7),
    _SwSredCtrlDropGreenState_Type()
)
swSredCtrlDropGreenState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSredCtrlDropGreenState.setStatus("current")
_Sw8021pColorMapCtrlTable_Object = MibTable
sw8021pColorMapCtrlTable = _Sw8021pColorMapCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 2)
)
if mibBuilder.loadTexts:
    sw8021pColorMapCtrlTable.setStatus("obsolete")
_Sw8021pColorMapCtrlEntry_Object = MibTableRow
sw8021pColorMapCtrlEntry = _Sw8021pColorMapCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 2, 1)
)
sw8021pColorMapCtrlEntry.setIndexNames(
    (0, "SRED-MIB", "sw8021pColorMapCtrlPortIndex"),
    (0, "SRED-MIB", "sw8021pColorMapCtrlPriorityIndex"),
)
if mibBuilder.loadTexts:
    sw8021pColorMapCtrlEntry.setStatus("obsolete")
_Sw8021pColorMapCtrlPortIndex_Type = Integer32
_Sw8021pColorMapCtrlPortIndex_Object = MibTableColumn
sw8021pColorMapCtrlPortIndex = _Sw8021pColorMapCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 2, 1, 1),
    _Sw8021pColorMapCtrlPortIndex_Type()
)
sw8021pColorMapCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw8021pColorMapCtrlPortIndex.setStatus("obsolete")
_Sw8021pColorMapCtrlPriorityIndex_Type = Integer32
_Sw8021pColorMapCtrlPriorityIndex_Object = MibTableColumn
sw8021pColorMapCtrlPriorityIndex = _Sw8021pColorMapCtrlPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 2, 1, 2),
    _Sw8021pColorMapCtrlPriorityIndex_Type()
)
sw8021pColorMapCtrlPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sw8021pColorMapCtrlPriorityIndex.setStatus("obsolete")


class _Sw8021pColorMapCtrlColor_Type(Integer32):
    """Custom type sw8021pColorMapCtrlColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 2),
          ("yellow", 3))
    )


_Sw8021pColorMapCtrlColor_Type.__name__ = "Integer32"
_Sw8021pColorMapCtrlColor_Object = MibTableColumn
sw8021pColorMapCtrlColor = _Sw8021pColorMapCtrlColor_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 2, 1, 3),
    _Sw8021pColorMapCtrlColor_Type()
)
sw8021pColorMapCtrlColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sw8021pColorMapCtrlColor.setStatus("obsolete")
_SwDscpTrustPortCtrlTable_Object = MibTable
swDscpTrustPortCtrlTable = _SwDscpTrustPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 3)
)
if mibBuilder.loadTexts:
    swDscpTrustPortCtrlTable.setStatus("obsolete")
_SwDscpTrustPortCtrlEntry_Object = MibTableRow
swDscpTrustPortCtrlEntry = _SwDscpTrustPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 3, 1)
)
swDscpTrustPortCtrlEntry.setIndexNames(
    (0, "SRED-MIB", "swDscpTrustPortCtrlPortIndex"),
)
if mibBuilder.loadTexts:
    swDscpTrustPortCtrlEntry.setStatus("obsolete")
_SwDscpTrustPortCtrlPortIndex_Type = Integer32
_SwDscpTrustPortCtrlPortIndex_Object = MibTableColumn
swDscpTrustPortCtrlPortIndex = _SwDscpTrustPortCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 3, 1, 1),
    _SwDscpTrustPortCtrlPortIndex_Type()
)
swDscpTrustPortCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDscpTrustPortCtrlPortIndex.setStatus("obsolete")


class _SwDscpTrustPortCtrlState_Type(Integer32):
    """Custom type swDscpTrustPortCtrlState based on Integer32"""
    defaultValue = 2

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


_SwDscpTrustPortCtrlState_Type.__name__ = "Integer32"
_SwDscpTrustPortCtrlState_Object = MibTableColumn
swDscpTrustPortCtrlState = _SwDscpTrustPortCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 3, 1, 2),
    _SwDscpTrustPortCtrlState_Type()
)
swDscpTrustPortCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDscpTrustPortCtrlState.setStatus("obsolete")
_SwDscpMapCtrlTable_Object = MibTable
swDscpMapCtrlTable = _SwDscpMapCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4)
)
if mibBuilder.loadTexts:
    swDscpMapCtrlTable.setStatus("obsolete")
_SwDscpMapCtrlEntry_Object = MibTableRow
swDscpMapCtrlEntry = _SwDscpMapCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4, 1)
)
swDscpMapCtrlEntry.setIndexNames(
    (0, "SRED-MIB", "swDscpMapCtrlPortIndex"),
    (0, "SRED-MIB", "swDscpMapCtrlDscpIndex"),
)
if mibBuilder.loadTexts:
    swDscpMapCtrlEntry.setStatus("obsolete")
_SwDscpMapCtrlPortIndex_Type = Integer32
_SwDscpMapCtrlPortIndex_Object = MibTableColumn
swDscpMapCtrlPortIndex = _SwDscpMapCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4, 1, 1),
    _SwDscpMapCtrlPortIndex_Type()
)
swDscpMapCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDscpMapCtrlPortIndex.setStatus("obsolete")
_SwDscpMapCtrlDscpIndex_Type = Integer32
_SwDscpMapCtrlDscpIndex_Object = MibTableColumn
swDscpMapCtrlDscpIndex = _SwDscpMapCtrlDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4, 1, 2),
    _SwDscpMapCtrlDscpIndex_Type()
)
swDscpMapCtrlDscpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDscpMapCtrlDscpIndex.setStatus("obsolete")


class _SwDscpMapCtrl8021pPriority_Type(Integer32):
    """Custom type swDscpMapCtrl8021pPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwDscpMapCtrl8021pPriority_Type.__name__ = "Integer32"
_SwDscpMapCtrl8021pPriority_Object = MibTableColumn
swDscpMapCtrl8021pPriority = _SwDscpMapCtrl8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4, 1, 3),
    _SwDscpMapCtrl8021pPriority_Type()
)
swDscpMapCtrl8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDscpMapCtrl8021pPriority.setStatus("obsolete")


class _SwDscpMapCtrlNewDscp_Type(Integer32):
    """Custom type swDscpMapCtrlNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwDscpMapCtrlNewDscp_Type.__name__ = "Integer32"
_SwDscpMapCtrlNewDscp_Object = MibTableColumn
swDscpMapCtrlNewDscp = _SwDscpMapCtrlNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4, 1, 4),
    _SwDscpMapCtrlNewDscp_Type()
)
swDscpMapCtrlNewDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDscpMapCtrlNewDscp.setStatus("obsolete")


class _SwDscpMapCtrlColor_Type(Integer32):
    """Custom type swDscpMapCtrlColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 2),
          ("yellow", 3))
    )


_SwDscpMapCtrlColor_Type.__name__ = "Integer32"
_SwDscpMapCtrlColor_Object = MibTableColumn
swDscpMapCtrlColor = _SwDscpMapCtrlColor_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 51, 3, 4, 1, 5),
    _SwDscpMapCtrlColor_Type()
)
swDscpMapCtrlColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDscpMapCtrlColor.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SRED-MIB",
    **{"swSredMIB": swSredMIB,
       "swSredCtrl": swSredCtrl,
       "swSredGlobalState": swSredGlobalState,
       "swSredInfo": swSredInfo,
       "swSredDropCounterTable": swSredDropCounterTable,
       "swSredDropCounterEntry": swSredDropCounterEntry,
       "swSredPortIndex": swSredPortIndex,
       "swSredLowDropCounter": swSredLowDropCounter,
       "swSredHighDropCounter": swSredHighDropCounter,
       "swSredMgmt": swSredMgmt,
       "swSredCtrlTable": swSredCtrlTable,
       "swSredCtrlEntry": swSredCtrlEntry,
       "swSredCtrlPortIndex": swSredCtrlPortIndex,
       "swSredCtrlClassIndex": swSredCtrlClassIndex,
       "swSredCtrlThresholdLow": swSredCtrlThresholdLow,
       "swSredCtrlThresholdHigh": swSredCtrlThresholdHigh,
       "swSredCtrlDropRateLow": swSredCtrlDropRateLow,
       "swSredCtrlDropRateHigh": swSredCtrlDropRateHigh,
       "swSredCtrlDropGreenState": swSredCtrlDropGreenState,
       "sw8021pColorMapCtrlTable": sw8021pColorMapCtrlTable,
       "sw8021pColorMapCtrlEntry": sw8021pColorMapCtrlEntry,
       "sw8021pColorMapCtrlPortIndex": sw8021pColorMapCtrlPortIndex,
       "sw8021pColorMapCtrlPriorityIndex": sw8021pColorMapCtrlPriorityIndex,
       "sw8021pColorMapCtrlColor": sw8021pColorMapCtrlColor,
       "swDscpTrustPortCtrlTable": swDscpTrustPortCtrlTable,
       "swDscpTrustPortCtrlEntry": swDscpTrustPortCtrlEntry,
       "swDscpTrustPortCtrlPortIndex": swDscpTrustPortCtrlPortIndex,
       "swDscpTrustPortCtrlState": swDscpTrustPortCtrlState,
       "swDscpMapCtrlTable": swDscpMapCtrlTable,
       "swDscpMapCtrlEntry": swDscpMapCtrlEntry,
       "swDscpMapCtrlPortIndex": swDscpMapCtrlPortIndex,
       "swDscpMapCtrlDscpIndex": swDscpMapCtrlDscpIndex,
       "swDscpMapCtrl8021pPriority": swDscpMapCtrl8021pPriority,
       "swDscpMapCtrlNewDscp": swDscpMapCtrlNewDscp,
       "swDscpMapCtrlColor": swDscpMapCtrlColor}
)
