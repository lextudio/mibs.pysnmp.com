# SNMP MIB module (DOCS-IFEXT2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-IFEXT2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:48 2024
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

(clabProjDocsis,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjDocsis")

(TenthdB,
 TenthdBmV,
 docsIfCmtsCmStatusIndex) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdB",
    "TenthdBmV",
    "docsIfCmtsCmStatusIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

docsIfExt2Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5)
)
docsIfExt2Mib.setRevisions(
        ("2010-10-08 17:00",
         "2004-11-10 17:00",
         "2004-06-23 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DocsIfExt2Notifications_ObjectIdentity = ObjectIdentity
docsIfExt2Notifications = _DocsIfExt2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 0)
)
_DocsIfExt2MibObjects_ObjectIdentity = ObjectIdentity
docsIfExt2MibObjects = _DocsIfExt2MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1)
)
_DocsIfExt2BaseObjects_ObjectIdentity = ObjectIdentity
docsIfExt2BaseObjects = _DocsIfExt2BaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 1)
)
_DocsIfExt2CmObjects_ObjectIdentity = ObjectIdentity
docsIfExt2CmObjects = _DocsIfExt2CmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 2)
)
_DocsIfExt2CmMscStatusTable_Object = MibTable
docsIfExt2CmMscStatusTable = _DocsIfExt2CmMscStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    docsIfExt2CmMscStatusTable.setStatus("current")
_DocsIfExt2CmMscStatusEntry_Object = MibTableRow
docsIfExt2CmMscStatusEntry = _DocsIfExt2CmMscStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 2, 1, 1)
)
docsIfExt2CmMscStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfExt2CmMscStatusEntry.setStatus("current")


class _DocsIfExt2CmMscStatusState_Type(Integer32):
    """Custom type docsIfExt2CmMscStatusState based on Integer32"""
    defaultValue = 5

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
        *(("active", 3),
          ("channelDisabled", 2),
          ("channelEnabled", 1),
          ("inactive", 4),
          ("unknown", 5))
    )


_DocsIfExt2CmMscStatusState_Type.__name__ = "Integer32"
_DocsIfExt2CmMscStatusState_Object = MibTableColumn
docsIfExt2CmMscStatusState = _DocsIfExt2CmMscStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 2, 1, 1, 1),
    _DocsIfExt2CmMscStatusState_Type()
)
docsIfExt2CmMscStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmMscStatusState.setStatus("current")


class _DocsIfExt2CmMscStatusPowerShortfall_Type(TenthdB):
    """Custom type docsIfExt2CmMscStatusPowerShortfall based on TenthdB"""
    defaultValue = 0


_DocsIfExt2CmMscStatusPowerShortfall_Object = MibTableColumn
docsIfExt2CmMscStatusPowerShortfall = _DocsIfExt2CmMscStatusPowerShortfall_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 2, 1, 1, 2),
    _DocsIfExt2CmMscStatusPowerShortfall_Type()
)
docsIfExt2CmMscStatusPowerShortfall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmMscStatusPowerShortfall.setStatus("current")
if mibBuilder.loadTexts:
    docsIfExt2CmMscStatusPowerShortfall.setUnits("TenthdB")


class _DocsIfExt2CmMscStatusCodeRatio_Type(Unsigned32):
    """Custom type docsIfExt2CmMscStatusCodeRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
    )


_DocsIfExt2CmMscStatusCodeRatio_Type.__name__ = "Unsigned32"
_DocsIfExt2CmMscStatusCodeRatio_Object = MibTableColumn
docsIfExt2CmMscStatusCodeRatio = _DocsIfExt2CmMscStatusCodeRatio_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 2, 1, 1, 3),
    _DocsIfExt2CmMscStatusCodeRatio_Type()
)
docsIfExt2CmMscStatusCodeRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmMscStatusCodeRatio.setStatus("current")


class _DocsIfExt2CmMscStatusMaximumScheduledCodes_Type(Unsigned32):
    """Custom type docsIfExt2CmMscStatusMaximumScheduledCodes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 128),
    )


_DocsIfExt2CmMscStatusMaximumScheduledCodes_Type.__name__ = "Unsigned32"
_DocsIfExt2CmMscStatusMaximumScheduledCodes_Object = MibTableColumn
docsIfExt2CmMscStatusMaximumScheduledCodes = _DocsIfExt2CmMscStatusMaximumScheduledCodes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 2, 1, 1, 4),
    _DocsIfExt2CmMscStatusMaximumScheduledCodes_Type()
)
docsIfExt2CmMscStatusMaximumScheduledCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmMscStatusMaximumScheduledCodes.setStatus("current")


class _DocsIfExt2CmMscStatusPowerHeadroom_Type(TenthdB):
    """Custom type docsIfExt2CmMscStatusPowerHeadroom based on TenthdB"""
    defaultValue = 0


_DocsIfExt2CmMscStatusPowerHeadroom_Object = MibTableColumn
docsIfExt2CmMscStatusPowerHeadroom = _DocsIfExt2CmMscStatusPowerHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 2, 1, 1, 5),
    _DocsIfExt2CmMscStatusPowerHeadroom_Type()
)
docsIfExt2CmMscStatusPowerHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmMscStatusPowerHeadroom.setStatus("current")
if mibBuilder.loadTexts:
    docsIfExt2CmMscStatusPowerHeadroom.setUnits("TenthdB")
_DocsIfExt2CmMscStatusEffectivePower_Type = TenthdBmV
_DocsIfExt2CmMscStatusEffectivePower_Object = MibTableColumn
docsIfExt2CmMscStatusEffectivePower = _DocsIfExt2CmMscStatusEffectivePower_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 2, 1, 1, 6),
    _DocsIfExt2CmMscStatusEffectivePower_Type()
)
docsIfExt2CmMscStatusEffectivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmMscStatusEffectivePower.setStatus("current")
if mibBuilder.loadTexts:
    docsIfExt2CmMscStatusEffectivePower.setUnits("TenthdBmV")


class _DocsIfExt2CmMscStatusIUC2Control_Type(Integer32):
    """Custom type docsIfExt2CmMscStatusIUC2Control based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("freeIUC2", 3),
          ("limitedIUC2", 2),
          ("noIUC2", 1))
    )


_DocsIfExt2CmMscStatusIUC2Control_Type.__name__ = "Integer32"
_DocsIfExt2CmMscStatusIUC2Control_Object = MibTableColumn
docsIfExt2CmMscStatusIUC2Control = _DocsIfExt2CmMscStatusIUC2Control_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 2, 1, 1, 7),
    _DocsIfExt2CmMscStatusIUC2Control_Type()
)
docsIfExt2CmMscStatusIUC2Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfExt2CmMscStatusIUC2Control.setStatus("current")


class _DocsIfExt2CmClearLearnedMacAddresses_Type(TruthValue):
    """Custom type docsIfExt2CmClearLearnedMacAddresses based on TruthValue"""


_DocsIfExt2CmClearLearnedMacAddresses_Object = MibScalar
docsIfExt2CmClearLearnedMacAddresses = _DocsIfExt2CmClearLearnedMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 2, 2),
    _DocsIfExt2CmClearLearnedMacAddresses_Type()
)
docsIfExt2CmClearLearnedMacAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfExt2CmClearLearnedMacAddresses.setStatus("current")
_DocsIfExt2CmtsObjects_ObjectIdentity = ObjectIdentity
docsIfExt2CmtsObjects = _DocsIfExt2CmtsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3)
)


class _DocsIfExt2CmtsMscGlobalEnable_Type(TruthValue):
    """Custom type docsIfExt2CmtsMscGlobalEnable based on TruthValue"""


_DocsIfExt2CmtsMscGlobalEnable_Object = MibScalar
docsIfExt2CmtsMscGlobalEnable = _DocsIfExt2CmtsMscGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 1),
    _DocsIfExt2CmtsMscGlobalEnable_Type()
)
docsIfExt2CmtsMscGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfExt2CmtsMscGlobalEnable.setStatus("current")
_DocsIfExt2CmtsCmMscStatusTable_Object = MibTable
docsIfExt2CmtsCmMscStatusTable = _DocsIfExt2CmtsCmMscStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    docsIfExt2CmtsCmMscStatusTable.setStatus("current")
_DocsIfExt2CmtsCmMscStatusEntry_Object = MibTableRow
docsIfExt2CmtsCmMscStatusEntry = _DocsIfExt2CmtsCmMscStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 2, 1)
)
docsIfExt2CmtsCmMscStatusEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    docsIfExt2CmtsCmMscStatusEntry.setStatus("current")


class _DocsIfExt2CmtsCmMscStatusPowerShortfall_Type(TenthdB):
    """Custom type docsIfExt2CmtsCmMscStatusPowerShortfall based on TenthdB"""
    defaultValue = 0


_DocsIfExt2CmtsCmMscStatusPowerShortfall_Object = MibTableColumn
docsIfExt2CmtsCmMscStatusPowerShortfall = _DocsIfExt2CmtsCmMscStatusPowerShortfall_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 2, 1, 1),
    _DocsIfExt2CmtsCmMscStatusPowerShortfall_Type()
)
docsIfExt2CmtsCmMscStatusPowerShortfall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmtsCmMscStatusPowerShortfall.setStatus("current")
if mibBuilder.loadTexts:
    docsIfExt2CmtsCmMscStatusPowerShortfall.setUnits("TenthdB")


class _DocsIfExt2CmtsCmMscStatusCodeRatio_Type(Unsigned32):
    """Custom type docsIfExt2CmtsCmMscStatusCodeRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
    )


_DocsIfExt2CmtsCmMscStatusCodeRatio_Type.__name__ = "Unsigned32"
_DocsIfExt2CmtsCmMscStatusCodeRatio_Object = MibTableColumn
docsIfExt2CmtsCmMscStatusCodeRatio = _DocsIfExt2CmtsCmMscStatusCodeRatio_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 2, 1, 2),
    _DocsIfExt2CmtsCmMscStatusCodeRatio_Type()
)
docsIfExt2CmtsCmMscStatusCodeRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmtsCmMscStatusCodeRatio.setStatus("current")


class _DocsIfExt2CmtsCmMscStatusMaximumScheduledCodes_Type(Unsigned32):
    """Custom type docsIfExt2CmtsCmMscStatusMaximumScheduledCodes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 128),
    )


_DocsIfExt2CmtsCmMscStatusMaximumScheduledCodes_Type.__name__ = "Unsigned32"
_DocsIfExt2CmtsCmMscStatusMaximumScheduledCodes_Object = MibTableColumn
docsIfExt2CmtsCmMscStatusMaximumScheduledCodes = _DocsIfExt2CmtsCmMscStatusMaximumScheduledCodes_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 2, 1, 3),
    _DocsIfExt2CmtsCmMscStatusMaximumScheduledCodes_Type()
)
docsIfExt2CmtsCmMscStatusMaximumScheduledCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmtsCmMscStatusMaximumScheduledCodes.setStatus("current")


class _DocsIfExt2CmtsCmMscStatusPowerHeadroom_Type(TenthdB):
    """Custom type docsIfExt2CmtsCmMscStatusPowerHeadroom based on TenthdB"""
    defaultValue = 0


_DocsIfExt2CmtsCmMscStatusPowerHeadroom_Object = MibTableColumn
docsIfExt2CmtsCmMscStatusPowerHeadroom = _DocsIfExt2CmtsCmMscStatusPowerHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 2, 1, 4),
    _DocsIfExt2CmtsCmMscStatusPowerHeadroom_Type()
)
docsIfExt2CmtsCmMscStatusPowerHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmtsCmMscStatusPowerHeadroom.setStatus("current")
if mibBuilder.loadTexts:
    docsIfExt2CmtsCmMscStatusPowerHeadroom.setUnits("TenthdB")
_DocsIfExt2CmtsCmMscStatusMeasuredSNR_Type = TenthdB
_DocsIfExt2CmtsCmMscStatusMeasuredSNR_Object = MibTableColumn
docsIfExt2CmtsCmMscStatusMeasuredSNR = _DocsIfExt2CmtsCmMscStatusMeasuredSNR_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 2, 1, 5),
    _DocsIfExt2CmtsCmMscStatusMeasuredSNR_Type()
)
docsIfExt2CmtsCmMscStatusMeasuredSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmtsCmMscStatusMeasuredSNR.setStatus("current")
if mibBuilder.loadTexts:
    docsIfExt2CmtsCmMscStatusMeasuredSNR.setUnits("TenthdB")
_DocsIfExt2CmtsCmMscStatusEffectiveSNR_Type = TenthdB
_DocsIfExt2CmtsCmMscStatusEffectiveSNR_Object = MibTableColumn
docsIfExt2CmtsCmMscStatusEffectiveSNR = _DocsIfExt2CmtsCmMscStatusEffectiveSNR_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 2, 1, 6),
    _DocsIfExt2CmtsCmMscStatusEffectiveSNR_Type()
)
docsIfExt2CmtsCmMscStatusEffectiveSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmtsCmMscStatusEffectiveSNR.setStatus("current")
if mibBuilder.loadTexts:
    docsIfExt2CmtsCmMscStatusEffectiveSNR.setUnits("TenthdB")
_DocsIfExt2CmtsUpChannelMscTable_Object = MibTable
docsIfExt2CmtsUpChannelMscTable = _DocsIfExt2CmtsUpChannelMscTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    docsIfExt2CmtsUpChannelMscTable.setStatus("current")
_DocsIfExt2CmtsUpChannelMscEntry_Object = MibTableRow
docsIfExt2CmtsUpChannelMscEntry = _DocsIfExt2CmtsUpChannelMscEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 3, 1)
)
docsIfExt2CmtsUpChannelMscEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfExt2CmtsUpChannelMscEntry.setStatus("current")


class _DocsIfExt2CmtsUpChannelMscState_Type(Integer32):
    """Custom type docsIfExt2CmtsUpChannelMscState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("channelDisabled", 2),
          ("channelEnabled", 1),
          ("dormant", 3))
    )


_DocsIfExt2CmtsUpChannelMscState_Type.__name__ = "Integer32"
_DocsIfExt2CmtsUpChannelMscState_Object = MibTableColumn
docsIfExt2CmtsUpChannelMscState = _DocsIfExt2CmtsUpChannelMscState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 3, 1, 1),
    _DocsIfExt2CmtsUpChannelMscState_Type()
)
docsIfExt2CmtsUpChannelMscState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfExt2CmtsUpChannelMscState.setStatus("current")
_DocsIfExt2CmtsUpChannelMSCTotalCMs_Type = Gauge32
_DocsIfExt2CmtsUpChannelMSCTotalCMs_Object = MibTableColumn
docsIfExt2CmtsUpChannelMSCTotalCMs = _DocsIfExt2CmtsUpChannelMSCTotalCMs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 3, 1, 2),
    _DocsIfExt2CmtsUpChannelMSCTotalCMs_Type()
)
docsIfExt2CmtsUpChannelMSCTotalCMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmtsUpChannelMSCTotalCMs.setStatus("current")


class _DocsIfExt2CmtsUpChannelMSCLimitIUC1_Type(Unsigned32):
    """Custom type docsIfExt2CmtsUpChannelMSCLimitIUC1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DocsIfExt2CmtsUpChannelMSCLimitIUC1_Type.__name__ = "Unsigned32"
_DocsIfExt2CmtsUpChannelMSCLimitIUC1_Object = MibTableColumn
docsIfExt2CmtsUpChannelMSCLimitIUC1 = _DocsIfExt2CmtsUpChannelMSCLimitIUC1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 3, 1, 3),
    _DocsIfExt2CmtsUpChannelMSCLimitIUC1_Type()
)
docsIfExt2CmtsUpChannelMSCLimitIUC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmtsUpChannelMSCLimitIUC1.setStatus("current")
if mibBuilder.loadTexts:
    docsIfExt2CmtsUpChannelMSCLimitIUC1.setUnits("codes")


class _DocsIfExt2CmtsUpChannelMSCMinimumValue_Type(Unsigned32):
    """Custom type docsIfExt2CmtsUpChannelMSCMinimumValue based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_DocsIfExt2CmtsUpChannelMSCMinimumValue_Type.__name__ = "Unsigned32"
_DocsIfExt2CmtsUpChannelMSCMinimumValue_Object = MibTableColumn
docsIfExt2CmtsUpChannelMSCMinimumValue = _DocsIfExt2CmtsUpChannelMSCMinimumValue_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 3, 1, 4),
    _DocsIfExt2CmtsUpChannelMSCMinimumValue_Type()
)
docsIfExt2CmtsUpChannelMSCMinimumValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsIfExt2CmtsUpChannelMSCMinimumValue.setStatus("current")
if mibBuilder.loadTexts:
    docsIfExt2CmtsUpChannelMSCMinimumValue.setUnits("codes")
_DocsIfExt2CmtsUpChannelTable_Object = MibTable
docsIfExt2CmtsUpChannelTable = _DocsIfExt2CmtsUpChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 4)
)
if mibBuilder.loadTexts:
    docsIfExt2CmtsUpChannelTable.setStatus("current")
_DocsIfExt2CmtsUpChannelEntry_Object = MibTableRow
docsIfExt2CmtsUpChannelEntry = _DocsIfExt2CmtsUpChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 4, 1)
)
docsIfExt2CmtsUpChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    docsIfExt2CmtsUpChannelEntry.setStatus("current")
_DocsIfExt2CmtsUpChannelTotalCMs_Type = Gauge32
_DocsIfExt2CmtsUpChannelTotalCMs_Object = MibTableColumn
docsIfExt2CmtsUpChannelTotalCMs = _DocsIfExt2CmtsUpChannelTotalCMs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 1, 3, 4, 1, 1),
    _DocsIfExt2CmtsUpChannelTotalCMs_Type()
)
docsIfExt2CmtsUpChannelTotalCMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfExt2CmtsUpChannelTotalCMs.setStatus("current")
_DocsIfExt2Conformance_ObjectIdentity = ObjectIdentity
docsIfExt2Conformance = _DocsIfExt2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 2)
)
_DocsIfExt2Compliances_ObjectIdentity = ObjectIdentity
docsIfExt2Compliances = _DocsIfExt2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 2, 1)
)
_DocsIfExt2Groups_ObjectIdentity = ObjectIdentity
docsIfExt2Groups = _DocsIfExt2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 2, 2)
)

# Managed Objects groups

docsIfExt2CmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 2, 2, 1)
)
docsIfExt2CmGroup.setObjects(
      *(("DOCS-IFEXT2-MIB", "docsIfExt2CmMscStatusState"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmMscStatusPowerShortfall"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmMscStatusCodeRatio"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmMscStatusMaximumScheduledCodes"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmMscStatusPowerHeadroom"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmMscStatusEffectivePower"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmMscStatusIUC2Control"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmClearLearnedMacAddresses"))
)
if mibBuilder.loadTexts:
    docsIfExt2CmGroup.setStatus("current")

docsIfExt2CmtsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 2, 2, 2)
)
docsIfExt2CmtsGroup.setObjects(
      *(("DOCS-IFEXT2-MIB", "docsIfExt2CmtsMscGlobalEnable"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmtsCmMscStatusPowerShortfall"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmtsCmMscStatusCodeRatio"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmtsCmMscStatusMaximumScheduledCodes"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmtsCmMscStatusPowerHeadroom"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmtsCmMscStatusMeasuredSNR"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmtsCmMscStatusEffectiveSNR"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmtsUpChannelMscState"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmtsUpChannelMSCTotalCMs"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmtsUpChannelMSCLimitIUC1"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmtsUpChannelMSCMinimumValue"),
        ("DOCS-IFEXT2-MIB", "docsIfExt2CmtsUpChannelTotalCMs"))
)
if mibBuilder.loadTexts:
    docsIfExt2CmtsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsIfExt2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsIfExt2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-IFEXT2-MIB",
    **{"docsIfExt2Mib": docsIfExt2Mib,
       "docsIfExt2Notifications": docsIfExt2Notifications,
       "docsIfExt2MibObjects": docsIfExt2MibObjects,
       "docsIfExt2BaseObjects": docsIfExt2BaseObjects,
       "docsIfExt2CmObjects": docsIfExt2CmObjects,
       "docsIfExt2CmMscStatusTable": docsIfExt2CmMscStatusTable,
       "docsIfExt2CmMscStatusEntry": docsIfExt2CmMscStatusEntry,
       "docsIfExt2CmMscStatusState": docsIfExt2CmMscStatusState,
       "docsIfExt2CmMscStatusPowerShortfall": docsIfExt2CmMscStatusPowerShortfall,
       "docsIfExt2CmMscStatusCodeRatio": docsIfExt2CmMscStatusCodeRatio,
       "docsIfExt2CmMscStatusMaximumScheduledCodes": docsIfExt2CmMscStatusMaximumScheduledCodes,
       "docsIfExt2CmMscStatusPowerHeadroom": docsIfExt2CmMscStatusPowerHeadroom,
       "docsIfExt2CmMscStatusEffectivePower": docsIfExt2CmMscStatusEffectivePower,
       "docsIfExt2CmMscStatusIUC2Control": docsIfExt2CmMscStatusIUC2Control,
       "docsIfExt2CmClearLearnedMacAddresses": docsIfExt2CmClearLearnedMacAddresses,
       "docsIfExt2CmtsObjects": docsIfExt2CmtsObjects,
       "docsIfExt2CmtsMscGlobalEnable": docsIfExt2CmtsMscGlobalEnable,
       "docsIfExt2CmtsCmMscStatusTable": docsIfExt2CmtsCmMscStatusTable,
       "docsIfExt2CmtsCmMscStatusEntry": docsIfExt2CmtsCmMscStatusEntry,
       "docsIfExt2CmtsCmMscStatusPowerShortfall": docsIfExt2CmtsCmMscStatusPowerShortfall,
       "docsIfExt2CmtsCmMscStatusCodeRatio": docsIfExt2CmtsCmMscStatusCodeRatio,
       "docsIfExt2CmtsCmMscStatusMaximumScheduledCodes": docsIfExt2CmtsCmMscStatusMaximumScheduledCodes,
       "docsIfExt2CmtsCmMscStatusPowerHeadroom": docsIfExt2CmtsCmMscStatusPowerHeadroom,
       "docsIfExt2CmtsCmMscStatusMeasuredSNR": docsIfExt2CmtsCmMscStatusMeasuredSNR,
       "docsIfExt2CmtsCmMscStatusEffectiveSNR": docsIfExt2CmtsCmMscStatusEffectiveSNR,
       "docsIfExt2CmtsUpChannelMscTable": docsIfExt2CmtsUpChannelMscTable,
       "docsIfExt2CmtsUpChannelMscEntry": docsIfExt2CmtsUpChannelMscEntry,
       "docsIfExt2CmtsUpChannelMscState": docsIfExt2CmtsUpChannelMscState,
       "docsIfExt2CmtsUpChannelMSCTotalCMs": docsIfExt2CmtsUpChannelMSCTotalCMs,
       "docsIfExt2CmtsUpChannelMSCLimitIUC1": docsIfExt2CmtsUpChannelMSCLimitIUC1,
       "docsIfExt2CmtsUpChannelMSCMinimumValue": docsIfExt2CmtsUpChannelMSCMinimumValue,
       "docsIfExt2CmtsUpChannelTable": docsIfExt2CmtsUpChannelTable,
       "docsIfExt2CmtsUpChannelEntry": docsIfExt2CmtsUpChannelEntry,
       "docsIfExt2CmtsUpChannelTotalCMs": docsIfExt2CmtsUpChannelTotalCMs,
       "docsIfExt2Conformance": docsIfExt2Conformance,
       "docsIfExt2Compliances": docsIfExt2Compliances,
       "docsIfExt2Compliance": docsIfExt2Compliance,
       "docsIfExt2Groups": docsIfExt2Groups,
       "docsIfExt2CmGroup": docsIfExt2CmGroup,
       "docsIfExt2CmtsGroup": docsIfExt2CmtsGroup}
)
