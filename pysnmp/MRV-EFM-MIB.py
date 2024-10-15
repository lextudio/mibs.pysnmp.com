# SNMP MIB module (MRV-EFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-EFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:33 2024
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
 nbs) = mibBuilder.importSymbols(
    "NBS-CMMC-MIB",
    "InterfaceIndex",
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

mrvEfmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Unsigned16(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class Unsigned64(Counter64, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_MrvEfmObjects_ObjectIdentity = ObjectIdentity
mrvEfmObjects = _MrvEfmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300, 1)
)
if mibBuilder.loadTexts:
    mrvEfmObjects.setStatus("current")
_MrvEfmOamGrp_ObjectIdentity = ObjectIdentity
mrvEfmOamGrp = _MrvEfmOamGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3)
)
if mibBuilder.loadTexts:
    mrvEfmOamGrp.setStatus("current")
_MrvEfmOamTable_Object = MibTable
mrvEfmOamTable = _MrvEfmOamTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mrvEfmOamTable.setStatus("current")
_MrvEfmOamEntry_Object = MibTableRow
mrvEfmOamEntry = _MrvEfmOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1)
)
mrvEfmOamEntry.setIndexNames(
    (0, "MRV-EFM-MIB", "mrvEfmPhysicalIfIndex"),
)
if mibBuilder.loadTexts:
    mrvEfmOamEntry.setStatus("current")
_MrvEfmPhysicalIfIndex_Type = InterfaceIndex
_MrvEfmPhysicalIfIndex_Object = MibTableColumn
mrvEfmPhysicalIfIndex = _MrvEfmPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 1),
    _MrvEfmPhysicalIfIndex_Type()
)
mrvEfmPhysicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmPhysicalIfIndex.setStatus("current")
_MrvEfmOamIfIndex_Type = InterfaceIndex
_MrvEfmOamIfIndex_Object = MibTableColumn
mrvEfmOamIfIndex = _MrvEfmOamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 2),
    _MrvEfmOamIfIndex_Type()
)
mrvEfmOamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamIfIndex.setStatus("current")
_MrvEfmOamPeerIfIndex_Type = InterfaceIndex
_MrvEfmOamPeerIfIndex_Object = MibTableColumn
mrvEfmOamPeerIfIndex = _MrvEfmOamPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 3),
    _MrvEfmOamPeerIfIndex_Type()
)
mrvEfmOamPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamPeerIfIndex.setStatus("current")


class _MrvEfmOamMode_Type(Integer32):
    """Custom type mrvEfmOamMode based on Integer32"""
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


_MrvEfmOamMode_Type.__name__ = "Integer32"
_MrvEfmOamMode_Object = MibTableColumn
mrvEfmOamMode = _MrvEfmOamMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 4),
    _MrvEfmOamMode_Type()
)
mrvEfmOamMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamMode.setStatus("current")


class _MrvEfmOamCfg_Type(OctetString):
    """Custom type mrvEfmOamCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MrvEfmOamCfg_Type.__name__ = "OctetString"
_MrvEfmOamCfg_Object = MibTableColumn
mrvEfmOamCfg = _MrvEfmOamCfg_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 5),
    _MrvEfmOamCfg_Type()
)
mrvEfmOamCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamCfg.setStatus("current")
_MrvEfmOamPduCfg_Type = Unsigned16
_MrvEfmOamPduCfg_Object = MibTableColumn
mrvEfmOamPduCfg = _MrvEfmOamPduCfg_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 6),
    _MrvEfmOamPduCfg_Type()
)
mrvEfmOamPduCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamPduCfg.setStatus("current")


class _MrvEfmOamFlagsField_Type(OctetString):
    """Custom type mrvEfmOamFlagsField based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MrvEfmOamFlagsField_Type.__name__ = "OctetString"
_MrvEfmOamFlagsField_Object = MibTableColumn
mrvEfmOamFlagsField = _MrvEfmOamFlagsField_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 7),
    _MrvEfmOamFlagsField_Type()
)
mrvEfmOamFlagsField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamFlagsField.setStatus("current")


class _MrvEfmOamState_Type(OctetString):
    """Custom type mrvEfmOamState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MrvEfmOamState_Type.__name__ = "OctetString"
_MrvEfmOamState_Object = MibTableColumn
mrvEfmOamState = _MrvEfmOamState_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 8),
    _MrvEfmOamState_Type()
)
mrvEfmOamState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamState.setStatus("current")


class _MrvEfmOamVendorOUI_Type(OctetString):
    """Custom type mrvEfmOamVendorOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_MrvEfmOamVendorOUI_Type.__name__ = "OctetString"
_MrvEfmOamVendorOUI_Object = MibTableColumn
mrvEfmOamVendorOUI = _MrvEfmOamVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 9),
    _MrvEfmOamVendorOUI_Type()
)
mrvEfmOamVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamVendorOUI.setStatus("current")
_MrvEfmOamVendorDeviceId_Type = Unsigned16
_MrvEfmOamVendorDeviceId_Object = MibTableColumn
mrvEfmOamVendorDeviceId = _MrvEfmOamVendorDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 10),
    _MrvEfmOamVendorDeviceId_Type()
)
mrvEfmOamVendorDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamVendorDeviceId.setStatus("current")
_MrvEfmOamVendorDeviceVersion_Type = Unsigned16
_MrvEfmOamVendorDeviceVersion_Object = MibTableColumn
mrvEfmOamVendorDeviceVersion = _MrvEfmOamVendorDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 11),
    _MrvEfmOamVendorDeviceVersion_Type()
)
mrvEfmOamVendorDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamVendorDeviceVersion.setStatus("current")
_MrvEfmOamPDUTx_Type = Counter32
_MrvEfmOamPDUTx_Object = MibTableColumn
mrvEfmOamPDUTx = _MrvEfmOamPDUTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 12),
    _MrvEfmOamPDUTx_Type()
)
mrvEfmOamPDUTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamPDUTx.setStatus("current")
_MrvEfmOamPDURx_Type = Counter32
_MrvEfmOamPDURx_Object = MibTableColumn
mrvEfmOamPDURx = _MrvEfmOamPDURx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 13),
    _MrvEfmOamPDURx_Type()
)
mrvEfmOamPDURx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamPDURx.setStatus("current")
_MrvEfmOamUnsupportedCodesRx_Type = Counter32
_MrvEfmOamUnsupportedCodesRx_Object = MibTableColumn
mrvEfmOamUnsupportedCodesRx = _MrvEfmOamUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 14),
    _MrvEfmOamUnsupportedCodesRx_Type()
)
mrvEfmOamUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamUnsupportedCodesRx.setStatus("current")
_MrvEfmOamInformationTx_Type = Counter32
_MrvEfmOamInformationTx_Object = MibTableColumn
mrvEfmOamInformationTx = _MrvEfmOamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 15),
    _MrvEfmOamInformationTx_Type()
)
mrvEfmOamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamInformationTx.setStatus("current")
_MrvEfmOamInformationRx_Type = Counter32
_MrvEfmOamInformationRx_Object = MibTableColumn
mrvEfmOamInformationRx = _MrvEfmOamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 16),
    _MrvEfmOamInformationRx_Type()
)
mrvEfmOamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamInformationRx.setStatus("current")
_MrvEfmOamEventNotificationTx_Type = Counter32
_MrvEfmOamEventNotificationTx_Object = MibTableColumn
mrvEfmOamEventNotificationTx = _MrvEfmOamEventNotificationTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 17),
    _MrvEfmOamEventNotificationTx_Type()
)
mrvEfmOamEventNotificationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamEventNotificationTx.setStatus("current")
_MrvEfmOamUniEventNotificationRx_Type = Counter32
_MrvEfmOamUniEventNotificationRx_Object = MibTableColumn
mrvEfmOamUniEventNotificationRx = _MrvEfmOamUniEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 18),
    _MrvEfmOamUniEventNotificationRx_Type()
)
mrvEfmOamUniEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamUniEventNotificationRx.setStatus("current")
_MrvEfmOamDupEventNotificationRx_Type = Counter32
_MrvEfmOamDupEventNotificationRx_Object = MibTableColumn
mrvEfmOamDupEventNotificationRx = _MrvEfmOamDupEventNotificationRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 19),
    _MrvEfmOamDupEventNotificationRx_Type()
)
mrvEfmOamDupEventNotificationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamDupEventNotificationRx.setStatus("current")
_MrvEfmOamLoopbackControlTx_Type = Counter32
_MrvEfmOamLoopbackControlTx_Object = MibTableColumn
mrvEfmOamLoopbackControlTx = _MrvEfmOamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 20),
    _MrvEfmOamLoopbackControlTx_Type()
)
mrvEfmOamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamLoopbackControlTx.setStatus("current")
_MrvEfmOamLoopbackControlRx_Type = Counter32
_MrvEfmOamLoopbackControlRx_Object = MibTableColumn
mrvEfmOamLoopbackControlRx = _MrvEfmOamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 21),
    _MrvEfmOamLoopbackControlRx_Type()
)
mrvEfmOamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamLoopbackControlRx.setStatus("current")
_MrvEfmOamVariableRequestTx_Type = Counter32
_MrvEfmOamVariableRequestTx_Object = MibTableColumn
mrvEfmOamVariableRequestTx = _MrvEfmOamVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 22),
    _MrvEfmOamVariableRequestTx_Type()
)
mrvEfmOamVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamVariableRequestTx.setStatus("current")
_MrvEfmOamVariableRequestRx_Type = Counter32
_MrvEfmOamVariableRequestRx_Object = MibTableColumn
mrvEfmOamVariableRequestRx = _MrvEfmOamVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 23),
    _MrvEfmOamVariableRequestRx_Type()
)
mrvEfmOamVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamVariableRequestRx.setStatus("current")
_MrvEfmOamVariableResponseTx_Type = Counter32
_MrvEfmOamVariableResponseTx_Object = MibTableColumn
mrvEfmOamVariableResponseTx = _MrvEfmOamVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 24),
    _MrvEfmOamVariableResponseTx_Type()
)
mrvEfmOamVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamVariableResponseTx.setStatus("current")
_MrvEfmOamVariableResponseRx_Type = Counter32
_MrvEfmOamVariableResponseRx_Object = MibTableColumn
mrvEfmOamVariableResponseRx = _MrvEfmOamVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 25),
    _MrvEfmOamVariableResponseRx_Type()
)
mrvEfmOamVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamVariableResponseRx.setStatus("current")
_MrvEfmOamOrganizationSpecificTx_Type = Counter32
_MrvEfmOamOrganizationSpecificTx_Object = MibTableColumn
mrvEfmOamOrganizationSpecificTx = _MrvEfmOamOrganizationSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 26),
    _MrvEfmOamOrganizationSpecificTx_Type()
)
mrvEfmOamOrganizationSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamOrganizationSpecificTx.setStatus("current")
_MrvEfmOamOrganizationSpecificRx_Type = Counter32
_MrvEfmOamOrganizationSpecificRx_Object = MibTableColumn
mrvEfmOamOrganizationSpecificRx = _MrvEfmOamOrganizationSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 27),
    _MrvEfmOamOrganizationSpecificRx_Type()
)
mrvEfmOamOrganizationSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamOrganizationSpecificRx.setStatus("current")
_MrvEfmOamErrSymPerCfgDuration_Type = Unsigned64
_MrvEfmOamErrSymPerCfgDuration_Object = MibTableColumn
mrvEfmOamErrSymPerCfgDuration = _MrvEfmOamErrSymPerCfgDuration_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 28),
    _MrvEfmOamErrSymPerCfgDuration_Type()
)
mrvEfmOamErrSymPerCfgDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrSymPerCfgDuration.setStatus("current")
_MrvEfmOamErrSymPerCfgThreshld_Type = Unsigned32
_MrvEfmOamErrSymPerCfgThreshld_Object = MibTableColumn
mrvEfmOamErrSymPerCfgThreshld = _MrvEfmOamErrSymPerCfgThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 29),
    _MrvEfmOamErrSymPerCfgThreshld_Type()
)
mrvEfmOamErrSymPerCfgThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrSymPerCfgThreshld.setStatus("current")
_MrvEfmOamErrSymPerEvtTime_Type = Unsigned16
_MrvEfmOamErrSymPerEvtTime_Object = MibTableColumn
mrvEfmOamErrSymPerEvtTime = _MrvEfmOamErrSymPerEvtTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 30),
    _MrvEfmOamErrSymPerEvtTime_Type()
)
mrvEfmOamErrSymPerEvtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrSymPerEvtTime.setStatus("current")
_MrvEfmOamErrSymPerEvtWindow_Type = Unsigned64
_MrvEfmOamErrSymPerEvtWindow_Object = MibTableColumn
mrvEfmOamErrSymPerEvtWindow = _MrvEfmOamErrSymPerEvtWindow_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 31),
    _MrvEfmOamErrSymPerEvtWindow_Type()
)
mrvEfmOamErrSymPerEvtWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrSymPerEvtWindow.setStatus("current")
_MrvEfmOamErrSymPerEvtThreshld_Type = Unsigned64
_MrvEfmOamErrSymPerEvtThreshld_Object = MibTableColumn
mrvEfmOamErrSymPerEvtThreshld = _MrvEfmOamErrSymPerEvtThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 32),
    _MrvEfmOamErrSymPerEvtThreshld_Type()
)
mrvEfmOamErrSymPerEvtThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrSymPerEvtThreshld.setStatus("current")
_MrvEfmOamErrSymPerEvtCount_Type = Counter64
_MrvEfmOamErrSymPerEvtCount_Object = MibTableColumn
mrvEfmOamErrSymPerEvtCount = _MrvEfmOamErrSymPerEvtCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 33),
    _MrvEfmOamErrSymPerEvtCount_Type()
)
mrvEfmOamErrSymPerEvtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrSymPerEvtCount.setStatus("current")
_MrvEfmOamErrFrmCfgDuration_Type = Unsigned32
_MrvEfmOamErrFrmCfgDuration_Object = MibTableColumn
mrvEfmOamErrFrmCfgDuration = _MrvEfmOamErrFrmCfgDuration_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 34),
    _MrvEfmOamErrFrmCfgDuration_Type()
)
mrvEfmOamErrFrmCfgDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmCfgDuration.setStatus("current")
_MrvEfmOamErrFrmCfgThreshld_Type = Unsigned32
_MrvEfmOamErrFrmCfgThreshld_Object = MibTableColumn
mrvEfmOamErrFrmCfgThreshld = _MrvEfmOamErrFrmCfgThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 35),
    _MrvEfmOamErrFrmCfgThreshld_Type()
)
mrvEfmOamErrFrmCfgThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmCfgThreshld.setStatus("current")
_MrvEfmOamErrFrmEvtTime_Type = Unsigned16
_MrvEfmOamErrFrmEvtTime_Object = MibTableColumn
mrvEfmOamErrFrmEvtTime = _MrvEfmOamErrFrmEvtTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 36),
    _MrvEfmOamErrFrmEvtTime_Type()
)
mrvEfmOamErrFrmEvtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmEvtTime.setStatus("current")
_MrvEfmOamErrFrmEvtWindow_Type = Unsigned16
_MrvEfmOamErrFrmEvtWindow_Object = MibTableColumn
mrvEfmOamErrFrmEvtWindow = _MrvEfmOamErrFrmEvtWindow_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 37),
    _MrvEfmOamErrFrmEvtWindow_Type()
)
mrvEfmOamErrFrmEvtWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmEvtWindow.setStatus("current")
_MrvEfmOamErrFrmEvtThreshld_Type = Unsigned32
_MrvEfmOamErrFrmEvtThreshld_Object = MibTableColumn
mrvEfmOamErrFrmEvtThreshld = _MrvEfmOamErrFrmEvtThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 38),
    _MrvEfmOamErrFrmEvtThreshld_Type()
)
mrvEfmOamErrFrmEvtThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmEvtThreshld.setStatus("current")
_MrvEfmOamErrFrmEvtCount_Type = Counter64
_MrvEfmOamErrFrmEvtCount_Object = MibTableColumn
mrvEfmOamErrFrmEvtCount = _MrvEfmOamErrFrmEvtCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 39),
    _MrvEfmOamErrFrmEvtCount_Type()
)
mrvEfmOamErrFrmEvtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmEvtCount.setStatus("current")
_MrvEfmOamErrFrmPerCfgDuration_Type = Unsigned32
_MrvEfmOamErrFrmPerCfgDuration_Object = MibTableColumn
mrvEfmOamErrFrmPerCfgDuration = _MrvEfmOamErrFrmPerCfgDuration_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 40),
    _MrvEfmOamErrFrmPerCfgDuration_Type()
)
mrvEfmOamErrFrmPerCfgDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmPerCfgDuration.setStatus("current")
_MrvEfmOamErrFrmPerCfgThreshld_Type = Unsigned32
_MrvEfmOamErrFrmPerCfgThreshld_Object = MibTableColumn
mrvEfmOamErrFrmPerCfgThreshld = _MrvEfmOamErrFrmPerCfgThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 41),
    _MrvEfmOamErrFrmPerCfgThreshld_Type()
)
mrvEfmOamErrFrmPerCfgThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmPerCfgThreshld.setStatus("current")
_MrvEfmOamErrFrmPerEvtTime_Type = Unsigned16
_MrvEfmOamErrFrmPerEvtTime_Object = MibTableColumn
mrvEfmOamErrFrmPerEvtTime = _MrvEfmOamErrFrmPerEvtTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 42),
    _MrvEfmOamErrFrmPerEvtTime_Type()
)
mrvEfmOamErrFrmPerEvtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmPerEvtTime.setStatus("current")
_MrvEfmOamErrFrmPerEvtWindow_Type = Unsigned32
_MrvEfmOamErrFrmPerEvtWindow_Object = MibTableColumn
mrvEfmOamErrFrmPerEvtWindow = _MrvEfmOamErrFrmPerEvtWindow_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 43),
    _MrvEfmOamErrFrmPerEvtWindow_Type()
)
mrvEfmOamErrFrmPerEvtWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmPerEvtWindow.setStatus("current")
_MrvEfmOamErrFrmPerEvtThreshld_Type = Unsigned32
_MrvEfmOamErrFrmPerEvtThreshld_Object = MibTableColumn
mrvEfmOamErrFrmPerEvtThreshld = _MrvEfmOamErrFrmPerEvtThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 44),
    _MrvEfmOamErrFrmPerEvtThreshld_Type()
)
mrvEfmOamErrFrmPerEvtThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmPerEvtThreshld.setStatus("current")
_MrvEfmOamErrFrmPerEvtCount_Type = Counter64
_MrvEfmOamErrFrmPerEvtCount_Object = MibTableColumn
mrvEfmOamErrFrmPerEvtCount = _MrvEfmOamErrFrmPerEvtCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 45),
    _MrvEfmOamErrFrmPerEvtCount_Type()
)
mrvEfmOamErrFrmPerEvtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmPerEvtCount.setStatus("current")
_MrvEfmOamErrFrmSecSumCfgDuration_Type = Unsigned16
_MrvEfmOamErrFrmSecSumCfgDuration_Object = MibTableColumn
mrvEfmOamErrFrmSecSumCfgDuration = _MrvEfmOamErrFrmSecSumCfgDuration_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 46),
    _MrvEfmOamErrFrmSecSumCfgDuration_Type()
)
mrvEfmOamErrFrmSecSumCfgDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmSecSumCfgDuration.setStatus("current")
_MrvEfmOamErrFrmSecSumCfgThreshld_Type = Unsigned16
_MrvEfmOamErrFrmSecSumCfgThreshld_Object = MibTableColumn
mrvEfmOamErrFrmSecSumCfgThreshld = _MrvEfmOamErrFrmSecSumCfgThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 47),
    _MrvEfmOamErrFrmSecSumCfgThreshld_Type()
)
mrvEfmOamErrFrmSecSumCfgThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmSecSumCfgThreshld.setStatus("current")
_MrvEfmOamErrFrmSecSumEvtTime_Type = Unsigned16
_MrvEfmOamErrFrmSecSumEvtTime_Object = MibTableColumn
mrvEfmOamErrFrmSecSumEvtTime = _MrvEfmOamErrFrmSecSumEvtTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 48),
    _MrvEfmOamErrFrmSecSumEvtTime_Type()
)
mrvEfmOamErrFrmSecSumEvtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmSecSumEvtTime.setStatus("current")
_MrvEfmOamErrFrmSecSumEvtWindow_Type = Unsigned16
_MrvEfmOamErrFrmSecSumEvtWindow_Object = MibTableColumn
mrvEfmOamErrFrmSecSumEvtWindow = _MrvEfmOamErrFrmSecSumEvtWindow_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 49),
    _MrvEfmOamErrFrmSecSumEvtWindow_Type()
)
mrvEfmOamErrFrmSecSumEvtWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmSecSumEvtWindow.setStatus("current")
_MrvEfmOamErrFrmSecSumEvtThreshld_Type = Unsigned16
_MrvEfmOamErrFrmSecSumEvtThreshld_Object = MibTableColumn
mrvEfmOamErrFrmSecSumEvtThreshld = _MrvEfmOamErrFrmSecSumEvtThreshld_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 50),
    _MrvEfmOamErrFrmSecSumEvtThreshld_Type()
)
mrvEfmOamErrFrmSecSumEvtThreshld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmSecSumEvtThreshld.setStatus("current")
_MrvEfmOamErrFrmSecSumEvtCount_Type = Counter32
_MrvEfmOamErrFrmSecSumEvtCount_Object = MibTableColumn
mrvEfmOamErrFrmSecSumEvtCount = _MrvEfmOamErrFrmSecSumEvtCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 51),
    _MrvEfmOamErrFrmSecSumEvtCount_Type()
)
mrvEfmOamErrFrmSecSumEvtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamErrFrmSecSumEvtCount.setStatus("current")
_MrvEfmOamFramesLostDueToOamError_Type = Counter32
_MrvEfmOamFramesLostDueToOamError_Object = MibTableColumn
mrvEfmOamFramesLostDueToOamError = _MrvEfmOamFramesLostDueToOamError_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 52),
    _MrvEfmOamFramesLostDueToOamError_Type()
)
mrvEfmOamFramesLostDueToOamError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamFramesLostDueToOamError.setStatus("current")


class _MrvEfmOamAdminState_Type(Integer32):
    """Custom type mrvEfmOamAdminState based on Integer32"""
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


_MrvEfmOamAdminState_Type.__name__ = "Integer32"
_MrvEfmOamAdminState_Object = MibTableColumn
mrvEfmOamAdminState = _MrvEfmOamAdminState_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 53),
    _MrvEfmOamAdminState_Type()
)
mrvEfmOamAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrvEfmOamAdminState.setStatus("current")


class _MrvEfmOamOperState_Type(OctetString):
    """Custom type mrvEfmOamOperState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MrvEfmOamOperState_Type.__name__ = "OctetString"
_MrvEfmOamOperState_Object = MibTableColumn
mrvEfmOamOperState = _MrvEfmOamOperState_Object(
    (1, 3, 6, 1, 4, 1, 629, 300, 1, 3, 1, 1, 54),
    _MrvEfmOamOperState_Type()
)
mrvEfmOamOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrvEfmOamOperState.setStatus("current")
_MrvEfmProduct_ObjectIdentity = ObjectIdentity
mrvEfmProduct = _MrvEfmProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300, 2)
)
_MrvEfmNc316Nm_ObjectIdentity = ObjectIdentity
mrvEfmNc316Nm = _MrvEfmNc316Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300, 2, 1)
)
_MrvEfmConformance_ObjectIdentity = ObjectIdentity
mrvEfmConformance = _MrvEfmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300, 3)
)
_MrvEfmGroups_ObjectIdentity = ObjectIdentity
mrvEfmGroups = _MrvEfmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 300, 3, 1)
)

# Managed Objects groups

mrvEfmOamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 300, 3, 1, 3)
)
mrvEfmOamGroup.setObjects(
      *(("MRV-EFM-MIB", "mrvEfmPhysicalIfIndex"),
        ("MRV-EFM-MIB", "mrvEfmOamIfIndex"),
        ("MRV-EFM-MIB", "mrvEfmOamPeerIfIndex"),
        ("MRV-EFM-MIB", "mrvEfmOamMode"),
        ("MRV-EFM-MIB", "mrvEfmOamCfg"),
        ("MRV-EFM-MIB", "mrvEfmOamPduCfg"),
        ("MRV-EFM-MIB", "mrvEfmOamFlagsField"),
        ("MRV-EFM-MIB", "mrvEfmOamState"),
        ("MRV-EFM-MIB", "mrvEfmOamVendorOUI"),
        ("MRV-EFM-MIB", "mrvEfmOamVendorDeviceId"),
        ("MRV-EFM-MIB", "mrvEfmOamVendorDeviceVersion"),
        ("MRV-EFM-MIB", "mrvEfmOamPDUTx"),
        ("MRV-EFM-MIB", "mrvEfmOamPDURx"),
        ("MRV-EFM-MIB", "mrvEfmOamUnsupportedCodesRx"),
        ("MRV-EFM-MIB", "mrvEfmOamInformationTx"),
        ("MRV-EFM-MIB", "mrvEfmOamInformationRx"),
        ("MRV-EFM-MIB", "mrvEfmOamEventNotificationTx"),
        ("MRV-EFM-MIB", "mrvEfmOamUniEventNotificationRx"),
        ("MRV-EFM-MIB", "mrvEfmOamDupEventNotificationRx"),
        ("MRV-EFM-MIB", "mrvEfmOamLoopbackControlTx"),
        ("MRV-EFM-MIB", "mrvEfmOamLoopbackControlRx"),
        ("MRV-EFM-MIB", "mrvEfmOamVariableRequestTx"),
        ("MRV-EFM-MIB", "mrvEfmOamVariableRequestRx"),
        ("MRV-EFM-MIB", "mrvEfmOamVariableResponseTx"),
        ("MRV-EFM-MIB", "mrvEfmOamVariableResponseRx"),
        ("MRV-EFM-MIB", "mrvEfmOamOrganizationSpecificTx"),
        ("MRV-EFM-MIB", "mrvEfmOamOrganizationSpecificRx"),
        ("MRV-EFM-MIB", "mrvEfmOamErrSymPerCfgDuration"),
        ("MRV-EFM-MIB", "mrvEfmOamErrSymPerCfgThreshld"),
        ("MRV-EFM-MIB", "mrvEfmOamErrSymPerEvtTime"),
        ("MRV-EFM-MIB", "mrvEfmOamErrSymPerEvtWindow"),
        ("MRV-EFM-MIB", "mrvEfmOamErrSymPerEvtThreshld"),
        ("MRV-EFM-MIB", "mrvEfmOamErrSymPerEvtCount"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmCfgDuration"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmCfgThreshld"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmEvtTime"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmEvtWindow"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmEvtThreshld"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmEvtCount"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmPerCfgDuration"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmPerCfgThreshld"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmPerEvtTime"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmPerEvtWindow"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmPerEvtThreshld"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmPerEvtCount"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmSecSumCfgDuration"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmSecSumCfgThreshld"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmSecSumEvtTime"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmSecSumEvtWindow"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmSecSumEvtThreshld"),
        ("MRV-EFM-MIB", "mrvEfmOamErrFrmSecSumEvtCount"),
        ("MRV-EFM-MIB", "mrvEfmOamFramesLostDueToOamError"),
        ("MRV-EFM-MIB", "mrvEfmOamAdminState"),
        ("MRV-EFM-MIB", "mrvEfmOamOperState"))
)
if mibBuilder.loadTexts:
    mrvEfmOamGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-EFM-MIB",
    **{"Unsigned16": Unsigned16,
       "Unsigned64": Unsigned64,
       "mrvEfmMib": mrvEfmMib,
       "mrvEfmObjects": mrvEfmObjects,
       "mrvEfmOamGrp": mrvEfmOamGrp,
       "mrvEfmOamTable": mrvEfmOamTable,
       "mrvEfmOamEntry": mrvEfmOamEntry,
       "mrvEfmPhysicalIfIndex": mrvEfmPhysicalIfIndex,
       "mrvEfmOamIfIndex": mrvEfmOamIfIndex,
       "mrvEfmOamPeerIfIndex": mrvEfmOamPeerIfIndex,
       "mrvEfmOamMode": mrvEfmOamMode,
       "mrvEfmOamCfg": mrvEfmOamCfg,
       "mrvEfmOamPduCfg": mrvEfmOamPduCfg,
       "mrvEfmOamFlagsField": mrvEfmOamFlagsField,
       "mrvEfmOamState": mrvEfmOamState,
       "mrvEfmOamVendorOUI": mrvEfmOamVendorOUI,
       "mrvEfmOamVendorDeviceId": mrvEfmOamVendorDeviceId,
       "mrvEfmOamVendorDeviceVersion": mrvEfmOamVendorDeviceVersion,
       "mrvEfmOamPDUTx": mrvEfmOamPDUTx,
       "mrvEfmOamPDURx": mrvEfmOamPDURx,
       "mrvEfmOamUnsupportedCodesRx": mrvEfmOamUnsupportedCodesRx,
       "mrvEfmOamInformationTx": mrvEfmOamInformationTx,
       "mrvEfmOamInformationRx": mrvEfmOamInformationRx,
       "mrvEfmOamEventNotificationTx": mrvEfmOamEventNotificationTx,
       "mrvEfmOamUniEventNotificationRx": mrvEfmOamUniEventNotificationRx,
       "mrvEfmOamDupEventNotificationRx": mrvEfmOamDupEventNotificationRx,
       "mrvEfmOamLoopbackControlTx": mrvEfmOamLoopbackControlTx,
       "mrvEfmOamLoopbackControlRx": mrvEfmOamLoopbackControlRx,
       "mrvEfmOamVariableRequestTx": mrvEfmOamVariableRequestTx,
       "mrvEfmOamVariableRequestRx": mrvEfmOamVariableRequestRx,
       "mrvEfmOamVariableResponseTx": mrvEfmOamVariableResponseTx,
       "mrvEfmOamVariableResponseRx": mrvEfmOamVariableResponseRx,
       "mrvEfmOamOrganizationSpecificTx": mrvEfmOamOrganizationSpecificTx,
       "mrvEfmOamOrganizationSpecificRx": mrvEfmOamOrganizationSpecificRx,
       "mrvEfmOamErrSymPerCfgDuration": mrvEfmOamErrSymPerCfgDuration,
       "mrvEfmOamErrSymPerCfgThreshld": mrvEfmOamErrSymPerCfgThreshld,
       "mrvEfmOamErrSymPerEvtTime": mrvEfmOamErrSymPerEvtTime,
       "mrvEfmOamErrSymPerEvtWindow": mrvEfmOamErrSymPerEvtWindow,
       "mrvEfmOamErrSymPerEvtThreshld": mrvEfmOamErrSymPerEvtThreshld,
       "mrvEfmOamErrSymPerEvtCount": mrvEfmOamErrSymPerEvtCount,
       "mrvEfmOamErrFrmCfgDuration": mrvEfmOamErrFrmCfgDuration,
       "mrvEfmOamErrFrmCfgThreshld": mrvEfmOamErrFrmCfgThreshld,
       "mrvEfmOamErrFrmEvtTime": mrvEfmOamErrFrmEvtTime,
       "mrvEfmOamErrFrmEvtWindow": mrvEfmOamErrFrmEvtWindow,
       "mrvEfmOamErrFrmEvtThreshld": mrvEfmOamErrFrmEvtThreshld,
       "mrvEfmOamErrFrmEvtCount": mrvEfmOamErrFrmEvtCount,
       "mrvEfmOamErrFrmPerCfgDuration": mrvEfmOamErrFrmPerCfgDuration,
       "mrvEfmOamErrFrmPerCfgThreshld": mrvEfmOamErrFrmPerCfgThreshld,
       "mrvEfmOamErrFrmPerEvtTime": mrvEfmOamErrFrmPerEvtTime,
       "mrvEfmOamErrFrmPerEvtWindow": mrvEfmOamErrFrmPerEvtWindow,
       "mrvEfmOamErrFrmPerEvtThreshld": mrvEfmOamErrFrmPerEvtThreshld,
       "mrvEfmOamErrFrmPerEvtCount": mrvEfmOamErrFrmPerEvtCount,
       "mrvEfmOamErrFrmSecSumCfgDuration": mrvEfmOamErrFrmSecSumCfgDuration,
       "mrvEfmOamErrFrmSecSumCfgThreshld": mrvEfmOamErrFrmSecSumCfgThreshld,
       "mrvEfmOamErrFrmSecSumEvtTime": mrvEfmOamErrFrmSecSumEvtTime,
       "mrvEfmOamErrFrmSecSumEvtWindow": mrvEfmOamErrFrmSecSumEvtWindow,
       "mrvEfmOamErrFrmSecSumEvtThreshld": mrvEfmOamErrFrmSecSumEvtThreshld,
       "mrvEfmOamErrFrmSecSumEvtCount": mrvEfmOamErrFrmSecSumEvtCount,
       "mrvEfmOamFramesLostDueToOamError": mrvEfmOamFramesLostDueToOamError,
       "mrvEfmOamAdminState": mrvEfmOamAdminState,
       "mrvEfmOamOperState": mrvEfmOamOperState,
       "mrvEfmProduct": mrvEfmProduct,
       "mrvEfmNc316Nm": mrvEfmNc316Nm,
       "mrvEfmConformance": mrvEfmConformance,
       "mrvEfmGroups": mrvEfmGroups,
       "mrvEfmOamGroup": mrvEfmOamGroup}
)
