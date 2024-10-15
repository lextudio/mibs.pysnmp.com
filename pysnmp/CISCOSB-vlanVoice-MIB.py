# SNMP MIB module (CISCOSB-vlanVoice-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-vlanVoice-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:24 2024
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

(VlanPriority,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "VlanPriority")

(vlan,) = mibBuilder.importSymbols(
    "CISCOSB-vlan-MIB",
    "vlan")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

vlanVoice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54)
)
vlanVoice.setRevisions(
        ("2010-09-26 00:00",
         "2010-09-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _VlanVoiceAdminState_Type(Integer32):
    """Custom type vlanVoiceAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-enabled", 1),
          ("auto-triggered", 2),
          ("disabled", 0),
          ("oui-enabled", 3))
    )


_VlanVoiceAdminState_Type.__name__ = "Integer32"
_VlanVoiceAdminState_Object = MibScalar
vlanVoiceAdminState = _VlanVoiceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 6),
    _VlanVoiceAdminState_Type()
)
vlanVoiceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceAdminState.setStatus("current")


class _VlanVoiceOperState_Type(Integer32):
    """Custom type vlanVoiceOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-enabled", 1),
          ("auto-triggered", 2),
          ("disabled", 0),
          ("oui-enabled", 3))
    )


_VlanVoiceOperState_Type.__name__ = "Integer32"
_VlanVoiceOperState_Object = MibScalar
vlanVoiceOperState = _VlanVoiceOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 7),
    _VlanVoiceOperState_Type()
)
vlanVoiceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceOperState.setStatus("current")


class _VlanVoiceAdminVid_Type(Integer32):
    """Custom type vlanVoiceAdminVid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanVoiceAdminVid_Type.__name__ = "Integer32"
_VlanVoiceAdminVid_Object = MibScalar
vlanVoiceAdminVid = _VlanVoiceAdminVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 8),
    _VlanVoiceAdminVid_Type()
)
vlanVoiceAdminVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceAdminVid.setStatus("current")


class _VlanVoiceOperVid_Type(Integer32):
    """Custom type vlanVoiceOperVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanVoiceOperVid_Type.__name__ = "Integer32"
_VlanVoiceOperVid_Object = MibScalar
vlanVoiceOperVid = _VlanVoiceOperVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 9),
    _VlanVoiceOperVid_Type()
)
vlanVoiceOperVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceOperVid.setStatus("current")
_VlanVoiceUcDeviceTable_Object = MibTable
vlanVoiceUcDeviceTable = _VlanVoiceUcDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 10)
)
if mibBuilder.loadTexts:
    vlanVoiceUcDeviceTable.setStatus("current")
_VlanVoiceUcDeviceEntry_Object = MibTableRow
vlanVoiceUcDeviceEntry = _VlanVoiceUcDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 10, 1)
)
vlanVoiceUcDeviceEntry.setIndexNames(
    (0, "CISCOSB-vlanVoice-MIB", "vlanVoiceUcDeviceType"),
    (0, "CISCOSB-vlanVoice-MIB", "vlanVoiceUcDeviceMacAddress"),
    (0, "CISCOSB-vlanVoice-MIB", "vlanVoiceUcDeviceInterface"),
)
if mibBuilder.loadTexts:
    vlanVoiceUcDeviceEntry.setStatus("current")


class _VlanVoiceUcDeviceType_Type(Integer32):
    """Custom type vlanVoiceUcDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("static", 1),
          ("uc", 2))
    )


_VlanVoiceUcDeviceType_Type.__name__ = "Integer32"
_VlanVoiceUcDeviceType_Object = MibTableColumn
vlanVoiceUcDeviceType = _VlanVoiceUcDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 10, 1, 1),
    _VlanVoiceUcDeviceType_Type()
)
vlanVoiceUcDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceUcDeviceType.setStatus("current")
_VlanVoiceUcDeviceMacAddress_Type = MacAddress
_VlanVoiceUcDeviceMacAddress_Object = MibTableColumn
vlanVoiceUcDeviceMacAddress = _VlanVoiceUcDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 10, 1, 2),
    _VlanVoiceUcDeviceMacAddress_Type()
)
vlanVoiceUcDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceUcDeviceMacAddress.setStatus("current")
_VlanVoiceUcDeviceInterface_Type = Integer32
_VlanVoiceUcDeviceInterface_Object = MibTableColumn
vlanVoiceUcDeviceInterface = _VlanVoiceUcDeviceInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 10, 1, 3),
    _VlanVoiceUcDeviceInterface_Type()
)
vlanVoiceUcDeviceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceUcDeviceInterface.setStatus("current")


class _VlanVoiceUcDeviceVid_Type(Integer32):
    """Custom type vlanVoiceUcDeviceVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanVoiceUcDeviceVid_Type.__name__ = "Integer32"
_VlanVoiceUcDeviceVid_Object = MibTableColumn
vlanVoiceUcDeviceVid = _VlanVoiceUcDeviceVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 10, 1, 4),
    _VlanVoiceUcDeviceVid_Type()
)
vlanVoiceUcDeviceVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceUcDeviceVid.setStatus("current")


class _VlanVoiceUcDeviceVpt_Type(Integer32):
    """Custom type vlanVoiceUcDeviceVpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanVoiceUcDeviceVpt_Type.__name__ = "Integer32"
_VlanVoiceUcDeviceVpt_Object = MibTableColumn
vlanVoiceUcDeviceVpt = _VlanVoiceUcDeviceVpt_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 10, 1, 5),
    _VlanVoiceUcDeviceVpt_Type()
)
vlanVoiceUcDeviceVpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceUcDeviceVpt.setStatus("current")


class _VlanVoiceUcDeviceDscp_Type(Integer32):
    """Custom type vlanVoiceUcDeviceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_VlanVoiceUcDeviceDscp_Type.__name__ = "Integer32"
_VlanVoiceUcDeviceDscp_Object = MibTableColumn
vlanVoiceUcDeviceDscp = _VlanVoiceUcDeviceDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 10, 1, 6),
    _VlanVoiceUcDeviceDscp_Type()
)
vlanVoiceUcDeviceDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceUcDeviceDscp.setStatus("current")
_VlanVoiceUcDeviceIsBest_Type = TruthValue
_VlanVoiceUcDeviceIsBest_Object = MibTableColumn
vlanVoiceUcDeviceIsBest = _VlanVoiceUcDeviceIsBest_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 10, 1, 7),
    _VlanVoiceUcDeviceIsBest_Type()
)
vlanVoiceUcDeviceIsBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceUcDeviceIsBest.setStatus("current")
_VlanVoiceAuto_ObjectIdentity = ObjectIdentity
vlanVoiceAuto = _VlanVoiceAuto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 11)
)
_VlanVoiceAutoAdmin_ObjectIdentity = ObjectIdentity
vlanVoiceAutoAdmin = _VlanVoiceAutoAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 11, 1)
)


class _VlanVoiceAutoAdminVpt_Type(VlanPriority):
    """Custom type vlanVoiceAutoAdminVpt based on VlanPriority"""
    defaultValue = 0


_VlanVoiceAutoAdminVpt_Object = MibScalar
vlanVoiceAutoAdminVpt = _VlanVoiceAutoAdminVpt_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 11, 1, 1),
    _VlanVoiceAutoAdminVpt_Type()
)
vlanVoiceAutoAdminVpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceAutoAdminVpt.setStatus("current")


class _VlanVoiceAutoAdminDscp_Type(Integer32):
    """Custom type vlanVoiceAutoAdminDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_VlanVoiceAutoAdminDscp_Type.__name__ = "Integer32"
_VlanVoiceAutoAdminDscp_Object = MibScalar
vlanVoiceAutoAdminDscp = _VlanVoiceAutoAdminDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 11, 1, 2),
    _VlanVoiceAutoAdminDscp_Type()
)
vlanVoiceAutoAdminDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceAutoAdminDscp.setStatus("current")
_VlanVoiceAutoOper_ObjectIdentity = ObjectIdentity
vlanVoiceAutoOper = _VlanVoiceAutoOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 11, 2)
)
_VlanVoiceAutoOperVpt_Type = VlanPriority
_VlanVoiceAutoOperVpt_Object = MibScalar
vlanVoiceAutoOperVpt = _VlanVoiceAutoOperVpt_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 11, 2, 1),
    _VlanVoiceAutoOperVpt_Type()
)
vlanVoiceAutoOperVpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceAutoOperVpt.setStatus("current")


class _VlanVoiceAutoOperDscp_Type(Integer32):
    """Custom type vlanVoiceAutoOperDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_VlanVoiceAutoOperDscp_Type.__name__ = "Integer32"
_VlanVoiceAutoOperDscp_Object = MibScalar
vlanVoiceAutoOperDscp = _VlanVoiceAutoOperDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 11, 2, 2),
    _VlanVoiceAutoOperDscp_Type()
)
vlanVoiceAutoOperDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceAutoOperDscp.setStatus("current")
_VlanVoiceAutoOperSource_Type = MacAddress
_VlanVoiceAutoOperSource_Object = MibScalar
vlanVoiceAutoOperSource = _VlanVoiceAutoOperSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 11, 2, 3),
    _VlanVoiceAutoOperSource_Type()
)
vlanVoiceAutoOperSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceAutoOperSource.setStatus("current")


class _VlanVoiceAutoOperPriority_Type(Integer32):
    """Custom type vlanVoiceAutoOperPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              6,
              10)
        )
    )
    namedValues = NamedValues(
        *(("default", 6),
          ("disabled", 10),
          ("staticActive", 0),
          ("staticInActive", 1),
          ("ucActive", 2),
          ("ucInActive", 3))
    )


_VlanVoiceAutoOperPriority_Type.__name__ = "Integer32"
_VlanVoiceAutoOperPriority_Object = MibScalar
vlanVoiceAutoOperPriority = _VlanVoiceAutoOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 11, 2, 4),
    _VlanVoiceAutoOperPriority_Type()
)
vlanVoiceAutoOperPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceAutoOperPriority.setStatus("current")
_VlanVoiceAutoRefresh_Type = TruthValue
_VlanVoiceAutoRefresh_Object = MibScalar
vlanVoiceAutoRefresh = _VlanVoiceAutoRefresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 11, 3),
    _VlanVoiceAutoRefresh_Type()
)
vlanVoiceAutoRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceAutoRefresh.setStatus("current")


class _VlanVoiceAutoAgreedVlanLastChange_Type(DisplayString):
    """Custom type vlanVoiceAutoAgreedVlanLastChange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_VlanVoiceAutoAgreedVlanLastChange_Type.__name__ = "DisplayString"
_VlanVoiceAutoAgreedVlanLastChange_Object = MibScalar
vlanVoiceAutoAgreedVlanLastChange = _VlanVoiceAutoAgreedVlanLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 11, 4),
    _VlanVoiceAutoAgreedVlanLastChange_Type()
)
vlanVoiceAutoAgreedVlanLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceAutoAgreedVlanLastChange.setStatus("current")
_VlanVoiceOUIBased_ObjectIdentity = ObjectIdentity
vlanVoiceOUIBased = _VlanVoiceOUIBased_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12)
)


class _VlanVoiceOUIBasedAdminPriority_Type(VlanPriority):
    """Custom type vlanVoiceOUIBasedAdminPriority based on VlanPriority"""
    defaultValue = 6


_VlanVoiceOUIBasedAdminPriority_Object = MibScalar
vlanVoiceOUIBasedAdminPriority = _VlanVoiceOUIBasedAdminPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 1),
    _VlanVoiceOUIBasedAdminPriority_Type()
)
vlanVoiceOUIBasedAdminPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedAdminPriority.setStatus("current")


class _VlanVoiceOUIBasedAdminRemark_Type(TruthValue):
    """Custom type vlanVoiceOUIBasedAdminRemark based on TruthValue"""


_VlanVoiceOUIBasedAdminRemark_Object = MibScalar
vlanVoiceOUIBasedAdminRemark = _VlanVoiceOUIBasedAdminRemark_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 2),
    _VlanVoiceOUIBasedAdminRemark_Type()
)
vlanVoiceOUIBasedAdminRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedAdminRemark.setStatus("current")


class _VlanVoiceOUIBasedSetToDefault_Type(TruthValue):
    """Custom type vlanVoiceOUIBasedSetToDefault based on TruthValue"""


_VlanVoiceOUIBasedSetToDefault_Object = MibScalar
vlanVoiceOUIBasedSetToDefault = _VlanVoiceOUIBasedSetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 3),
    _VlanVoiceOUIBasedSetToDefault_Type()
)
vlanVoiceOUIBasedSetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedSetToDefault.setStatus("current")
_VlanVoiceOUIBasedTable_Object = MibTable
vlanVoiceOUIBasedTable = _VlanVoiceOUIBasedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 4)
)
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedTable.setStatus("current")
_VlanVoiceOUIBasedEntry_Object = MibTableRow
vlanVoiceOUIBasedEntry = _VlanVoiceOUIBasedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 4, 1)
)
vlanVoiceOUIBasedEntry.setIndexNames(
    (0, "CISCOSB-vlanVoice-MIB", "vlanVoiceOUIBasedPrefix"),
)
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedEntry.setStatus("current")


class _VlanVoiceOUIBasedPrefix_Type(OctetString):
    """Custom type vlanVoiceOUIBasedPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_VlanVoiceOUIBasedPrefix_Type.__name__ = "OctetString"
_VlanVoiceOUIBasedPrefix_Object = MibTableColumn
vlanVoiceOUIBasedPrefix = _VlanVoiceOUIBasedPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 4, 1, 1),
    _VlanVoiceOUIBasedPrefix_Type()
)
vlanVoiceOUIBasedPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedPrefix.setStatus("current")


class _VlanVoiceOUIBasedDescription_Type(DisplayString):
    """Custom type vlanVoiceOUIBasedDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanVoiceOUIBasedDescription_Type.__name__ = "DisplayString"
_VlanVoiceOUIBasedDescription_Object = MibTableColumn
vlanVoiceOUIBasedDescription = _VlanVoiceOUIBasedDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 4, 1, 2),
    _VlanVoiceOUIBasedDescription_Type()
)
vlanVoiceOUIBasedDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedDescription.setStatus("current")
_VlanVoiceOUIBasedEntryRowStatus_Type = RowStatus
_VlanVoiceOUIBasedEntryRowStatus_Object = MibTableColumn
vlanVoiceOUIBasedEntryRowStatus = _VlanVoiceOUIBasedEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 4, 1, 3),
    _VlanVoiceOUIBasedEntryRowStatus_Type()
)
vlanVoiceOUIBasedEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedEntryRowStatus.setStatus("current")
_VlanVoiceOUIBasedPortTable_Object = MibTable
vlanVoiceOUIBasedPortTable = _VlanVoiceOUIBasedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 5)
)
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedPortTable.setStatus("current")
_VlanVoiceOUIBasedPortEntry_Object = MibTableRow
vlanVoiceOUIBasedPortEntry = _VlanVoiceOUIBasedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 5, 1)
)
vlanVoiceOUIBasedPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedPortEntry.setStatus("current")


class _VlanVoiceOUIBasedPortEnable_Type(TruthValue):
    """Custom type vlanVoiceOUIBasedPortEnable based on TruthValue"""


_VlanVoiceOUIBasedPortEnable_Object = MibTableColumn
vlanVoiceOUIBasedPortEnable = _VlanVoiceOUIBasedPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 5, 1, 1),
    _VlanVoiceOUIBasedPortEnable_Type()
)
vlanVoiceOUIBasedPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedPortEnable.setStatus("current")


class _VlanVoiceOUIBasedPortVlanIndex_Type(VlanIndex):
    """Custom type vlanVoiceOUIBasedPortVlanIndex based on VlanIndex"""
    defaultValue = 4095


_VlanVoiceOUIBasedPortVlanIndex_Object = MibTableColumn
vlanVoiceOUIBasedPortVlanIndex = _VlanVoiceOUIBasedPortVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 5, 1, 2),
    _VlanVoiceOUIBasedPortVlanIndex_Type()
)
vlanVoiceOUIBasedPortVlanIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedPortVlanIndex.setStatus("current")


class _VlanVoiceOUIBasedPortSecure_Type(TruthValue):
    """Custom type vlanVoiceOUIBasedPortSecure based on TruthValue"""


_VlanVoiceOUIBasedPortSecure_Object = MibTableColumn
vlanVoiceOUIBasedPortSecure = _VlanVoiceOUIBasedPortSecure_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 5, 1, 3),
    _VlanVoiceOUIBasedPortSecure_Type()
)
vlanVoiceOUIBasedPortSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedPortSecure.setStatus("current")


class _VlanVoiceOUIBasedPortCurrentMembership_Type(Integer32):
    """Custom type vlanVoiceOUIBasedPortCurrentMembership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_VlanVoiceOUIBasedPortCurrentMembership_Type.__name__ = "Integer32"
_VlanVoiceOUIBasedPortCurrentMembership_Object = MibTableColumn
vlanVoiceOUIBasedPortCurrentMembership = _VlanVoiceOUIBasedPortCurrentMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 5, 1, 4),
    _VlanVoiceOUIBasedPortCurrentMembership_Type()
)
vlanVoiceOUIBasedPortCurrentMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedPortCurrentMembership.setStatus("current")


class _VlanVoiceOUIBasedPortQosMode_Type(Integer32):
    """Custom type vlanVoiceOUIBasedPortQosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("src", 1))
    )


_VlanVoiceOUIBasedPortQosMode_Type.__name__ = "Integer32"
_VlanVoiceOUIBasedPortQosMode_Object = MibTableColumn
vlanVoiceOUIBasedPortQosMode = _VlanVoiceOUIBasedPortQosMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 5, 1, 5),
    _VlanVoiceOUIBasedPortQosMode_Type()
)
vlanVoiceOUIBasedPortQosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedPortQosMode.setStatus("current")


class _VlanVoiceOUIBasedAgingTimeout_Type(Integer32):
    """Custom type vlanVoiceOUIBasedAgingTimeout based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 43200),
    )


_VlanVoiceOUIBasedAgingTimeout_Type.__name__ = "Integer32"
_VlanVoiceOUIBasedAgingTimeout_Object = MibScalar
vlanVoiceOUIBasedAgingTimeout = _VlanVoiceOUIBasedAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 48, 54, 12, 6),
    _VlanVoiceOUIBasedAgingTimeout_Type()
)
vlanVoiceOUIBasedAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedAgingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vlanVoiceOUIBasedAgingTimeout.setUnits("minutes")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-vlanVoice-MIB",
    **{"vlanVoice": vlanVoice,
       "vlanVoiceAdminState": vlanVoiceAdminState,
       "vlanVoiceOperState": vlanVoiceOperState,
       "vlanVoiceAdminVid": vlanVoiceAdminVid,
       "vlanVoiceOperVid": vlanVoiceOperVid,
       "vlanVoiceUcDeviceTable": vlanVoiceUcDeviceTable,
       "vlanVoiceUcDeviceEntry": vlanVoiceUcDeviceEntry,
       "vlanVoiceUcDeviceType": vlanVoiceUcDeviceType,
       "vlanVoiceUcDeviceMacAddress": vlanVoiceUcDeviceMacAddress,
       "vlanVoiceUcDeviceInterface": vlanVoiceUcDeviceInterface,
       "vlanVoiceUcDeviceVid": vlanVoiceUcDeviceVid,
       "vlanVoiceUcDeviceVpt": vlanVoiceUcDeviceVpt,
       "vlanVoiceUcDeviceDscp": vlanVoiceUcDeviceDscp,
       "vlanVoiceUcDeviceIsBest": vlanVoiceUcDeviceIsBest,
       "vlanVoiceAuto": vlanVoiceAuto,
       "vlanVoiceAutoAdmin": vlanVoiceAutoAdmin,
       "vlanVoiceAutoAdminVpt": vlanVoiceAutoAdminVpt,
       "vlanVoiceAutoAdminDscp": vlanVoiceAutoAdminDscp,
       "vlanVoiceAutoOper": vlanVoiceAutoOper,
       "vlanVoiceAutoOperVpt": vlanVoiceAutoOperVpt,
       "vlanVoiceAutoOperDscp": vlanVoiceAutoOperDscp,
       "vlanVoiceAutoOperSource": vlanVoiceAutoOperSource,
       "vlanVoiceAutoOperPriority": vlanVoiceAutoOperPriority,
       "vlanVoiceAutoRefresh": vlanVoiceAutoRefresh,
       "vlanVoiceAutoAgreedVlanLastChange": vlanVoiceAutoAgreedVlanLastChange,
       "vlanVoiceOUIBased": vlanVoiceOUIBased,
       "vlanVoiceOUIBasedAdminPriority": vlanVoiceOUIBasedAdminPriority,
       "vlanVoiceOUIBasedAdminRemark": vlanVoiceOUIBasedAdminRemark,
       "vlanVoiceOUIBasedSetToDefault": vlanVoiceOUIBasedSetToDefault,
       "vlanVoiceOUIBasedTable": vlanVoiceOUIBasedTable,
       "vlanVoiceOUIBasedEntry": vlanVoiceOUIBasedEntry,
       "vlanVoiceOUIBasedPrefix": vlanVoiceOUIBasedPrefix,
       "vlanVoiceOUIBasedDescription": vlanVoiceOUIBasedDescription,
       "vlanVoiceOUIBasedEntryRowStatus": vlanVoiceOUIBasedEntryRowStatus,
       "vlanVoiceOUIBasedPortTable": vlanVoiceOUIBasedPortTable,
       "vlanVoiceOUIBasedPortEntry": vlanVoiceOUIBasedPortEntry,
       "vlanVoiceOUIBasedPortEnable": vlanVoiceOUIBasedPortEnable,
       "vlanVoiceOUIBasedPortVlanIndex": vlanVoiceOUIBasedPortVlanIndex,
       "vlanVoiceOUIBasedPortSecure": vlanVoiceOUIBasedPortSecure,
       "vlanVoiceOUIBasedPortCurrentMembership": vlanVoiceOUIBasedPortCurrentMembership,
       "vlanVoiceOUIBasedPortQosMode": vlanVoiceOUIBasedPortQosMode,
       "vlanVoiceOUIBasedAgingTimeout": vlanVoiceOUIBasedAgingTimeout}
)
