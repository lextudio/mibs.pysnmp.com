# SNMP MIB module (TPLINK-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-VRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:50 2024
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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkVrrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65)
)
tplinkVrrpMIB.setRevisions(
        ("2012-12-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkVrrpMIBObjects_ObjectIdentity = ObjectIdentity
tplinkVrrpMIBObjects = _TplinkVrrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1)
)
_TpVrrpGlobalCtrl_ObjectIdentity = ObjectIdentity
tpVrrpGlobalCtrl = _TpVrrpGlobalCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1)
)
_TpVrrpGlobalCtrlTable_Object = MibTable
tpVrrpGlobalCtrlTable = _TpVrrpGlobalCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpVrrpGlobalCtrlTable.setStatus("current")
_TpVrrpGlobalCtrlEntry_Object = MibTableRow
tpVrrpGlobalCtrlEntry = _TpVrrpGlobalCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1)
)
tpVrrpGlobalCtrlEntry.setIndexNames(
    (0, "TPLINK-VRRP-MIB", "tpVrrpVrid"),
    (0, "TPLINK-VRRP-MIB", "tpVrrpVid"),
)
if mibBuilder.loadTexts:
    tpVrrpGlobalCtrlEntry.setStatus("current")


class _TpVrrpVrid_Type(Integer32):
    """Custom type tpVrrpVrid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TpVrrpVrid_Type.__name__ = "Integer32"
_TpVrrpVrid_Object = MibTableColumn
tpVrrpVrid = _TpVrrpVrid_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 1),
    _TpVrrpVrid_Type()
)
tpVrrpVrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpVrid.setStatus("current")
_TpVrrpVid_Type = Integer32
_TpVrrpVid_Object = MibTableColumn
tpVrrpVid = _TpVrrpVid_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 2),
    _TpVrrpVid_Type()
)
tpVrrpVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpVid.setStatus("current")


class _TpVrrpIntfStatus_Type(Integer32):
    """Custom type tpVrrpIntfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interfacevlan", 1),
          ("routedport", 0))
    )


_TpVrrpIntfStatus_Type.__name__ = "Integer32"
_TpVrrpIntfStatus_Object = MibTableColumn
tpVrrpIntfStatus = _TpVrrpIntfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 3),
    _TpVrrpIntfStatus_Type()
)
tpVrrpIntfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpIntfStatus.setStatus("current")
_TpVrrpInterfaceIP_Type = IpAddress
_TpVrrpInterfaceIP_Object = MibTableColumn
tpVrrpInterfaceIP = _TpVrrpInterfaceIP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 4),
    _TpVrrpInterfaceIP_Type()
)
tpVrrpInterfaceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpInterfaceIP.setStatus("current")
_TpVrrpMacAddress_Type = OctetString
_TpVrrpMacAddress_Object = MibTableColumn
tpVrrpMacAddress = _TpVrrpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 5),
    _TpVrrpMacAddress_Type()
)
tpVrrpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpMacAddress.setStatus("current")
_TpVrrpDescription_Type = OctetString
_TpVrrpDescription_Object = MibTableColumn
tpVrrpDescription = _TpVrrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 6),
    _TpVrrpDescription_Type()
)
tpVrrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVrrpDescription.setStatus("current")
_TpVrrpPrimaryVirtualIp_Type = IpAddress
_TpVrrpPrimaryVirtualIp_Object = MibTableColumn
tpVrrpPrimaryVirtualIp = _TpVrrpPrimaryVirtualIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 7),
    _TpVrrpPrimaryVirtualIp_Type()
)
tpVrrpPrimaryVirtualIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpPrimaryVirtualIp.setStatus("current")


class _TpVrrpRunPriority_Type(Integer32):
    """Custom type tpVrrpRunPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TpVrrpRunPriority_Type.__name__ = "Integer32"
_TpVrrpRunPriority_Object = MibTableColumn
tpVrrpRunPriority = _TpVrrpRunPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 8),
    _TpVrrpRunPriority_Type()
)
tpVrrpRunPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpRunPriority.setStatus("current")


class _TpVrrpConfigPriority_Type(Integer32):
    """Custom type tpVrrpConfigPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TpVrrpConfigPriority_Type.__name__ = "Integer32"
_TpVrrpConfigPriority_Object = MibTableColumn
tpVrrpConfigPriority = _TpVrrpConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 9),
    _TpVrrpConfigPriority_Type()
)
tpVrrpConfigPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVrrpConfigPriority.setStatus("current")


class _TpVrrpAdvertisement_Type(Integer32):
    """Custom type tpVrrpAdvertisement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TpVrrpAdvertisement_Type.__name__ = "Integer32"
_TpVrrpAdvertisement_Object = MibTableColumn
tpVrrpAdvertisement = _TpVrrpAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 10),
    _TpVrrpAdvertisement_Type()
)
tpVrrpAdvertisement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVrrpAdvertisement.setStatus("current")


class _TpVrrpPreeptMode_Type(Integer32):
    """Custom type tpVrrpPreeptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_TpVrrpPreeptMode_Type.__name__ = "Integer32"
_TpVrrpPreeptMode_Object = MibTableColumn
tpVrrpPreeptMode = _TpVrrpPreeptMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 11),
    _TpVrrpPreeptMode_Type()
)
tpVrrpPreeptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVrrpPreeptMode.setStatus("current")


class _TpVrrpTimeDelay_Type(Integer32):
    """Custom type tpVrrpTimeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TpVrrpTimeDelay_Type.__name__ = "Integer32"
_TpVrrpTimeDelay_Object = MibTableColumn
tpVrrpTimeDelay = _TpVrrpTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 12),
    _TpVrrpTimeDelay_Type()
)
tpVrrpTimeDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVrrpTimeDelay.setStatus("current")


class _TpVrrpAuthType_Type(Integer32):
    """Custom type tpVrrpAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("normal", 0),
          ("simple", 1))
    )


_TpVrrpAuthType_Type.__name__ = "Integer32"
_TpVrrpAuthType_Object = MibTableColumn
tpVrrpAuthType = _TpVrrpAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 13),
    _TpVrrpAuthType_Type()
)
tpVrrpAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVrrpAuthType.setStatus("current")
_TpVrrpKey_Type = OctetString
_TpVrrpKey_Object = MibTableColumn
tpVrrpKey = _TpVrrpKey_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 14),
    _TpVrrpKey_Type()
)
tpVrrpKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVrrpKey.setStatus("current")


class _TpVrrpState_Type(Integer32):
    """Custom type tpVrrpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("initialize", 0),
          ("master", 2))
    )


_TpVrrpState_Type.__name__ = "Integer32"
_TpVrrpState_Object = MibTableColumn
tpVrrpState = _TpVrrpState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 15),
    _TpVrrpState_Type()
)
tpVrrpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpState.setStatus("current")
_TpVrrpStatus_Type = TPRowStatus
_TpVrrpStatus_Object = MibTableColumn
tpVrrpStatus = _TpVrrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 1, 1, 1, 16),
    _TpVrrpStatus_Type()
)
tpVrrpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVrrpStatus.setStatus("current")
_TpVrrpVirtualIpCtrl_ObjectIdentity = ObjectIdentity
tpVrrpVirtualIpCtrl = _TpVrrpVirtualIpCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2)
)
_TpVrrpVirtualIpCtrlTable_Object = MibTable
tpVrrpVirtualIpCtrlTable = _TpVrrpVirtualIpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpVrrpVirtualIpCtrlTable.setStatus("current")
_TpVrrpVirtualIpCtrlEntry_Object = MibTableRow
tpVrrpVirtualIpCtrlEntry = _TpVrrpVirtualIpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1, 1)
)
tpVrrpVirtualIpCtrlEntry.setIndexNames(
    (0, "TPLINK-VRRP-MIB", "tpVrrpVirtualIpVrid"),
    (0, "TPLINK-VRRP-MIB", "tpVrrpVirtualIpVid"),
    (0, "TPLINK-VRRP-MIB", "tpVrrpVirtualIpAddress"),
)
if mibBuilder.loadTexts:
    tpVrrpVirtualIpCtrlEntry.setStatus("current")


class _TpVrrpVirtualIpVrid_Type(Integer32):
    """Custom type tpVrrpVirtualIpVrid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TpVrrpVirtualIpVrid_Type.__name__ = "Integer32"
_TpVrrpVirtualIpVrid_Object = MibTableColumn
tpVrrpVirtualIpVrid = _TpVrrpVirtualIpVrid_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1, 1, 1),
    _TpVrrpVirtualIpVrid_Type()
)
tpVrrpVirtualIpVrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpVirtualIpVrid.setStatus("current")
_TpVrrpVirtualIpVid_Type = Integer32
_TpVrrpVirtualIpVid_Object = MibTableColumn
tpVrrpVirtualIpVid = _TpVrrpVirtualIpVid_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1, 1, 2),
    _TpVrrpVirtualIpVid_Type()
)
tpVrrpVirtualIpVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpVirtualIpVid.setStatus("current")


class _TpVrrpVirtualIpintfStatus_Type(Integer32):
    """Custom type tpVrrpVirtualIpintfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interfacevlan", 1),
          ("routedport", 0))
    )


_TpVrrpVirtualIpintfStatus_Type.__name__ = "Integer32"
_TpVrrpVirtualIpintfStatus_Object = MibTableColumn
tpVrrpVirtualIpintfStatus = _TpVrrpVirtualIpintfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1, 1, 3),
    _TpVrrpVirtualIpintfStatus_Type()
)
tpVrrpVirtualIpintfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpVirtualIpintfStatus.setStatus("current")
_TpVrrpVirtualIpAddress_Type = IpAddress
_TpVrrpVirtualIpAddress_Object = MibTableColumn
tpVrrpVirtualIpAddress = _TpVrrpVirtualIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1, 1, 4),
    _TpVrrpVirtualIpAddress_Type()
)
tpVrrpVirtualIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpVirtualIpAddress.setStatus("current")
_TpVrrpVirtualIpStatus_Type = TPRowStatus
_TpVrrpVirtualIpStatus_Object = MibTableColumn
tpVrrpVirtualIpStatus = _TpVrrpVirtualIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 2, 1, 1, 5),
    _TpVrrpVirtualIpStatus_Type()
)
tpVrrpVirtualIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVrrpVirtualIpStatus.setStatus("current")
_TpVrrpTrackCtrl_ObjectIdentity = ObjectIdentity
tpVrrpTrackCtrl = _TpVrrpTrackCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3)
)
_TpVrrpTrackCtrlTable_Object = MibTable
tpVrrpTrackCtrlTable = _TpVrrpTrackCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tpVrrpTrackCtrlTable.setStatus("current")
_TpVrrpTrackCtrlEntry_Object = MibTableRow
tpVrrpTrackCtrlEntry = _TpVrrpTrackCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1)
)
tpVrrpTrackCtrlEntry.setIndexNames(
    (0, "TPLINK-VRRP-MIB", "tpVrrpTrackVrid"),
    (0, "TPLINK-VRRP-MIB", "tpVrrpTrackVid"),
    (0, "TPLINK-VRRP-MIB", "tpVrrpTrackInterface"),
)
if mibBuilder.loadTexts:
    tpVrrpTrackCtrlEntry.setStatus("current")


class _TpVrrpTrackVrid_Type(Integer32):
    """Custom type tpVrrpTrackVrid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TpVrrpTrackVrid_Type.__name__ = "Integer32"
_TpVrrpTrackVrid_Object = MibTableColumn
tpVrrpTrackVrid = _TpVrrpTrackVrid_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 1),
    _TpVrrpTrackVrid_Type()
)
tpVrrpTrackVrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpTrackVrid.setStatus("current")
_TpVrrpTrackVid_Type = Integer32
_TpVrrpTrackVid_Object = MibTableColumn
tpVrrpTrackVid = _TpVrrpTrackVid_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 2),
    _TpVrrpTrackVid_Type()
)
tpVrrpTrackVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpTrackVid.setStatus("current")


class _TpVrrpTrackIntfStatus_Type(Integer32):
    """Custom type tpVrrpTrackIntfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interfacevlan", 1),
          ("routedport", 0))
    )


_TpVrrpTrackIntfStatus_Type.__name__ = "Integer32"
_TpVrrpTrackIntfStatus_Object = MibTableColumn
tpVrrpTrackIntfStatus = _TpVrrpTrackIntfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 3),
    _TpVrrpTrackIntfStatus_Type()
)
tpVrrpTrackIntfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpTrackIntfStatus.setStatus("current")
_TpVrrpTrackInterface_Type = Integer32
_TpVrrpTrackInterface_Object = MibTableColumn
tpVrrpTrackInterface = _TpVrrpTrackInterface_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 4),
    _TpVrrpTrackInterface_Type()
)
tpVrrpTrackInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpTrackInterface.setStatus("current")


class _TpVrrpTrackIntfTrackedStatus_Type(Integer32):
    """Custom type tpVrrpTrackIntfTrackedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interfacevlan", 1),
          ("routedport", 0))
    )


_TpVrrpTrackIntfTrackedStatus_Type.__name__ = "Integer32"
_TpVrrpTrackIntfTrackedStatus_Object = MibTableColumn
tpVrrpTrackIntfTrackedStatus = _TpVrrpTrackIntfTrackedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 5),
    _TpVrrpTrackIntfTrackedStatus_Type()
)
tpVrrpTrackIntfTrackedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpTrackIntfTrackedStatus.setStatus("current")


class _TpVrrpTrackPriortiy_Type(Integer32):
    """Custom type tpVrrpTrackPriortiy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TpVrrpTrackPriortiy_Type.__name__ = "Integer32"
_TpVrrpTrackPriortiy_Object = MibTableColumn
tpVrrpTrackPriortiy = _TpVrrpTrackPriortiy_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 6),
    _TpVrrpTrackPriortiy_Type()
)
tpVrrpTrackPriortiy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVrrpTrackPriortiy.setStatus("current")


class _TpVrrpLinkState_Type(Integer32):
    """Custom type tpVrrpLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_TpVrrpLinkState_Type.__name__ = "Integer32"
_TpVrrpLinkState_Object = MibTableColumn
tpVrrpLinkState = _TpVrrpLinkState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 7),
    _TpVrrpLinkState_Type()
)
tpVrrpLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpLinkState.setStatus("current")
_TpVrrpTrackStatus_Type = TPRowStatus
_TpVrrpTrackStatus_Object = MibTableColumn
tpVrrpTrackStatus = _TpVrrpTrackStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 3, 1, 1, 8),
    _TpVrrpTrackStatus_Type()
)
tpVrrpTrackStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpVrrpTrackStatus.setStatus("current")
_TpVrrpStatistics_ObjectIdentity = ObjectIdentity
tpVrrpStatistics = _TpVrrpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4)
)
_TpVrrpChecksumErrors_Type = Integer32
_TpVrrpChecksumErrors_Object = MibScalar
tpVrrpChecksumErrors = _TpVrrpChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 1),
    _TpVrrpChecksumErrors_Type()
)
tpVrrpChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpChecksumErrors.setStatus("current")
_TpVrrpVersionErrors_Type = Integer32
_TpVrrpVersionErrors_Object = MibScalar
tpVrrpVersionErrors = _TpVrrpVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 2),
    _TpVrrpVersionErrors_Type()
)
tpVrrpVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpVersionErrors.setStatus("current")
_TpVrrpVridErrors_Type = Integer32
_TpVrrpVridErrors_Object = MibScalar
tpVrrpVridErrors = _TpVrrpVridErrors_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 3),
    _TpVrrpVridErrors_Type()
)
tpVrrpVridErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpVridErrors.setStatus("current")
_TpVrrpStatsTable_Object = MibTable
tpVrrpStatsTable = _TpVrrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4)
)
if mibBuilder.loadTexts:
    tpVrrpStatsTable.setStatus("current")
_TpVrrpStatsEntry_Object = MibTableRow
tpVrrpStatsEntry = _TpVrrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1)
)
tpVrrpStatsEntry.setIndexNames(
    (0, "TPLINK-VRRP-MIB", "tpVrrpStatsVrid"),
    (0, "TPLINK-VRRP-MIB", "tpVrrpStatsVid"),
)
if mibBuilder.loadTexts:
    tpVrrpStatsEntry.setStatus("current")
_TpVrrpStatsVrid_Type = Integer32
_TpVrrpStatsVrid_Object = MibTableColumn
tpVrrpStatsVrid = _TpVrrpStatsVrid_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 1),
    _TpVrrpStatsVrid_Type()
)
tpVrrpStatsVrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpStatsVrid.setStatus("current")
_TpVrrpStatsVid_Type = Integer32
_TpVrrpStatsVid_Object = MibTableColumn
tpVrrpStatsVid = _TpVrrpStatsVid_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 2),
    _TpVrrpStatsVid_Type()
)
tpVrrpStatsVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpStatsVid.setStatus("current")


class _TpVrrpStatsIntfStatus_Type(Integer32):
    """Custom type tpVrrpStatsIntfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interfacevlan", 1),
          ("routedport", 0))
    )


_TpVrrpStatsIntfStatus_Type.__name__ = "Integer32"
_TpVrrpStatsIntfStatus_Object = MibTableColumn
tpVrrpStatsIntfStatus = _TpVrrpStatsIntfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 3),
    _TpVrrpStatsIntfStatus_Type()
)
tpVrrpStatsIntfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpStatsIntfStatus.setStatus("current")
_TpVrrpChecksumErr_Type = Integer32
_TpVrrpChecksumErr_Object = MibTableColumn
tpVrrpChecksumErr = _TpVrrpChecksumErr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 4),
    _TpVrrpChecksumErr_Type()
)
tpVrrpChecksumErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpChecksumErr.setStatus("current")
_TpVrrpVersionErr_Type = Integer32
_TpVrrpVersionErr_Object = MibTableColumn
tpVrrpVersionErr = _TpVrrpVersionErr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 5),
    _TpVrrpVersionErr_Type()
)
tpVrrpVersionErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpVersionErr.setStatus("current")
_TpVrrpStatsBecomeMaster_Type = Integer32
_TpVrrpStatsBecomeMaster_Object = MibTableColumn
tpVrrpStatsBecomeMaster = _TpVrrpStatsBecomeMaster_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 6),
    _TpVrrpStatsBecomeMaster_Type()
)
tpVrrpStatsBecomeMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpVrrpStatsBecomeMaster.setStatus("current")
_TpvrrpStatsAdvertiseRcvd_Type = Integer32
_TpvrrpStatsAdvertiseRcvd_Object = MibTableColumn
tpvrrpStatsAdvertiseRcvd = _TpvrrpStatsAdvertiseRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 7),
    _TpvrrpStatsAdvertiseRcvd_Type()
)
tpvrrpStatsAdvertiseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpvrrpStatsAdvertiseRcvd.setStatus("current")
_TpvrrpStatsAdvertiseSent_Type = Integer32
_TpvrrpStatsAdvertiseSent_Object = MibTableColumn
tpvrrpStatsAdvertiseSent = _TpvrrpStatsAdvertiseSent_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 8),
    _TpvrrpStatsAdvertiseSent_Type()
)
tpvrrpStatsAdvertiseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpvrrpStatsAdvertiseSent.setStatus("current")
_TpvrrpStatsAdvertiseIntervalErrors_Type = Integer32
_TpvrrpStatsAdvertiseIntervalErrors_Object = MibTableColumn
tpvrrpStatsAdvertiseIntervalErrors = _TpvrrpStatsAdvertiseIntervalErrors_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 9),
    _TpvrrpStatsAdvertiseIntervalErrors_Type()
)
tpvrrpStatsAdvertiseIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpvrrpStatsAdvertiseIntervalErrors.setStatus("current")
_TpvrrpStatsAuthFailures_Type = Integer32
_TpvrrpStatsAuthFailures_Object = MibTableColumn
tpvrrpStatsAuthFailures = _TpvrrpStatsAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 10),
    _TpvrrpStatsAuthFailures_Type()
)
tpvrrpStatsAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpvrrpStatsAuthFailures.setStatus("current")
_TpvrrpStatsIpTtlErrors_Type = Integer32
_TpvrrpStatsIpTtlErrors_Object = MibTableColumn
tpvrrpStatsIpTtlErrors = _TpvrrpStatsIpTtlErrors_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 11),
    _TpvrrpStatsIpTtlErrors_Type()
)
tpvrrpStatsIpTtlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpvrrpStatsIpTtlErrors.setStatus("current")
_TpvrrpStatsPriorityZeroPktsRcvd_Type = Integer32
_TpvrrpStatsPriorityZeroPktsRcvd_Object = MibTableColumn
tpvrrpStatsPriorityZeroPktsRcvd = _TpvrrpStatsPriorityZeroPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 12),
    _TpvrrpStatsPriorityZeroPktsRcvd_Type()
)
tpvrrpStatsPriorityZeroPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpvrrpStatsPriorityZeroPktsRcvd.setStatus("current")
_TpvrrpStatsPriorityZeroPktsSent_Type = Integer32
_TpvrrpStatsPriorityZeroPktsSent_Object = MibTableColumn
tpvrrpStatsPriorityZeroPktsSent = _TpvrrpStatsPriorityZeroPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 13),
    _TpvrrpStatsPriorityZeroPktsSent_Type()
)
tpvrrpStatsPriorityZeroPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpvrrpStatsPriorityZeroPktsSent.setStatus("current")
_TpvrrpStatsInvalidTypePktsRcvd_Type = Integer32
_TpvrrpStatsInvalidTypePktsRcvd_Object = MibTableColumn
tpvrrpStatsInvalidTypePktsRcvd = _TpvrrpStatsInvalidTypePktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 14),
    _TpvrrpStatsInvalidTypePktsRcvd_Type()
)
tpvrrpStatsInvalidTypePktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpvrrpStatsInvalidTypePktsRcvd.setStatus("current")
_TpvrrpStatsAddressListErrors_Type = Integer32
_TpvrrpStatsAddressListErrors_Object = MibTableColumn
tpvrrpStatsAddressListErrors = _TpvrrpStatsAddressListErrors_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 15),
    _TpvrrpStatsAddressListErrors_Type()
)
tpvrrpStatsAddressListErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpvrrpStatsAddressListErrors.setStatus("current")
_TpvrrpStatsInvalidAuthType_Type = Integer32
_TpvrrpStatsInvalidAuthType_Object = MibTableColumn
tpvrrpStatsInvalidAuthType = _TpvrrpStatsInvalidAuthType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 16),
    _TpvrrpStatsInvalidAuthType_Type()
)
tpvrrpStatsInvalidAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpvrrpStatsInvalidAuthType.setStatus("current")
_TpvrrpStatsAuthTypeMismatch_Type = Integer32
_TpvrrpStatsAuthTypeMismatch_Object = MibTableColumn
tpvrrpStatsAuthTypeMismatch = _TpvrrpStatsAuthTypeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 17),
    _TpvrrpStatsAuthTypeMismatch_Type()
)
tpvrrpStatsAuthTypeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpvrrpStatsAuthTypeMismatch.setStatus("current")
_TpvrrpStatsPacketLengthErrors_Type = Integer32
_TpvrrpStatsPacketLengthErrors_Object = MibTableColumn
tpvrrpStatsPacketLengthErrors = _TpvrrpStatsPacketLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 4, 1, 18),
    _TpvrrpStatsPacketLengthErrors_Type()
)
tpvrrpStatsPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpvrrpStatsPacketLengthErrors.setStatus("current")


class _TpvrrpStatsClear_Type(Integer32):
    """Custom type tpvrrpStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("clear", 0))
    )


_TpvrrpStatsClear_Type.__name__ = "Integer32"
_TpvrrpStatsClear_Object = MibScalar
tpvrrpStatsClear = _TpvrrpStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 1, 4, 5),
    _TpvrrpStatsClear_Type()
)
tpvrrpStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpvrrpStatsClear.setStatus("current")
_TplinkVrrpNotifications_ObjectIdentity = ObjectIdentity
tplinkVrrpNotifications = _TplinkVrrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 65, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-VRRP-MIB",
    **{"tplinkVrrpMIB": tplinkVrrpMIB,
       "tplinkVrrpMIBObjects": tplinkVrrpMIBObjects,
       "tpVrrpGlobalCtrl": tpVrrpGlobalCtrl,
       "tpVrrpGlobalCtrlTable": tpVrrpGlobalCtrlTable,
       "tpVrrpGlobalCtrlEntry": tpVrrpGlobalCtrlEntry,
       "tpVrrpVrid": tpVrrpVrid,
       "tpVrrpVid": tpVrrpVid,
       "tpVrrpIntfStatus": tpVrrpIntfStatus,
       "tpVrrpInterfaceIP": tpVrrpInterfaceIP,
       "tpVrrpMacAddress": tpVrrpMacAddress,
       "tpVrrpDescription": tpVrrpDescription,
       "tpVrrpPrimaryVirtualIp": tpVrrpPrimaryVirtualIp,
       "tpVrrpRunPriority": tpVrrpRunPriority,
       "tpVrrpConfigPriority": tpVrrpConfigPriority,
       "tpVrrpAdvertisement": tpVrrpAdvertisement,
       "tpVrrpPreeptMode": tpVrrpPreeptMode,
       "tpVrrpTimeDelay": tpVrrpTimeDelay,
       "tpVrrpAuthType": tpVrrpAuthType,
       "tpVrrpKey": tpVrrpKey,
       "tpVrrpState": tpVrrpState,
       "tpVrrpStatus": tpVrrpStatus,
       "tpVrrpVirtualIpCtrl": tpVrrpVirtualIpCtrl,
       "tpVrrpVirtualIpCtrlTable": tpVrrpVirtualIpCtrlTable,
       "tpVrrpVirtualIpCtrlEntry": tpVrrpVirtualIpCtrlEntry,
       "tpVrrpVirtualIpVrid": tpVrrpVirtualIpVrid,
       "tpVrrpVirtualIpVid": tpVrrpVirtualIpVid,
       "tpVrrpVirtualIpintfStatus": tpVrrpVirtualIpintfStatus,
       "tpVrrpVirtualIpAddress": tpVrrpVirtualIpAddress,
       "tpVrrpVirtualIpStatus": tpVrrpVirtualIpStatus,
       "tpVrrpTrackCtrl": tpVrrpTrackCtrl,
       "tpVrrpTrackCtrlTable": tpVrrpTrackCtrlTable,
       "tpVrrpTrackCtrlEntry": tpVrrpTrackCtrlEntry,
       "tpVrrpTrackVrid": tpVrrpTrackVrid,
       "tpVrrpTrackVid": tpVrrpTrackVid,
       "tpVrrpTrackIntfStatus": tpVrrpTrackIntfStatus,
       "tpVrrpTrackInterface": tpVrrpTrackInterface,
       "tpVrrpTrackIntfTrackedStatus": tpVrrpTrackIntfTrackedStatus,
       "tpVrrpTrackPriortiy": tpVrrpTrackPriortiy,
       "tpVrrpLinkState": tpVrrpLinkState,
       "tpVrrpTrackStatus": tpVrrpTrackStatus,
       "tpVrrpStatistics": tpVrrpStatistics,
       "tpVrrpChecksumErrors": tpVrrpChecksumErrors,
       "tpVrrpVersionErrors": tpVrrpVersionErrors,
       "tpVrrpVridErrors": tpVrrpVridErrors,
       "tpVrrpStatsTable": tpVrrpStatsTable,
       "tpVrrpStatsEntry": tpVrrpStatsEntry,
       "tpVrrpStatsVrid": tpVrrpStatsVrid,
       "tpVrrpStatsVid": tpVrrpStatsVid,
       "tpVrrpStatsIntfStatus": tpVrrpStatsIntfStatus,
       "tpVrrpChecksumErr": tpVrrpChecksumErr,
       "tpVrrpVersionErr": tpVrrpVersionErr,
       "tpVrrpStatsBecomeMaster": tpVrrpStatsBecomeMaster,
       "tpvrrpStatsAdvertiseRcvd": tpvrrpStatsAdvertiseRcvd,
       "tpvrrpStatsAdvertiseSent": tpvrrpStatsAdvertiseSent,
       "tpvrrpStatsAdvertiseIntervalErrors": tpvrrpStatsAdvertiseIntervalErrors,
       "tpvrrpStatsAuthFailures": tpvrrpStatsAuthFailures,
       "tpvrrpStatsIpTtlErrors": tpvrrpStatsIpTtlErrors,
       "tpvrrpStatsPriorityZeroPktsRcvd": tpvrrpStatsPriorityZeroPktsRcvd,
       "tpvrrpStatsPriorityZeroPktsSent": tpvrrpStatsPriorityZeroPktsSent,
       "tpvrrpStatsInvalidTypePktsRcvd": tpvrrpStatsInvalidTypePktsRcvd,
       "tpvrrpStatsAddressListErrors": tpvrrpStatsAddressListErrors,
       "tpvrrpStatsInvalidAuthType": tpvrrpStatsInvalidAuthType,
       "tpvrrpStatsAuthTypeMismatch": tpvrrpStatsAuthTypeMismatch,
       "tpvrrpStatsPacketLengthErrors": tpvrrpStatsPacketLengthErrors,
       "tpvrrpStatsClear": tpvrrpStatsClear,
       "tplinkVrrpNotifications": tplinkVrrpNotifications}
)
