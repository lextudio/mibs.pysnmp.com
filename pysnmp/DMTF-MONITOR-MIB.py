# SNMP MIB module (DMTF-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DMTF-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:42 2024
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

(DmiString,
 dmiCompId,
 dmiEventAssociatedGroup,
 dmiEventDateTime,
 dmiEventSeverity,
 dmiEventStateKey,
 dmiEventSubSystem,
 dmiEventSystem) = mibBuilder.importSymbols(
    "DMTF-DMI-MIB",
    "DmiString",
    "dmiCompId",
    "dmiEventAssociatedGroup",
    "dmiEventDateTime",
    "dmiEventSeverity",
    "dmiEventStateKey",
    "dmiEventSubSystem",
    "dmiEventSystem")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

dmtfMonitorMIF = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2, 6)
)


# Types definitions



class DmiCounter(Counter32):
    """Custom type DmiCounter based on Counter32"""




class DmiCounter64(Counter64):
    """Custom type DmiCounter64 based on Counter64"""




class DmiGauge(Gauge32):
    """Custom type DmiGauge based on Gauge32"""




class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiOctetstring(OctetString):
    """Custom type DmiOctetstring based on OctetString"""




class DmiCompId(Integer32):
    """Custom type DmiCompId based on Integer32"""




class DmiGroupId(Integer32):
    """Custom type DmiGroupId based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dmtf_ObjectIdentity = ObjectIdentity
dmtf = _Dmtf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412)
)
_DmtfStdMifs_ObjectIdentity = ObjectIdentity
dmtfStdMifs = _DmtfStdMifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2)
)
_DmtfMonitorAdditionalInformationsTable_Object = MibTable
dmtfMonitorAdditionalInformationsTable = _DmtfMonitorAdditionalInformationsTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 1)
)
if mibBuilder.loadTexts:
    dmtfMonitorAdditionalInformationsTable.setStatus("current")
_DmtfMonitorAdditionalInformationsEntry_Object = MibTableRow
dmtfMonitorAdditionalInformationsEntry = _DmtfMonitorAdditionalInformationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1)
)
dmtfMonitorAdditionalInformationsEntry.setIndexNames(
    (0, "DMTF-MONITOR-MIB", "DmiCompId"),
    (0, "DMTF-MONITOR-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dmtfMonitorAdditionalInformationsEntry.setStatus("current")
_AssetTag_Type = DmiString
_AssetTag_Object = MibTableColumn
assetTag = _AssetTag_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1, 1),
    _AssetTag_Type()
)
assetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    assetTag.setStatus("current")
_MonitorLocation_Type = DmiString
_MonitorLocation_Object = MibTableColumn
monitorLocation = _MonitorLocation_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1, 2),
    _MonitorLocation_Type()
)
monitorLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorLocation.setStatus("current")
_MonitorPrimaryUserName_Type = DmiString
_MonitorPrimaryUserName_Object = MibTableColumn
monitorPrimaryUserName = _MonitorPrimaryUserName_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1, 3),
    _MonitorPrimaryUserName_Type()
)
monitorPrimaryUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorPrimaryUserName.setStatus("current")
_MonitorPrimaryUserPhone_Type = DmiString
_MonitorPrimaryUserPhone_Object = MibTableColumn
monitorPrimaryUserPhone = _MonitorPrimaryUserPhone_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 1, 1, 4),
    _MonitorPrimaryUserPhone_Type()
)
monitorPrimaryUserPhone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorPrimaryUserPhone.setStatus("current")
_DmtfMonitorResolutionsTable_Object = MibTable
dmtfMonitorResolutionsTable = _DmtfMonitorResolutionsTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 2)
)
if mibBuilder.loadTexts:
    dmtfMonitorResolutionsTable.setStatus("current")
_DmtfMonitorResolutionsEntry_Object = MibTableRow
dmtfMonitorResolutionsEntry = _DmtfMonitorResolutionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1)
)
dmtfMonitorResolutionsEntry.setIndexNames(
    (0, "DMTF-MONITOR-MIB", "DmiCompId"),
    (0, "DMTF-MONITOR-MIB", "DmiGroupId"),
    (0, "DMTF-MONITOR-MIB", "monitorResolutionIndex"),
)
if mibBuilder.loadTexts:
    dmtfMonitorResolutionsEntry.setStatus("current")


class _DmtfMonitorResolutionsState_Type(Integer32):
    """Custom type dmtfMonitorResolutionsState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DmtfMonitorResolutionsState_Type.__name__ = "Integer32"
_DmtfMonitorResolutionsState_Object = MibTableColumn
dmtfMonitorResolutionsState = _DmtfMonitorResolutionsState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 0),
    _DmtfMonitorResolutionsState_Type()
)
dmtfMonitorResolutionsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtfMonitorResolutionsState.setStatus("current")
_MonitorResolutionIndex_Type = DmiInteger
_MonitorResolutionIndex_Object = MibTableColumn
monitorResolutionIndex = _MonitorResolutionIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 1),
    _MonitorResolutionIndex_Type()
)
monitorResolutionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorResolutionIndex.setStatus("current")
_HorizontalResolution_Type = DmiInteger
_HorizontalResolution_Object = MibTableColumn
horizontalResolution = _HorizontalResolution_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 2),
    _HorizontalResolution_Type()
)
horizontalResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    horizontalResolution.setStatus("current")
_VerticalResolution_Type = DmiInteger
_VerticalResolution_Object = MibTableColumn
verticalResolution = _VerticalResolution_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 3),
    _VerticalResolution_Type()
)
verticalResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verticalResolution.setStatus("current")
_RefreshRate_Type = DmiInteger
_RefreshRate_Object = MibTableColumn
refreshRate = _RefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 4),
    _RefreshRate_Type()
)
refreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    refreshRate.setStatus("current")


class _VerticalScanMode_Type(Integer32):
    """Custom type verticalScanMode based on Integer32"""
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
        *(("interlaced", 5),
          ("notInterlaced", 4),
          ("other", 1),
          ("unknown", 2),
          ("unsupported", 3))
    )


_VerticalScanMode_Type.__name__ = "Integer32"
_VerticalScanMode_Object = MibTableColumn
verticalScanMode = _VerticalScanMode_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 5),
    _VerticalScanMode_Type()
)
verticalScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verticalScanMode.setStatus("current")
_MinimumMonitorRefreshRate_Type = DmiInteger
_MinimumMonitorRefreshRate_Object = MibTableColumn
minimumMonitorRefreshRate = _MinimumMonitorRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 6),
    _MinimumMonitorRefreshRate_Type()
)
minimumMonitorRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minimumMonitorRefreshRate.setStatus("current")
_MaximumMonitorRefreshRate_Type = DmiInteger
_MaximumMonitorRefreshRate_Object = MibTableColumn
maximumMonitorRefreshRate = _MaximumMonitorRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 6, 2, 1, 7),
    _MaximumMonitorRefreshRate_Type()
)
maximumMonitorRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumMonitorRefreshRate.setStatus("current")
_DmtfDynOids_ObjectIdentity = ObjectIdentity
dmtfDynOids = _DmtfDynOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMTF-MONITOR-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiCounter64": DmiCounter64,
       "DmiGauge": DmiGauge,
       "DmiInteger": DmiInteger,
       "DmiOctetstring": DmiOctetstring,
       "DmiCompId": DmiCompId,
       "DmiGroupId": DmiGroupId,
       "dmtf": dmtf,
       "dmtfStdMifs": dmtfStdMifs,
       "dmtfMonitorMIF": dmtfMonitorMIF,
       "dmtfMonitorAdditionalInformationsTable": dmtfMonitorAdditionalInformationsTable,
       "dmtfMonitorAdditionalInformationsEntry": dmtfMonitorAdditionalInformationsEntry,
       "assetTag": assetTag,
       "monitorLocation": monitorLocation,
       "monitorPrimaryUserName": monitorPrimaryUserName,
       "monitorPrimaryUserPhone": monitorPrimaryUserPhone,
       "dmtfMonitorResolutionsTable": dmtfMonitorResolutionsTable,
       "dmtfMonitorResolutionsEntry": dmtfMonitorResolutionsEntry,
       "dmtfMonitorResolutionsState": dmtfMonitorResolutionsState,
       "monitorResolutionIndex": monitorResolutionIndex,
       "horizontalResolution": horizontalResolution,
       "verticalResolution": verticalResolution,
       "refreshRate": refreshRate,
       "verticalScanMode": verticalScanMode,
       "minimumMonitorRefreshRate": minimumMonitorRefreshRate,
       "maximumMonitorRefreshRate": maximumMonitorRefreshRate,
       "dmtfDynOids": dmtfDynOids}
)
