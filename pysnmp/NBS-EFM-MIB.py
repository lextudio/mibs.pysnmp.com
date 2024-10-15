# SNMP MIB module (NBS-EFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-EFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:46 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(Unsigned16,
 Unsigned64,
 nbs) = mibBuilder.importSymbols(
    "NBS-MIB",
    "Unsigned16",
    "Unsigned64",
    "nbs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nbsEfmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsEfmObjects_ObjectIdentity = ObjectIdentity
nbsEfmObjects = _NbsEfmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300, 1)
)
if mibBuilder.loadTexts:
    nbsEfmObjects.setStatus("current")
_NbsEfmOamGrp_ObjectIdentity = ObjectIdentity
nbsEfmOamGrp = _NbsEfmOamGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3)
)
if mibBuilder.loadTexts:
    nbsEfmOamGrp.setStatus("current")
_NbsEfmOamTable_Object = MibTable
nbsEfmOamTable = _NbsEfmOamTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nbsEfmOamTable.setStatus("current")
_NbsEfmOamEntry_Object = MibTableRow
nbsEfmOamEntry = _NbsEfmOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1)
)
nbsEfmOamEntry.setIndexNames(
    (0, "NBS-EFM-MIB", "nbsEfmPhysicalIfIndex"),
)
if mibBuilder.loadTexts:
    nbsEfmOamEntry.setStatus("current")
_NbsEfmPhysicalIfIndex_Type = InterfaceIndex
_NbsEfmPhysicalIfIndex_Object = MibTableColumn
nbsEfmPhysicalIfIndex = _NbsEfmPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 1),
    _NbsEfmPhysicalIfIndex_Type()
)
nbsEfmPhysicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmPhysicalIfIndex.setStatus("current")
_NbsEfmOamIfIndex_Type = InterfaceIndex
_NbsEfmOamIfIndex_Object = MibTableColumn
nbsEfmOamIfIndex = _NbsEfmOamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 2),
    _NbsEfmOamIfIndex_Type()
)
nbsEfmOamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamIfIndex.setStatus("current")
_NbsEfmOamPeerIfIndex_Type = InterfaceIndex
_NbsEfmOamPeerIfIndex_Object = MibTableColumn
nbsEfmOamPeerIfIndex = _NbsEfmOamPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 3),
    _NbsEfmOamPeerIfIndex_Type()
)
nbsEfmOamPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamPeerIfIndex.setStatus("current")


class _NbsEfmOamMode_Type(Integer32):
    """Custom type nbsEfmOamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("notSupported", 1),
          ("passive", 2))
    )


_NbsEfmOamMode_Type.__name__ = "Integer32"
_NbsEfmOamMode_Object = MibTableColumn
nbsEfmOamMode = _NbsEfmOamMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 4),
    _NbsEfmOamMode_Type()
)
nbsEfmOamMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamMode.setStatus("current")


class _NbsEfmOamCfg_Type(OctetString):
    """Custom type nbsEfmOamCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NbsEfmOamCfg_Type.__name__ = "OctetString"
_NbsEfmOamCfg_Object = MibTableColumn
nbsEfmOamCfg = _NbsEfmOamCfg_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 5),
    _NbsEfmOamCfg_Type()
)
nbsEfmOamCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamCfg.setStatus("current")
_NbsEfmOamPduCfg_Type = Unsigned16
_NbsEfmOamPduCfg_Object = MibTableColumn
nbsEfmOamPduCfg = _NbsEfmOamPduCfg_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 6),
    _NbsEfmOamPduCfg_Type()
)
nbsEfmOamPduCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamPduCfg.setStatus("current")


class _NbsEfmOamFlagsField_Type(OctetString):
    """Custom type nbsEfmOamFlagsField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NbsEfmOamFlagsField_Type.__name__ = "OctetString"
_NbsEfmOamFlagsField_Object = MibTableColumn
nbsEfmOamFlagsField = _NbsEfmOamFlagsField_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 7),
    _NbsEfmOamFlagsField_Type()
)
nbsEfmOamFlagsField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamFlagsField.setStatus("current")


class _NbsEfmOamState_Type(OctetString):
    """Custom type nbsEfmOamState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NbsEfmOamState_Type.__name__ = "OctetString"
_NbsEfmOamState_Object = MibTableColumn
nbsEfmOamState = _NbsEfmOamState_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 8),
    _NbsEfmOamState_Type()
)
nbsEfmOamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamState.setStatus("current")


class _NbsEfmOamVendorOUI_Type(OctetString):
    """Custom type nbsEfmOamVendorOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_NbsEfmOamVendorOUI_Type.__name__ = "OctetString"
_NbsEfmOamVendorOUI_Object = MibTableColumn
nbsEfmOamVendorOUI = _NbsEfmOamVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 9),
    _NbsEfmOamVendorOUI_Type()
)
nbsEfmOamVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamVendorOUI.setStatus("current")
_NbsEfmOamVendorDeviceId_Type = Unsigned16
_NbsEfmOamVendorDeviceId_Object = MibTableColumn
nbsEfmOamVendorDeviceId = _NbsEfmOamVendorDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 10),
    _NbsEfmOamVendorDeviceId_Type()
)
nbsEfmOamVendorDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamVendorDeviceId.setStatus("current")
_NbsEfmOamVendorDeviceVersion_Type = Unsigned16
_NbsEfmOamVendorDeviceVersion_Object = MibTableColumn
nbsEfmOamVendorDeviceVersion = _NbsEfmOamVendorDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 11),
    _NbsEfmOamVendorDeviceVersion_Type()
)
nbsEfmOamVendorDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamVendorDeviceVersion.setStatus("current")
_NbsEfmOamPDUTx_Type = Counter32
_NbsEfmOamPDUTx_Object = MibTableColumn
nbsEfmOamPDUTx = _NbsEfmOamPDUTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 12),
    _NbsEfmOamPDUTx_Type()
)
nbsEfmOamPDUTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamPDUTx.setStatus("current")
_NbsEfmOamPDURx_Type = Counter32
_NbsEfmOamPDURx_Object = MibTableColumn
nbsEfmOamPDURx = _NbsEfmOamPDURx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 13),
    _NbsEfmOamPDURx_Type()
)
nbsEfmOamPDURx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamPDURx.setStatus("current")
_NbsEfmOamUnsupportedCodesRx_Type = Counter32
_NbsEfmOamUnsupportedCodesRx_Object = MibTableColumn
nbsEfmOamUnsupportedCodesRx = _NbsEfmOamUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 14),
    _NbsEfmOamUnsupportedCodesRx_Type()
)
nbsEfmOamUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamUnsupportedCodesRx.setStatus("current")
_NbsEfmOamInformationTx_Type = Counter32
_NbsEfmOamInformationTx_Object = MibTableColumn
nbsEfmOamInformationTx = _NbsEfmOamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 15),
    _NbsEfmOamInformationTx_Type()
)
nbsEfmOamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamInformationTx.setStatus("current")
_NbsEfmOamInformationRx_Type = Counter32
_NbsEfmOamInformationRx_Object = MibTableColumn
nbsEfmOamInformationRx = _NbsEfmOamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 16),
    _NbsEfmOamInformationRx_Type()
)
nbsEfmOamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamInformationRx.setStatus("current")
_NbsEfmOamEventNotificationTx_Type = Counter32
_NbsEfmOamEventNotificationTx_Object = MibTableColumn
nbsEfmOamEventNotificationTx = _NbsEfmOamEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 17),
    _NbsEfmOamEventNotificationTx_Type()
)
nbsEfmOamEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamEventNotificationTx.setStatus("current")
_NbsEfmOamUniEventNotificationRx_Type = Counter32
_NbsEfmOamUniEventNotificationRx_Object = MibTableColumn
nbsEfmOamUniEventNotificationRx = _NbsEfmOamUniEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 18),
    _NbsEfmOamUniEventNotificationRx_Type()
)
nbsEfmOamUniEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamUniEventNotificationRx.setStatus("current")
_NbsEfmOamDupEventNotificationRx_Type = Counter32
_NbsEfmOamDupEventNotificationRx_Object = MibTableColumn
nbsEfmOamDupEventNotificationRx = _NbsEfmOamDupEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 19),
    _NbsEfmOamDupEventNotificationRx_Type()
)
nbsEfmOamDupEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamDupEventNotificationRx.setStatus("current")
_NbsEfmOamLoopbackControlTx_Type = Counter32
_NbsEfmOamLoopbackControlTx_Object = MibTableColumn
nbsEfmOamLoopbackControlTx = _NbsEfmOamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 20),
    _NbsEfmOamLoopbackControlTx_Type()
)
nbsEfmOamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamLoopbackControlTx.setStatus("current")
_NbsEfmOamLoopbackControlRx_Type = Counter32
_NbsEfmOamLoopbackControlRx_Object = MibTableColumn
nbsEfmOamLoopbackControlRx = _NbsEfmOamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 21),
    _NbsEfmOamLoopbackControlRx_Type()
)
nbsEfmOamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamLoopbackControlRx.setStatus("current")
_NbsEfmOamVariableRequestTx_Type = Counter32
_NbsEfmOamVariableRequestTx_Object = MibTableColumn
nbsEfmOamVariableRequestTx = _NbsEfmOamVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 22),
    _NbsEfmOamVariableRequestTx_Type()
)
nbsEfmOamVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamVariableRequestTx.setStatus("current")
_NbsEfmOamVariableRequestRx_Type = Counter32
_NbsEfmOamVariableRequestRx_Object = MibTableColumn
nbsEfmOamVariableRequestRx = _NbsEfmOamVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 23),
    _NbsEfmOamVariableRequestRx_Type()
)
nbsEfmOamVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamVariableRequestRx.setStatus("current")
_NbsEfmOamVariableResponseTx_Type = Counter32
_NbsEfmOamVariableResponseTx_Object = MibTableColumn
nbsEfmOamVariableResponseTx = _NbsEfmOamVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 24),
    _NbsEfmOamVariableResponseTx_Type()
)
nbsEfmOamVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamVariableResponseTx.setStatus("current")
_NbsEfmOamVariableResponseRx_Type = Counter32
_NbsEfmOamVariableResponseRx_Object = MibTableColumn
nbsEfmOamVariableResponseRx = _NbsEfmOamVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 25),
    _NbsEfmOamVariableResponseRx_Type()
)
nbsEfmOamVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamVariableResponseRx.setStatus("current")
_NbsEfmOamOrganizationSpecificTx_Type = Counter32
_NbsEfmOamOrganizationSpecificTx_Object = MibTableColumn
nbsEfmOamOrganizationSpecificTx = _NbsEfmOamOrganizationSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 26),
    _NbsEfmOamOrganizationSpecificTx_Type()
)
nbsEfmOamOrganizationSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamOrganizationSpecificTx.setStatus("current")
_NbsEfmOamOrganizationSpecificRx_Type = Counter32
_NbsEfmOamOrganizationSpecificRx_Object = MibTableColumn
nbsEfmOamOrganizationSpecificRx = _NbsEfmOamOrganizationSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 27),
    _NbsEfmOamOrganizationSpecificRx_Type()
)
nbsEfmOamOrganizationSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamOrganizationSpecificRx.setStatus("current")
_NbsEfmOamErrSymPerCfgDuration_Type = Unsigned64
_NbsEfmOamErrSymPerCfgDuration_Object = MibTableColumn
nbsEfmOamErrSymPerCfgDuration = _NbsEfmOamErrSymPerCfgDuration_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 28),
    _NbsEfmOamErrSymPerCfgDuration_Type()
)
nbsEfmOamErrSymPerCfgDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrSymPerCfgDuration.setStatus("current")
_NbsEfmOamErrSymPerCfgThreshld_Type = Unsigned32
_NbsEfmOamErrSymPerCfgThreshld_Object = MibTableColumn
nbsEfmOamErrSymPerCfgThreshld = _NbsEfmOamErrSymPerCfgThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 29),
    _NbsEfmOamErrSymPerCfgThreshld_Type()
)
nbsEfmOamErrSymPerCfgThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrSymPerCfgThreshld.setStatus("current")
_NbsEfmOamErrSymPerEvtTime_Type = Unsigned16
_NbsEfmOamErrSymPerEvtTime_Object = MibTableColumn
nbsEfmOamErrSymPerEvtTime = _NbsEfmOamErrSymPerEvtTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 30),
    _NbsEfmOamErrSymPerEvtTime_Type()
)
nbsEfmOamErrSymPerEvtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrSymPerEvtTime.setStatus("current")
_NbsEfmOamErrSymPerEvtWindow_Type = Unsigned64
_NbsEfmOamErrSymPerEvtWindow_Object = MibTableColumn
nbsEfmOamErrSymPerEvtWindow = _NbsEfmOamErrSymPerEvtWindow_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 31),
    _NbsEfmOamErrSymPerEvtWindow_Type()
)
nbsEfmOamErrSymPerEvtWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrSymPerEvtWindow.setStatus("current")
_NbsEfmOamErrSymPerEvtThreshld_Type = Unsigned64
_NbsEfmOamErrSymPerEvtThreshld_Object = MibTableColumn
nbsEfmOamErrSymPerEvtThreshld = _NbsEfmOamErrSymPerEvtThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 32),
    _NbsEfmOamErrSymPerEvtThreshld_Type()
)
nbsEfmOamErrSymPerEvtThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrSymPerEvtThreshld.setStatus("current")
_NbsEfmOamErrSymPerEvtCount_Type = Counter64
_NbsEfmOamErrSymPerEvtCount_Object = MibTableColumn
nbsEfmOamErrSymPerEvtCount = _NbsEfmOamErrSymPerEvtCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 33),
    _NbsEfmOamErrSymPerEvtCount_Type()
)
nbsEfmOamErrSymPerEvtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrSymPerEvtCount.setStatus("current")
_NbsEfmOamErrFrmCfgDuration_Type = Unsigned32
_NbsEfmOamErrFrmCfgDuration_Object = MibTableColumn
nbsEfmOamErrFrmCfgDuration = _NbsEfmOamErrFrmCfgDuration_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 34),
    _NbsEfmOamErrFrmCfgDuration_Type()
)
nbsEfmOamErrFrmCfgDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmCfgDuration.setStatus("current")
_NbsEfmOamErrFrmCfgThreshld_Type = Unsigned32
_NbsEfmOamErrFrmCfgThreshld_Object = MibTableColumn
nbsEfmOamErrFrmCfgThreshld = _NbsEfmOamErrFrmCfgThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 35),
    _NbsEfmOamErrFrmCfgThreshld_Type()
)
nbsEfmOamErrFrmCfgThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmCfgThreshld.setStatus("current")
_NbsEfmOamErrFrmEvtTime_Type = Unsigned16
_NbsEfmOamErrFrmEvtTime_Object = MibTableColumn
nbsEfmOamErrFrmEvtTime = _NbsEfmOamErrFrmEvtTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 36),
    _NbsEfmOamErrFrmEvtTime_Type()
)
nbsEfmOamErrFrmEvtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmEvtTime.setStatus("current")
_NbsEfmOamErrFrmEvtWindow_Type = Unsigned16
_NbsEfmOamErrFrmEvtWindow_Object = MibTableColumn
nbsEfmOamErrFrmEvtWindow = _NbsEfmOamErrFrmEvtWindow_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 37),
    _NbsEfmOamErrFrmEvtWindow_Type()
)
nbsEfmOamErrFrmEvtWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmEvtWindow.setStatus("current")
_NbsEfmOamErrFrmEvtThreshld_Type = Unsigned32
_NbsEfmOamErrFrmEvtThreshld_Object = MibTableColumn
nbsEfmOamErrFrmEvtThreshld = _NbsEfmOamErrFrmEvtThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 38),
    _NbsEfmOamErrFrmEvtThreshld_Type()
)
nbsEfmOamErrFrmEvtThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmEvtThreshld.setStatus("current")
_NbsEfmOamErrFrmEvtCount_Type = Counter64
_NbsEfmOamErrFrmEvtCount_Object = MibTableColumn
nbsEfmOamErrFrmEvtCount = _NbsEfmOamErrFrmEvtCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 39),
    _NbsEfmOamErrFrmEvtCount_Type()
)
nbsEfmOamErrFrmEvtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmEvtCount.setStatus("current")
_NbsEfmOamErrFrmPerCfgDuration_Type = Unsigned32
_NbsEfmOamErrFrmPerCfgDuration_Object = MibTableColumn
nbsEfmOamErrFrmPerCfgDuration = _NbsEfmOamErrFrmPerCfgDuration_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 40),
    _NbsEfmOamErrFrmPerCfgDuration_Type()
)
nbsEfmOamErrFrmPerCfgDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmPerCfgDuration.setStatus("current")
_NbsEfmOamErrFrmPerCfgThreshld_Type = Unsigned32
_NbsEfmOamErrFrmPerCfgThreshld_Object = MibTableColumn
nbsEfmOamErrFrmPerCfgThreshld = _NbsEfmOamErrFrmPerCfgThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 41),
    _NbsEfmOamErrFrmPerCfgThreshld_Type()
)
nbsEfmOamErrFrmPerCfgThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmPerCfgThreshld.setStatus("current")
_NbsEfmOamErrFrmPerEvtTime_Type = Unsigned16
_NbsEfmOamErrFrmPerEvtTime_Object = MibTableColumn
nbsEfmOamErrFrmPerEvtTime = _NbsEfmOamErrFrmPerEvtTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 42),
    _NbsEfmOamErrFrmPerEvtTime_Type()
)
nbsEfmOamErrFrmPerEvtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmPerEvtTime.setStatus("current")
_NbsEfmOamErrFrmPerEvtWindow_Type = Unsigned32
_NbsEfmOamErrFrmPerEvtWindow_Object = MibTableColumn
nbsEfmOamErrFrmPerEvtWindow = _NbsEfmOamErrFrmPerEvtWindow_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 43),
    _NbsEfmOamErrFrmPerEvtWindow_Type()
)
nbsEfmOamErrFrmPerEvtWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmPerEvtWindow.setStatus("current")
_NbsEfmOamErrFrmPerEvtThreshld_Type = Unsigned32
_NbsEfmOamErrFrmPerEvtThreshld_Object = MibTableColumn
nbsEfmOamErrFrmPerEvtThreshld = _NbsEfmOamErrFrmPerEvtThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 44),
    _NbsEfmOamErrFrmPerEvtThreshld_Type()
)
nbsEfmOamErrFrmPerEvtThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmPerEvtThreshld.setStatus("current")
_NbsEfmOamErrFrmPerEvtCount_Type = Counter64
_NbsEfmOamErrFrmPerEvtCount_Object = MibTableColumn
nbsEfmOamErrFrmPerEvtCount = _NbsEfmOamErrFrmPerEvtCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 45),
    _NbsEfmOamErrFrmPerEvtCount_Type()
)
nbsEfmOamErrFrmPerEvtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmPerEvtCount.setStatus("current")
_NbsEfmOamErrFrmSecSumCfgDuration_Type = Unsigned16
_NbsEfmOamErrFrmSecSumCfgDuration_Object = MibTableColumn
nbsEfmOamErrFrmSecSumCfgDuration = _NbsEfmOamErrFrmSecSumCfgDuration_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 46),
    _NbsEfmOamErrFrmSecSumCfgDuration_Type()
)
nbsEfmOamErrFrmSecSumCfgDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmSecSumCfgDuration.setStatus("current")
_NbsEfmOamErrFrmSecSumCfgThreshld_Type = Unsigned16
_NbsEfmOamErrFrmSecSumCfgThreshld_Object = MibTableColumn
nbsEfmOamErrFrmSecSumCfgThreshld = _NbsEfmOamErrFrmSecSumCfgThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 47),
    _NbsEfmOamErrFrmSecSumCfgThreshld_Type()
)
nbsEfmOamErrFrmSecSumCfgThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmSecSumCfgThreshld.setStatus("current")
_NbsEfmOamErrFrmSecSumEvtTime_Type = Unsigned16
_NbsEfmOamErrFrmSecSumEvtTime_Object = MibTableColumn
nbsEfmOamErrFrmSecSumEvtTime = _NbsEfmOamErrFrmSecSumEvtTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 48),
    _NbsEfmOamErrFrmSecSumEvtTime_Type()
)
nbsEfmOamErrFrmSecSumEvtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmSecSumEvtTime.setStatus("current")
_NbsEfmOamErrFrmSecSumEvtWindow_Type = Unsigned16
_NbsEfmOamErrFrmSecSumEvtWindow_Object = MibTableColumn
nbsEfmOamErrFrmSecSumEvtWindow = _NbsEfmOamErrFrmSecSumEvtWindow_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 49),
    _NbsEfmOamErrFrmSecSumEvtWindow_Type()
)
nbsEfmOamErrFrmSecSumEvtWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmSecSumEvtWindow.setStatus("current")
_NbsEfmOamErrFrmSecSumEvtThreshld_Type = Unsigned16
_NbsEfmOamErrFrmSecSumEvtThreshld_Object = MibTableColumn
nbsEfmOamErrFrmSecSumEvtThreshld = _NbsEfmOamErrFrmSecSumEvtThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 50),
    _NbsEfmOamErrFrmSecSumEvtThreshld_Type()
)
nbsEfmOamErrFrmSecSumEvtThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmSecSumEvtThreshld.setStatus("current")
_NbsEfmOamErrFrmSecSumEvtCount_Type = Counter32
_NbsEfmOamErrFrmSecSumEvtCount_Object = MibTableColumn
nbsEfmOamErrFrmSecSumEvtCount = _NbsEfmOamErrFrmSecSumEvtCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 51),
    _NbsEfmOamErrFrmSecSumEvtCount_Type()
)
nbsEfmOamErrFrmSecSumEvtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamErrFrmSecSumEvtCount.setStatus("current")
_NbsEfmOamFramesLostDueToOamError_Type = Counter32
_NbsEfmOamFramesLostDueToOamError_Object = MibTableColumn
nbsEfmOamFramesLostDueToOamError = _NbsEfmOamFramesLostDueToOamError_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 52),
    _NbsEfmOamFramesLostDueToOamError_Type()
)
nbsEfmOamFramesLostDueToOamError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamFramesLostDueToOamError.setStatus("current")


class _NbsEfmOamAdminState_Type(Integer32):
    """Custom type nbsEfmOamAdminState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("notSupported", 1))
    )


_NbsEfmOamAdminState_Type.__name__ = "Integer32"
_NbsEfmOamAdminState_Object = MibTableColumn
nbsEfmOamAdminState = _NbsEfmOamAdminState_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 53),
    _NbsEfmOamAdminState_Type()
)
nbsEfmOamAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsEfmOamAdminState.setStatus("current")


class _NbsEfmOamOperState_Type(OctetString):
    """Custom type nbsEfmOamOperState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NbsEfmOamOperState_Type.__name__ = "OctetString"
_NbsEfmOamOperState_Object = MibTableColumn
nbsEfmOamOperState = _NbsEfmOamOperState_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 54),
    _NbsEfmOamOperState_Type()
)
nbsEfmOamOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsEfmOamOperState.setStatus("current")
_NbsEfmProduct_ObjectIdentity = ObjectIdentity
nbsEfmProduct = _NbsEfmProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300, 2)
)
_NbsEfmNc316Nm_ObjectIdentity = ObjectIdentity
nbsEfmNc316Nm = _NbsEfmNc316Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300, 2, 1)
)
_NbsEfmConformance_ObjectIdentity = ObjectIdentity
nbsEfmConformance = _NbsEfmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300, 3)
)
_NbsEfmGroups_ObjectIdentity = ObjectIdentity
nbsEfmGroups = _NbsEfmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300, 3, 1)
)

# Managed Objects groups

nbsEfmOamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 300, 3, 1, 3)
)
nbsEfmOamGroup.setObjects(
      *(("NBS-EFM-MIB", "nbsEfmPhysicalIfIndex"),
        ("NBS-EFM-MIB", "nbsEfmOamIfIndex"),
        ("NBS-EFM-MIB", "nbsEfmOamPeerIfIndex"),
        ("NBS-EFM-MIB", "nbsEfmOamMode"),
        ("NBS-EFM-MIB", "nbsEfmOamCfg"),
        ("NBS-EFM-MIB", "nbsEfmOamPduCfg"),
        ("NBS-EFM-MIB", "nbsEfmOamFlagsField"),
        ("NBS-EFM-MIB", "nbsEfmOamState"),
        ("NBS-EFM-MIB", "nbsEfmOamVendorOUI"),
        ("NBS-EFM-MIB", "nbsEfmOamVendorDeviceId"),
        ("NBS-EFM-MIB", "nbsEfmOamVendorDeviceVersion"),
        ("NBS-EFM-MIB", "nbsEfmOamPDUTx"),
        ("NBS-EFM-MIB", "nbsEfmOamPDURx"),
        ("NBS-EFM-MIB", "nbsEfmOamUnsupportedCodesRx"),
        ("NBS-EFM-MIB", "nbsEfmOamInformationTx"),
        ("NBS-EFM-MIB", "nbsEfmOamInformationRx"),
        ("NBS-EFM-MIB", "nbsEfmOamEventNotificationTx"),
        ("NBS-EFM-MIB", "nbsEfmOamUniEventNotificationRx"),
        ("NBS-EFM-MIB", "nbsEfmOamDupEventNotificationRx"),
        ("NBS-EFM-MIB", "nbsEfmOamLoopbackControlTx"),
        ("NBS-EFM-MIB", "nbsEfmOamLoopbackControlRx"),
        ("NBS-EFM-MIB", "nbsEfmOamVariableRequestTx"),
        ("NBS-EFM-MIB", "nbsEfmOamVariableRequestRx"),
        ("NBS-EFM-MIB", "nbsEfmOamVariableResponseTx"),
        ("NBS-EFM-MIB", "nbsEfmOamVariableResponseRx"),
        ("NBS-EFM-MIB", "nbsEfmOamOrganizationSpecificTx"),
        ("NBS-EFM-MIB", "nbsEfmOamOrganizationSpecificRx"),
        ("NBS-EFM-MIB", "nbsEfmOamErrSymPerCfgDuration"),
        ("NBS-EFM-MIB", "nbsEfmOamErrSymPerCfgThreshld"),
        ("NBS-EFM-MIB", "nbsEfmOamErrSymPerEvtTime"),
        ("NBS-EFM-MIB", "nbsEfmOamErrSymPerEvtWindow"),
        ("NBS-EFM-MIB", "nbsEfmOamErrSymPerEvtThreshld"),
        ("NBS-EFM-MIB", "nbsEfmOamErrSymPerEvtCount"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmCfgDuration"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmCfgThreshld"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmEvtTime"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmEvtWindow"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmEvtThreshld"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmEvtCount"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmPerCfgDuration"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmPerCfgThreshld"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmPerEvtTime"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmPerEvtWindow"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmPerEvtThreshld"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmPerEvtCount"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmSecSumCfgDuration"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmSecSumCfgThreshld"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmSecSumEvtTime"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmSecSumEvtWindow"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmSecSumEvtThreshld"),
        ("NBS-EFM-MIB", "nbsEfmOamErrFrmSecSumEvtCount"),
        ("NBS-EFM-MIB", "nbsEfmOamFramesLostDueToOamError"),
        ("NBS-EFM-MIB", "nbsEfmOamAdminState"),
        ("NBS-EFM-MIB", "nbsEfmOamOperState"))
)
if mibBuilder.loadTexts:
    nbsEfmOamGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-EFM-MIB",
    **{"nbsEfmMib": nbsEfmMib,
       "nbsEfmObjects": nbsEfmObjects,
       "nbsEfmOamGrp": nbsEfmOamGrp,
       "nbsEfmOamTable": nbsEfmOamTable,
       "nbsEfmOamEntry": nbsEfmOamEntry,
       "nbsEfmPhysicalIfIndex": nbsEfmPhysicalIfIndex,
       "nbsEfmOamIfIndex": nbsEfmOamIfIndex,
       "nbsEfmOamPeerIfIndex": nbsEfmOamPeerIfIndex,
       "nbsEfmOamMode": nbsEfmOamMode,
       "nbsEfmOamCfg": nbsEfmOamCfg,
       "nbsEfmOamPduCfg": nbsEfmOamPduCfg,
       "nbsEfmOamFlagsField": nbsEfmOamFlagsField,
       "nbsEfmOamState": nbsEfmOamState,
       "nbsEfmOamVendorOUI": nbsEfmOamVendorOUI,
       "nbsEfmOamVendorDeviceId": nbsEfmOamVendorDeviceId,
       "nbsEfmOamVendorDeviceVersion": nbsEfmOamVendorDeviceVersion,
       "nbsEfmOamPDUTx": nbsEfmOamPDUTx,
       "nbsEfmOamPDURx": nbsEfmOamPDURx,
       "nbsEfmOamUnsupportedCodesRx": nbsEfmOamUnsupportedCodesRx,
       "nbsEfmOamInformationTx": nbsEfmOamInformationTx,
       "nbsEfmOamInformationRx": nbsEfmOamInformationRx,
       "nbsEfmOamEventNotificationTx": nbsEfmOamEventNotificationTx,
       "nbsEfmOamUniEventNotificationRx": nbsEfmOamUniEventNotificationRx,
       "nbsEfmOamDupEventNotificationRx": nbsEfmOamDupEventNotificationRx,
       "nbsEfmOamLoopbackControlTx": nbsEfmOamLoopbackControlTx,
       "nbsEfmOamLoopbackControlRx": nbsEfmOamLoopbackControlRx,
       "nbsEfmOamVariableRequestTx": nbsEfmOamVariableRequestTx,
       "nbsEfmOamVariableRequestRx": nbsEfmOamVariableRequestRx,
       "nbsEfmOamVariableResponseTx": nbsEfmOamVariableResponseTx,
       "nbsEfmOamVariableResponseRx": nbsEfmOamVariableResponseRx,
       "nbsEfmOamOrganizationSpecificTx": nbsEfmOamOrganizationSpecificTx,
       "nbsEfmOamOrganizationSpecificRx": nbsEfmOamOrganizationSpecificRx,
       "nbsEfmOamErrSymPerCfgDuration": nbsEfmOamErrSymPerCfgDuration,
       "nbsEfmOamErrSymPerCfgThreshld": nbsEfmOamErrSymPerCfgThreshld,
       "nbsEfmOamErrSymPerEvtTime": nbsEfmOamErrSymPerEvtTime,
       "nbsEfmOamErrSymPerEvtWindow": nbsEfmOamErrSymPerEvtWindow,
       "nbsEfmOamErrSymPerEvtThreshld": nbsEfmOamErrSymPerEvtThreshld,
       "nbsEfmOamErrSymPerEvtCount": nbsEfmOamErrSymPerEvtCount,
       "nbsEfmOamErrFrmCfgDuration": nbsEfmOamErrFrmCfgDuration,
       "nbsEfmOamErrFrmCfgThreshld": nbsEfmOamErrFrmCfgThreshld,
       "nbsEfmOamErrFrmEvtTime": nbsEfmOamErrFrmEvtTime,
       "nbsEfmOamErrFrmEvtWindow": nbsEfmOamErrFrmEvtWindow,
       "nbsEfmOamErrFrmEvtThreshld": nbsEfmOamErrFrmEvtThreshld,
       "nbsEfmOamErrFrmEvtCount": nbsEfmOamErrFrmEvtCount,
       "nbsEfmOamErrFrmPerCfgDuration": nbsEfmOamErrFrmPerCfgDuration,
       "nbsEfmOamErrFrmPerCfgThreshld": nbsEfmOamErrFrmPerCfgThreshld,
       "nbsEfmOamErrFrmPerEvtTime": nbsEfmOamErrFrmPerEvtTime,
       "nbsEfmOamErrFrmPerEvtWindow": nbsEfmOamErrFrmPerEvtWindow,
       "nbsEfmOamErrFrmPerEvtThreshld": nbsEfmOamErrFrmPerEvtThreshld,
       "nbsEfmOamErrFrmPerEvtCount": nbsEfmOamErrFrmPerEvtCount,
       "nbsEfmOamErrFrmSecSumCfgDuration": nbsEfmOamErrFrmSecSumCfgDuration,
       "nbsEfmOamErrFrmSecSumCfgThreshld": nbsEfmOamErrFrmSecSumCfgThreshld,
       "nbsEfmOamErrFrmSecSumEvtTime": nbsEfmOamErrFrmSecSumEvtTime,
       "nbsEfmOamErrFrmSecSumEvtWindow": nbsEfmOamErrFrmSecSumEvtWindow,
       "nbsEfmOamErrFrmSecSumEvtThreshld": nbsEfmOamErrFrmSecSumEvtThreshld,
       "nbsEfmOamErrFrmSecSumEvtCount": nbsEfmOamErrFrmSecSumEvtCount,
       "nbsEfmOamFramesLostDueToOamError": nbsEfmOamFramesLostDueToOamError,
       "nbsEfmOamAdminState": nbsEfmOamAdminState,
       "nbsEfmOamOperState": nbsEfmOamOperState,
       "nbsEfmProduct": nbsEfmProduct,
       "nbsEfmNc316Nm": nbsEfmNc316Nm,
       "nbsEfmConformance": nbsEfmConformance,
       "nbsEfmGroups": nbsEfmGroups,
       "nbsEfmOamGroup": nbsEfmOamGroup}
)
