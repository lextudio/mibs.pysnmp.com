# SNMP MIB module (XYLAN-VSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-VSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:18 2024
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

(XylanModuleSubunit,) = mibBuilder.importSymbols(
    "CHASSIS-MIB",
    "XylanModuleSubunit")

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

(xylanVsmArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanVsmArch")


# MODULE-IDENTITY


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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





class VsmEnableDisabled(Integer32):
    """Custom type VsmEnableDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )





class VsmOnOff(Integer32):
    """Custom type VsmOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )





class VsmVoiceCodingType(Integer32):
    """Custom type VsmVoiceCodingType based on Integer32"""
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
        *(("aLawPcm", 1),
          ("ituG723-53", 3),
          ("ituG723-63", 4),
          ("ituG729AB", 5),
          ("muLawPcm", 2),
          ("t38-fax", 6))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VsmNetworkGroup_ObjectIdentity = ObjectIdentity
vsmNetworkGroup = _VsmNetworkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1)
)
_VsmVNTemplateTable_Object = MibTable
vsmVNTemplateTable = _VsmVNTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 1)
)
if mibBuilder.loadTexts:
    vsmVNTemplateTable.setStatus("mandatory")
_VsmVNTemplateEntry_Object = MibTableRow
vsmVNTemplateEntry = _VsmVNTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 1, 1)
)
vsmVNTemplateEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmVNTmplIndex"),
)
if mibBuilder.loadTexts:
    vsmVNTemplateEntry.setStatus("mandatory")
_VsmVNTmplIndex_Type = Integer32
_VsmVNTmplIndex_Object = MibTableColumn
vsmVNTmplIndex = _VsmVNTmplIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 1, 1, 1),
    _VsmVNTmplIndex_Type()
)
vsmVNTmplIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNTmplIndex.setStatus("mandatory")
_VsmVNTmplName_Type = DisplayString
_VsmVNTmplName_Object = MibTableColumn
vsmVNTmplName = _VsmVNTmplName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 1, 1, 2),
    _VsmVNTmplName_Type()
)
vsmVNTmplName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNTmplName.setStatus("deprecated")
_VsmVNTmplRowStatus_Type = RowStatus
_VsmVNTmplRowStatus_Object = MibTableColumn
vsmVNTmplRowStatus = _VsmVNTmplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 1, 1, 3),
    _VsmVNTmplRowStatus_Type()
)
vsmVNTmplRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNTmplRowStatus.setStatus("mandatory")
_VsmVNTmplH323GateKeeperPhoneGroupTable_Object = MibTable
vsmVNTmplH323GateKeeperPhoneGroupTable = _VsmVNTmplH323GateKeeperPhoneGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 2)
)
if mibBuilder.loadTexts:
    vsmVNTmplH323GateKeeperPhoneGroupTable.setStatus("mandatory")
_VsmVNTmplH323GateKeeperPhoneGroupEntry_Object = MibTableRow
vsmVNTmplH323GateKeeperPhoneGroupEntry = _VsmVNTmplH323GateKeeperPhoneGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 2, 1)
)
vsmVNTmplH323GateKeeperPhoneGroupEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmVNTmplName"),
    (0, "XYLAN-VSM-MIB", "vsmPhoneGroupName"),
)
if mibBuilder.loadTexts:
    vsmVNTmplH323GateKeeperPhoneGroupEntry.setStatus("mandatory")
_VsmVNTmplH323GateKeeperPhoneGroupRowStatus_Type = RowStatus
_VsmVNTmplH323GateKeeperPhoneGroupRowStatus_Object = MibTableColumn
vsmVNTmplH323GateKeeperPhoneGroupRowStatus = _VsmVNTmplH323GateKeeperPhoneGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 2, 1, 1),
    _VsmVNTmplH323GateKeeperPhoneGroupRowStatus_Type()
)
vsmVNTmplH323GateKeeperPhoneGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNTmplH323GateKeeperPhoneGroupRowStatus.setStatus("mandatory")
_VsmVNCardTable_Object = MibTable
vsmVNCardTable = _VsmVNCardTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3)
)
if mibBuilder.loadTexts:
    vsmVNCardTable.setStatus("mandatory")
_VsmVNCardEntry_Object = MibTableRow
vsmVNCardEntry = _VsmVNCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3, 1)
)
vsmVNCardEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmCardSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmCardSubunitIndex"),
)
if mibBuilder.loadTexts:
    vsmVNCardEntry.setStatus("mandatory")
_VsmVNCardH323DisplayName_Type = DisplayString
_VsmVNCardH323DisplayName_Object = MibTableColumn
vsmVNCardH323DisplayName = _VsmVNCardH323DisplayName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3, 1, 1),
    _VsmVNCardH323DisplayName_Type()
)
vsmVNCardH323DisplayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNCardH323DisplayName.setStatus("mandatory")


class _VsmVNCardRTPPortMode_Type(Integer32):
    """Custom type vsmVNCardRTPPortMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("sequential", 2))
    )


_VsmVNCardRTPPortMode_Type.__name__ = "Integer32"
_VsmVNCardRTPPortMode_Object = MibTableColumn
vsmVNCardRTPPortMode = _VsmVNCardRTPPortMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3, 1, 2),
    _VsmVNCardRTPPortMode_Type()
)
vsmVNCardRTPPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNCardRTPPortMode.setStatus("mandatory")


class _VsmVNCardRTPPortBase_Type(Integer32):
    """Custom type vsmVNCardRTPPortBase based on Integer32"""
    defaultValue = 30000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_VsmVNCardRTPPortBase_Type.__name__ = "Integer32"
_VsmVNCardRTPPortBase_Object = MibTableColumn
vsmVNCardRTPPortBase = _VsmVNCardRTPPortBase_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3, 1, 3),
    _VsmVNCardRTPPortBase_Type()
)
vsmVNCardRTPPortBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNCardRTPPortBase.setStatus("mandatory")


class _VsmVNCardH323OutFastStart_Type(VsmEnableDisabled):
    """Custom type vsmVNCardH323OutFastStart based on VsmEnableDisabled"""


_VsmVNCardH323OutFastStart_Object = MibTableColumn
vsmVNCardH323OutFastStart = _VsmVNCardH323OutFastStart_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3, 1, 4),
    _VsmVNCardH323OutFastStart_Type()
)
vsmVNCardH323OutFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNCardH323OutFastStart.setStatus("deprecated")


class _VsmVNCardH323InFastStart_Type(VsmEnableDisabled):
    """Custom type vsmVNCardH323InFastStart based on VsmEnableDisabled"""


_VsmVNCardH323InFastStart_Object = MibTableColumn
vsmVNCardH323InFastStart = _VsmVNCardH323InFastStart_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3, 1, 5),
    _VsmVNCardH323InFastStart_Type()
)
vsmVNCardH323InFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNCardH323InFastStart.setStatus("mandatory")


class _VsmVNCardH323GatekeeperCtrl_Type(VsmEnableDisabled):
    """Custom type vsmVNCardH323GatekeeperCtrl based on VsmEnableDisabled"""


_VsmVNCardH323GatekeeperCtrl_Object = MibTableColumn
vsmVNCardH323GatekeeperCtrl = _VsmVNCardH323GatekeeperCtrl_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3, 1, 6),
    _VsmVNCardH323GatekeeperCtrl_Type()
)
vsmVNCardH323GatekeeperCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNCardH323GatekeeperCtrl.setStatus("mandatory")


class _VsmVNCardH323GatekeeperMode_Type(Integer32):
    """Custom type vsmVNCardH323GatekeeperMode based on Integer32"""
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
        *(("auto", 3),
          ("manual", 2),
          ("off", 1))
    )


_VsmVNCardH323GatekeeperMode_Type.__name__ = "Integer32"
_VsmVNCardH323GatekeeperMode_Object = MibTableColumn
vsmVNCardH323GatekeeperMode = _VsmVNCardH323GatekeeperMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3, 1, 7),
    _VsmVNCardH323GatekeeperMode_Type()
)
vsmVNCardH323GatekeeperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNCardH323GatekeeperMode.setStatus("mandatory")
_VsmVNCardH323GatekeeperAddr_Type = IpAddress
_VsmVNCardH323GatekeeperAddr_Object = MibTableColumn
vsmVNCardH323GatekeeperAddr = _VsmVNCardH323GatekeeperAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3, 1, 8),
    _VsmVNCardH323GatekeeperAddr_Type()
)
vsmVNCardH323GatekeeperAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNCardH323GatekeeperAddr.setStatus("mandatory")


class _VsmVNCardH323AllowCallsWithoutGatekeeper_Type(VsmEnableDisabled):
    """Custom type vsmVNCardH323AllowCallsWithoutGatekeeper based on VsmEnableDisabled"""


_VsmVNCardH323AllowCallsWithoutGatekeeper_Object = MibTableColumn
vsmVNCardH323AllowCallsWithoutGatekeeper = _VsmVNCardH323AllowCallsWithoutGatekeeper_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3, 1, 9),
    _VsmVNCardH323AllowCallsWithoutGatekeeper_Type()
)
vsmVNCardH323AllowCallsWithoutGatekeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNCardH323AllowCallsWithoutGatekeeper.setStatus("mandatory")


class _VsmVNCardH323GatekeeperMaxRetries_Type(Integer32):
    """Custom type vsmVNCardH323GatekeeperMaxRetries based on Integer32"""
    defaultValue = 4


_VsmVNCardH323GatekeeperMaxRetries_Object = MibTableColumn
vsmVNCardH323GatekeeperMaxRetries = _VsmVNCardH323GatekeeperMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3, 1, 10),
    _VsmVNCardH323GatekeeperMaxRetries_Type()
)
vsmVNCardH323GatekeeperMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNCardH323GatekeeperMaxRetries.setStatus("mandatory")


class _VsmVNCardH323EndpointRegType_Type(Integer32):
    """Custom type vsmVNCardH323EndpointRegType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gateway", 1),
          ("terminal", 2))
    )


_VsmVNCardH323EndpointRegType_Type.__name__ = "Integer32"
_VsmVNCardH323EndpointRegType_Object = MibTableColumn
vsmVNCardH323EndpointRegType = _VsmVNCardH323EndpointRegType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3, 1, 11),
    _VsmVNCardH323EndpointRegType_Type()
)
vsmVNCardH323EndpointRegType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNCardH323EndpointRegType.setStatus("mandatory")


class _VsmVNCardH323Notification_Type(VsmEnableDisabled):
    """Custom type vsmVNCardH323Notification based on VsmEnableDisabled"""


_VsmVNCardH323Notification_Object = MibTableColumn
vsmVNCardH323Notification = _VsmVNCardH323Notification_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 3, 1, 12),
    _VsmVNCardH323Notification_Type()
)
vsmVNCardH323Notification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNCardH323Notification.setStatus("deprecated")
_VsmVNCardH323GateKeeperPhoneGroupTable_Object = MibTable
vsmVNCardH323GateKeeperPhoneGroupTable = _VsmVNCardH323GateKeeperPhoneGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 4)
)
if mibBuilder.loadTexts:
    vsmVNCardH323GateKeeperPhoneGroupTable.setStatus("mandatory")
_VsmVNCardH323GateKeeperPhoneGroupEntry_Object = MibTableRow
vsmVNCardH323GateKeeperPhoneGroupEntry = _VsmVNCardH323GateKeeperPhoneGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 4, 1)
)
vsmVNCardH323GateKeeperPhoneGroupEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmCardSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmCardSubunitIndex"),
    (0, "XYLAN-VSM-MIB", "vsmPhoneGroupName"),
)
if mibBuilder.loadTexts:
    vsmVNCardH323GateKeeperPhoneGroupEntry.setStatus("mandatory")
_VsmVNCardH323GateKeeperPhoneGroupRowStatus_Type = RowStatus
_VsmVNCardH323GateKeeperPhoneGroupRowStatus_Object = MibTableColumn
vsmVNCardH323GateKeeperPhoneGroupRowStatus = _VsmVNCardH323GateKeeperPhoneGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 1, 4, 1, 1),
    _VsmVNCardH323GateKeeperPhoneGroupRowStatus_Type()
)
vsmVNCardH323GateKeeperPhoneGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmVNCardH323GateKeeperPhoneGroupRowStatus.setStatus("mandatory")
_VsmSignalingGroup_ObjectIdentity = ObjectIdentity
vsmSignalingGroup = _VsmSignalingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2)
)
_VsmSignalingTemplateTable_Object = MibTable
vsmSignalingTemplateTable = _VsmSignalingTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 1)
)
if mibBuilder.loadTexts:
    vsmSignalingTemplateTable.setStatus("mandatory")
_VsmSignalingTemplateEntry_Object = MibTableRow
vsmSignalingTemplateEntry = _VsmSignalingTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 1, 1)
)
vsmSignalingTemplateEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmSigTmplIndex"),
)
if mibBuilder.loadTexts:
    vsmSignalingTemplateEntry.setStatus("mandatory")
_VsmSigTmplIndex_Type = Integer32
_VsmSigTmplIndex_Object = MibTableColumn
vsmSigTmplIndex = _VsmSigTmplIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 1, 1, 1),
    _VsmSigTmplIndex_Type()
)
vsmSigTmplIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigTmplIndex.setStatus("mandatory")
_VsmSigTmplName_Type = DisplayString
_VsmSigTmplName_Object = MibTableColumn
vsmSigTmplName = _VsmSigTmplName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 1, 1, 2),
    _VsmSigTmplName_Type()
)
vsmSigTmplName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigTmplName.setStatus("deprecated")
_VsmSigTmplRowStatus_Type = RowStatus
_VsmSigTmplRowStatus_Object = MibTableColumn
vsmSigTmplRowStatus = _VsmSigTmplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 1, 1, 3),
    _VsmSigTmplRowStatus_Type()
)
vsmSigTmplRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigTmplRowStatus.setStatus("mandatory")
_VsmSigTmplEmCommonTable_Object = MibTable
vsmSigTmplEmCommonTable = _VsmSigTmplEmCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 2)
)
if mibBuilder.loadTexts:
    vsmSigTmplEmCommonTable.setStatus("mandatory")
_VsmSigTmplEmCommonEntry_Object = MibTableRow
vsmSigTmplEmCommonEntry = _VsmSigTmplEmCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 2, 1)
)
vsmSigTmplEmCommonEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmSigTmplIndex"),
)
if mibBuilder.loadTexts:
    vsmSigTmplEmCommonEntry.setStatus("mandatory")


class _VsmSigTmplEmCommonOffHookDebounce_Type(Integer32):
    """Custom type vsmSigTmplEmCommonOffHookDebounce based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_VsmSigTmplEmCommonOffHookDebounce_Type.__name__ = "Integer32"
_VsmSigTmplEmCommonOffHookDebounce_Object = MibTableColumn
vsmSigTmplEmCommonOffHookDebounce = _VsmSigTmplEmCommonOffHookDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 2, 1, 1),
    _VsmSigTmplEmCommonOffHookDebounce_Type()
)
vsmSigTmplEmCommonOffHookDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigTmplEmCommonOffHookDebounce.setStatus("deprecated")
_VsmSigTmplEmDelayTable_Object = MibTable
vsmSigTmplEmDelayTable = _VsmSigTmplEmDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 3)
)
if mibBuilder.loadTexts:
    vsmSigTmplEmDelayTable.setStatus("mandatory")
_VsmSigTmplEmDelayEntry_Object = MibTableRow
vsmSigTmplEmDelayEntry = _VsmSigTmplEmDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 3, 1)
)
vsmSigTmplEmDelayEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmSigTmplIndex"),
)
if mibBuilder.loadTexts:
    vsmSigTmplEmDelayEntry.setStatus("mandatory")


class _VsmSigTmplEmDelayInDelayDurMin_Type(Integer32):
    """Custom type vsmSigTmplEmDelayInDelayDurMin based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigTmplEmDelayInDelayDurMin_Type.__name__ = "Integer32"
_VsmSigTmplEmDelayInDelayDurMin_Object = MibTableColumn
vsmSigTmplEmDelayInDelayDurMin = _VsmSigTmplEmDelayInDelayDurMin_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 3, 1, 1),
    _VsmSigTmplEmDelayInDelayDurMin_Type()
)
vsmSigTmplEmDelayInDelayDurMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigTmplEmDelayInDelayDurMin.setStatus("deprecated")
_VsmSigTmplEmImmedTable_Object = MibTable
vsmSigTmplEmImmedTable = _VsmSigTmplEmImmedTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 4)
)
if mibBuilder.loadTexts:
    vsmSigTmplEmImmedTable.setStatus("mandatory")
_VsmSigTmplEmImmedEntry_Object = MibTableRow
vsmSigTmplEmImmedEntry = _VsmSigTmplEmImmedEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 4, 1)
)
vsmSigTmplEmImmedEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmSigTmplIndex"),
)
if mibBuilder.loadTexts:
    vsmSigTmplEmImmedEntry.setStatus("mandatory")


class _VsmSigTmplEmImmedGlareReport_Type(Integer32):
    """Custom type vsmSigTmplEmImmedGlareReport based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_VsmSigTmplEmImmedGlareReport_Type.__name__ = "Integer32"
_VsmSigTmplEmImmedGlareReport_Object = MibTableColumn
vsmSigTmplEmImmedGlareReport = _VsmSigTmplEmImmedGlareReport_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 4, 1, 1),
    _VsmSigTmplEmImmedGlareReport_Type()
)
vsmSigTmplEmImmedGlareReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigTmplEmImmedGlareReport.setStatus("deprecated")
_VsmSigTmplEmWinkTable_Object = MibTable
vsmSigTmplEmWinkTable = _VsmSigTmplEmWinkTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 5)
)
if mibBuilder.loadTexts:
    vsmSigTmplEmWinkTable.setStatus("mandatory")
_VsmSigTmplEmWinkEntry_Object = MibTableRow
vsmSigTmplEmWinkEntry = _VsmSigTmplEmWinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 5, 1)
)
vsmSigTmplEmWinkEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmSigTmplIndex"),
)
if mibBuilder.loadTexts:
    vsmSigTmplEmWinkEntry.setStatus("mandatory")


class _VsmSigTmplEmWinkInWinkWaitMin_Type(Integer32):
    """Custom type vsmSigTmplEmWinkInWinkWaitMin based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigTmplEmWinkInWinkWaitMin_Type.__name__ = "Integer32"
_VsmSigTmplEmWinkInWinkWaitMin_Object = MibTableColumn
vsmSigTmplEmWinkInWinkWaitMin = _VsmSigTmplEmWinkInWinkWaitMin_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 5, 1, 1),
    _VsmSigTmplEmWinkInWinkWaitMin_Type()
)
vsmSigTmplEmWinkInWinkWaitMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigTmplEmWinkInWinkWaitMin.setStatus("deprecated")
_VsmSigTmplFxoGSTable_Object = MibTable
vsmSigTmplFxoGSTable = _VsmSigTmplFxoGSTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 6)
)
if mibBuilder.loadTexts:
    vsmSigTmplFxoGSTable.setStatus("mandatory")
_VsmSigTmplFxoGSEntry_Object = MibTableRow
vsmSigTmplFxoGSEntry = _VsmSigTmplFxoGSEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 6, 1)
)
vsmSigTmplFxoGSEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmSigTmplIndex"),
)
if mibBuilder.loadTexts:
    vsmSigTmplFxoGSEntry.setStatus("mandatory")


class _VsmSigTmplFxoGSConnectionLoopOpenDebounce_Type(Integer32):
    """Custom type vsmSigTmplFxoGSConnectionLoopOpenDebounce based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_VsmSigTmplFxoGSConnectionLoopOpenDebounce_Type.__name__ = "Integer32"
_VsmSigTmplFxoGSConnectionLoopOpenDebounce_Object = MibTableColumn
vsmSigTmplFxoGSConnectionLoopOpenDebounce = _VsmSigTmplFxoGSConnectionLoopOpenDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 6, 1, 1),
    _VsmSigTmplFxoGSConnectionLoopOpenDebounce_Type()
)
vsmSigTmplFxoGSConnectionLoopOpenDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigTmplFxoGSConnectionLoopOpenDebounce.setStatus("deprecated")
_VsmSigTmplFxoLSTable_Object = MibTable
vsmSigTmplFxoLSTable = _VsmSigTmplFxoLSTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 7)
)
if mibBuilder.loadTexts:
    vsmSigTmplFxoLSTable.setStatus("mandatory")
_VsmSigTmplFxoLSEntry_Object = MibTableRow
vsmSigTmplFxoLSEntry = _VsmSigTmplFxoLSEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 7, 1)
)
vsmSigTmplFxoLSEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmSigTmplIndex"),
)
if mibBuilder.loadTexts:
    vsmSigTmplFxoLSEntry.setStatus("mandatory")


class _VsmSigTmplFxoLSRingingDebounce_Type(Integer32):
    """Custom type vsmSigTmplFxoLSRingingDebounce based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VsmSigTmplFxoLSRingingDebounce_Type.__name__ = "Integer32"
_VsmSigTmplFxoLSRingingDebounce_Object = MibTableColumn
vsmSigTmplFxoLSRingingDebounce = _VsmSigTmplFxoLSRingingDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 7, 1, 1),
    _VsmSigTmplFxoLSRingingDebounce_Type()
)
vsmSigTmplFxoLSRingingDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigTmplFxoLSRingingDebounce.setStatus("deprecated")
_VsmSigTmplFxsGSTable_Object = MibTable
vsmSigTmplFxsGSTable = _VsmSigTmplFxsGSTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 8)
)
if mibBuilder.loadTexts:
    vsmSigTmplFxsGSTable.setStatus("mandatory")
_VsmSigTmplFxsGSEntry_Object = MibTableRow
vsmSigTmplFxsGSEntry = _VsmSigTmplFxsGSEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 8, 1)
)
vsmSigTmplFxsGSEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmSigTmplIndex"),
)
if mibBuilder.loadTexts:
    vsmSigTmplFxsGSEntry.setStatus("mandatory")


class _VsmSigTmplFxsGSSeizeDetect_Type(Integer32):
    """Custom type vsmSigTmplFxsGSSeizeDetect based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_VsmSigTmplFxsGSSeizeDetect_Type.__name__ = "Integer32"
_VsmSigTmplFxsGSSeizeDetect_Object = MibTableColumn
vsmSigTmplFxsGSSeizeDetect = _VsmSigTmplFxsGSSeizeDetect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 8, 1, 1),
    _VsmSigTmplFxsGSSeizeDetect_Type()
)
vsmSigTmplFxsGSSeizeDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigTmplFxsGSSeizeDetect.setStatus("deprecated")
_VsmSigTmplFxsLSTable_Object = MibTable
vsmSigTmplFxsLSTable = _VsmSigTmplFxsLSTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 9)
)
if mibBuilder.loadTexts:
    vsmSigTmplFxsLSTable.setStatus("mandatory")
_VsmSigTmplFxsLSEntry_Object = MibTableRow
vsmSigTmplFxsLSEntry = _VsmSigTmplFxsLSEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 9, 1)
)
vsmSigTmplFxsLSEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmSigTmplIndex"),
)
if mibBuilder.loadTexts:
    vsmSigTmplFxsLSEntry.setStatus("mandatory")


class _VsmSigTmplFxsLSOffHookDebounce_Type(Integer32):
    """Custom type vsmSigTmplFxsLSOffHookDebounce based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VsmSigTmplFxsLSOffHookDebounce_Type.__name__ = "Integer32"
_VsmSigTmplFxsLSOffHookDebounce_Object = MibTableColumn
vsmSigTmplFxsLSOffHookDebounce = _VsmSigTmplFxsLSOffHookDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 9, 1, 1),
    _VsmSigTmplFxsLSOffHookDebounce_Type()
)
vsmSigTmplFxsLSOffHookDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigTmplFxsLSOffHookDebounce.setStatus("deprecated")
_VsmSignalingChannelTable_Object = MibTable
vsmSignalingChannelTable = _VsmSignalingChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10)
)
if mibBuilder.loadTexts:
    vsmSignalingChannelTable.setStatus("mandatory")
_VsmSignalingChannelEntry_Object = MibTableRow
vsmSignalingChannelEntry = _VsmSignalingChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1)
)
vsmSignalingChannelEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmSignalingChannelEntry.setStatus("mandatory")


class _VsmSigChanProtocol_Type(Integer32):
    """Custom type vsmSigChanProtocol based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("emDelayStart", 1),
          ("emImmedStart", 2),
          ("emWinkStart", 3),
          ("fxoGroundStart", 4),
          ("fxoLoopStart", 6),
          ("fxsGroundStart", 5),
          ("fxsLoopStart", 7),
          ("isdn", 8))
    )


_VsmSigChanProtocol_Type.__name__ = "Integer32"
_VsmSigChanProtocol_Object = MibTableColumn
vsmSigChanProtocol = _VsmSigChanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 1),
    _VsmSigChanProtocol_Type()
)
vsmSigChanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanProtocol.setStatus("mandatory")


class _VsmSigChanCallerIdName_Type(Integer32):
    """Custom type vsmSigChanCallerIdName based on Integer32"""
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
        *(("available", 3),
          ("private", 1),
          ("unavailable", 2))
    )


_VsmSigChanCallerIdName_Type.__name__ = "Integer32"
_VsmSigChanCallerIdName_Object = MibTableColumn
vsmSigChanCallerIdName = _VsmSigChanCallerIdName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 2),
    _VsmSigChanCallerIdName_Type()
)
vsmSigChanCallerIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanCallerIdName.setStatus("mandatory")
_VsmSigChanCallerIdNameStr_Type = DisplayString
_VsmSigChanCallerIdNameStr_Object = MibTableColumn
vsmSigChanCallerIdNameStr = _VsmSigChanCallerIdNameStr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 3),
    _VsmSigChanCallerIdNameStr_Type()
)
vsmSigChanCallerIdNameStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanCallerIdNameStr.setStatus("mandatory")


class _VsmSigChanCallerIdNumber_Type(Integer32):
    """Custom type vsmSigChanCallerIdNumber based on Integer32"""
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
        *(("available", 3),
          ("private", 1),
          ("unavailable", 2))
    )


_VsmSigChanCallerIdNumber_Type.__name__ = "Integer32"
_VsmSigChanCallerIdNumber_Object = MibTableColumn
vsmSigChanCallerIdNumber = _VsmSigChanCallerIdNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 4),
    _VsmSigChanCallerIdNumber_Type()
)
vsmSigChanCallerIdNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanCallerIdNumber.setStatus("mandatory")
_VsmSigChanCallerIdNumberStr_Type = DisplayString
_VsmSigChanCallerIdNumberStr_Object = MibTableColumn
vsmSigChanCallerIdNumberStr = _VsmSigChanCallerIdNumberStr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 5),
    _VsmSigChanCallerIdNumberStr_Type()
)
vsmSigChanCallerIdNumberStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanCallerIdNumberStr.setStatus("mandatory")


class _VsmSigChanToneTable_Type(Integer32):
    """Custom type vsmSigChanToneTable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ringing", 1),
          ("silence", 2))
    )


_VsmSigChanToneTable_Type.__name__ = "Integer32"
_VsmSigChanToneTable_Object = MibTableColumn
vsmSigChanToneTable = _VsmSigChanToneTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 6),
    _VsmSigChanToneTable_Type()
)
vsmSigChanToneTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanToneTable.setStatus("mandatory")


class _VsmSigChanOutWait_Type(Integer32):
    """Custom type vsmSigChanOutWait based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_VsmSigChanOutWait_Type.__name__ = "Integer32"
_VsmSigChanOutWait_Object = MibTableColumn
vsmSigChanOutWait = _VsmSigChanOutWait_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 7),
    _VsmSigChanOutWait_Type()
)
vsmSigChanOutWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOutWait.setStatus("mandatory")


class _VsmSigChanOutToneDigitDur_Type(Integer32):
    """Custom type vsmSigChanOutToneDigitDur based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 2000),
    )


_VsmSigChanOutToneDigitDur_Type.__name__ = "Integer32"
_VsmSigChanOutToneDigitDur_Object = MibTableColumn
vsmSigChanOutToneDigitDur = _VsmSigChanOutToneDigitDur_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 8),
    _VsmSigChanOutToneDigitDur_Type()
)
vsmSigChanOutToneDigitDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOutToneDigitDur.setStatus("mandatory")


class _VsmSigChanOutToneInterDigitDur_Type(Integer32):
    """Custom type vsmSigChanOutToneInterDigitDur based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 2000),
    )


_VsmSigChanOutToneInterDigitDur_Type.__name__ = "Integer32"
_VsmSigChanOutToneInterDigitDur_Object = MibTableColumn
vsmSigChanOutToneInterDigitDur = _VsmSigChanOutToneInterDigitDur_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 9),
    _VsmSigChanOutToneInterDigitDur_Type()
)
vsmSigChanOutToneInterDigitDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOutToneInterDigitDur.setStatus("mandatory")


class _VsmSigChanUnused_Type(Integer32):
    """Custom type vsmSigChanUnused based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_VsmSigChanUnused_Type.__name__ = "Integer32"
_VsmSigChanUnused_Object = MibTableColumn
vsmSigChanUnused = _VsmSigChanUnused_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 10),
    _VsmSigChanUnused_Type()
)
vsmSigChanUnused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanUnused.setStatus("deprecated")


class _VsmSigChanCallLimitCtrl_Type(VsmEnableDisabled):
    """Custom type vsmSigChanCallLimitCtrl based on VsmEnableDisabled"""


_VsmSigChanCallLimitCtrl_Object = MibTableColumn
vsmSigChanCallLimitCtrl = _VsmSigChanCallLimitCtrl_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 11),
    _VsmSigChanCallLimitCtrl_Type()
)
vsmSigChanCallLimitCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanCallLimitCtrl.setStatus("mandatory")


class _VsmSigChanCallLimit_Type(Integer32):
    """Custom type vsmSigChanCallLimit based on Integer32"""
    defaultValue = 65534

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_VsmSigChanCallLimit_Type.__name__ = "Integer32"
_VsmSigChanCallLimit_Object = MibTableColumn
vsmSigChanCallLimit = _VsmSigChanCallLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 12),
    _VsmSigChanCallLimit_Type()
)
vsmSigChanCallLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanCallLimit.setStatus("mandatory")


class _VsmSigChanAnswerWaitLimitCtrl_Type(VsmEnableDisabled):
    """Custom type vsmSigChanAnswerWaitLimitCtrl based on VsmEnableDisabled"""


_VsmSigChanAnswerWaitLimitCtrl_Object = MibTableColumn
vsmSigChanAnswerWaitLimitCtrl = _VsmSigChanAnswerWaitLimitCtrl_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 13),
    _VsmSigChanAnswerWaitLimitCtrl_Type()
)
vsmSigChanAnswerWaitLimitCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanAnswerWaitLimitCtrl.setStatus("mandatory")


class _VsmSigChanAnswerWaitLimit_Type(Integer32):
    """Custom type vsmSigChanAnswerWaitLimit based on Integer32"""
    defaultValue = 65534

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_VsmSigChanAnswerWaitLimit_Type.__name__ = "Integer32"
_VsmSigChanAnswerWaitLimit_Object = MibTableColumn
vsmSigChanAnswerWaitLimit = _VsmSigChanAnswerWaitLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 14),
    _VsmSigChanAnswerWaitLimit_Type()
)
vsmSigChanAnswerWaitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanAnswerWaitLimit.setStatus("mandatory")


class _VsmSigChanHangupWaitLimitCtrl_Type(VsmEnableDisabled):
    """Custom type vsmSigChanHangupWaitLimitCtrl based on VsmEnableDisabled"""


_VsmSigChanHangupWaitLimitCtrl_Object = MibTableColumn
vsmSigChanHangupWaitLimitCtrl = _VsmSigChanHangupWaitLimitCtrl_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 15),
    _VsmSigChanHangupWaitLimitCtrl_Type()
)
vsmSigChanHangupWaitLimitCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanHangupWaitLimitCtrl.setStatus("mandatory")


class _VsmSigChanHangupWaitLimit_Type(Integer32):
    """Custom type vsmSigChanHangupWaitLimit based on Integer32"""
    defaultValue = 65534

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_VsmSigChanHangupWaitLimit_Type.__name__ = "Integer32"
_VsmSigChanHangupWaitLimit_Object = MibTableColumn
vsmSigChanHangupWaitLimit = _VsmSigChanHangupWaitLimit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 16),
    _VsmSigChanHangupWaitLimit_Type()
)
vsmSigChanHangupWaitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanHangupWaitLimit.setStatus("mandatory")


class _VsmSigChanFaxHoldoverDelay_Type(Integer32):
    """Custom type vsmSigChanFaxHoldoverDelay based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_VsmSigChanFaxHoldoverDelay_Type.__name__ = "Integer32"
_VsmSigChanFaxHoldoverDelay_Object = MibTableColumn
vsmSigChanFaxHoldoverDelay = _VsmSigChanFaxHoldoverDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 17),
    _VsmSigChanFaxHoldoverDelay_Type()
)
vsmSigChanFaxHoldoverDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFaxHoldoverDelay.setStatus("mandatory")


class _VsmSigChanCompanding_Type(Integer32):
    """Custom type vsmSigChanCompanding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 1),
          ("mulaw", 2))
    )


_VsmSigChanCompanding_Type.__name__ = "Integer32"
_VsmSigChanCompanding_Object = MibTableColumn
vsmSigChanCompanding = _VsmSigChanCompanding_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 18),
    _VsmSigChanCompanding_Type()
)
vsmSigChanCompanding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanCompanding.setStatus("mandatory")


class _VsmSigChanReceiveGain_Type(Integer32):
    """Custom type vsmSigChanReceiveGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-14, 14),
    )


_VsmSigChanReceiveGain_Type.__name__ = "Integer32"
_VsmSigChanReceiveGain_Object = MibTableColumn
vsmSigChanReceiveGain = _VsmSigChanReceiveGain_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 19),
    _VsmSigChanReceiveGain_Type()
)
vsmSigChanReceiveGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanReceiveGain.setStatus("mandatory")


class _VsmSigChanTransmitGain_Type(Integer32):
    """Custom type vsmSigChanTransmitGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-14, 14),
    )


_VsmSigChanTransmitGain_Type.__name__ = "Integer32"
_VsmSigChanTransmitGain_Object = MibTableColumn
vsmSigChanTransmitGain = _VsmSigChanTransmitGain_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 20),
    _VsmSigChanTransmitGain_Type()
)
vsmSigChanTransmitGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanTransmitGain.setStatus("mandatory")


class _VsmSigChanIdleNoise_Type(Integer32):
    """Custom type vsmSigChanIdleNoise based on Integer32"""
    defaultValue = 7000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7000, 7000),
    )


_VsmSigChanIdleNoise_Type.__name__ = "Integer32"
_VsmSigChanIdleNoise_Object = MibTableColumn
vsmSigChanIdleNoise = _VsmSigChanIdleNoise_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 21),
    _VsmSigChanIdleNoise_Type()
)
vsmSigChanIdleNoise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanIdleNoise.setStatus("mandatory")


class _VsmSigChanOverrideInBandCallProgressTones_Type(VsmEnableDisabled):
    """Custom type vsmSigChanOverrideInBandCallProgressTones based on VsmEnableDisabled"""


_VsmSigChanOverrideInBandCallProgressTones_Object = MibTableColumn
vsmSigChanOverrideInBandCallProgressTones = _VsmSigChanOverrideInBandCallProgressTones_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 22),
    _VsmSigChanOverrideInBandCallProgressTones_Type()
)
vsmSigChanOverrideInBandCallProgressTones.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOverrideInBandCallProgressTones.setStatus("mandatory")


class _VsmSigChanOverrideInBandCodecSwitching_Type(VsmEnableDisabled):
    """Custom type vsmSigChanOverrideInBandCodecSwitching based on VsmEnableDisabled"""


_VsmSigChanOverrideInBandCodecSwitching_Object = MibTableColumn
vsmSigChanOverrideInBandCodecSwitching = _VsmSigChanOverrideInBandCodecSwitching_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 23),
    _VsmSigChanOverrideInBandCodecSwitching_Type()
)
vsmSigChanOverrideInBandCodecSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOverrideInBandCodecSwitching.setStatus("mandatory")


class _VsmSigChanOverridePSUCodecSwitching_Type(VsmEnableDisabled):
    """Custom type vsmSigChanOverridePSUCodecSwitching based on VsmEnableDisabled"""


_VsmSigChanOverridePSUCodecSwitching_Object = MibTableColumn
vsmSigChanOverridePSUCodecSwitching = _VsmSigChanOverridePSUCodecSwitching_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 24),
    _VsmSigChanOverridePSUCodecSwitching_Type()
)
vsmSigChanOverridePSUCodecSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOverridePSUCodecSwitching.setStatus("mandatory")


class _VsmSigChanOverrideNetworkOverlapDialing_Type(VsmEnableDisabled):
    """Custom type vsmSigChanOverrideNetworkOverlapDialing based on VsmEnableDisabled"""


_VsmSigChanOverrideNetworkOverlapDialing_Object = MibTableColumn
vsmSigChanOverrideNetworkOverlapDialing = _VsmSigChanOverrideNetworkOverlapDialing_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 25),
    _VsmSigChanOverrideNetworkOverlapDialing_Type()
)
vsmSigChanOverrideNetworkOverlapDialing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOverrideNetworkOverlapDialing.setStatus("mandatory")


class _VsmSigChanOverrideFullCallProgressTones_Type(VsmEnableDisabled):
    """Custom type vsmSigChanOverrideFullCallProgressTones based on VsmEnableDisabled"""


_VsmSigChanOverrideFullCallProgressTones_Object = MibTableColumn
vsmSigChanOverrideFullCallProgressTones = _VsmSigChanOverrideFullCallProgressTones_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 26),
    _VsmSigChanOverrideFullCallProgressTones_Type()
)
vsmSigChanOverrideFullCallProgressTones.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOverrideFullCallProgressTones.setStatus("mandatory")


class _VsmSigChanOverrideRingBack_Type(VsmEnableDisabled):
    """Custom type vsmSigChanOverrideRingBack based on VsmEnableDisabled"""


_VsmSigChanOverrideRingBack_Object = MibTableColumn
vsmSigChanOverrideRingBack = _VsmSigChanOverrideRingBack_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 27),
    _VsmSigChanOverrideRingBack_Type()
)
vsmSigChanOverrideRingBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOverrideRingBack.setStatus("mandatory")


class _VsmSigChanOverrideInfoElementTransport_Type(VsmEnableDisabled):
    """Custom type vsmSigChanOverrideInfoElementTransport based on VsmEnableDisabled"""


_VsmSigChanOverrideInfoElementTransport_Object = MibTableColumn
vsmSigChanOverrideInfoElementTransport = _VsmSigChanOverrideInfoElementTransport_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 28),
    _VsmSigChanOverrideInfoElementTransport_Type()
)
vsmSigChanOverrideInfoElementTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOverrideInfoElementTransport.setStatus("mandatory")


class _VsmSigChanOverrideQSIGInfoElementTransport_Type(VsmEnableDisabled):
    """Custom type vsmSigChanOverrideQSIGInfoElementTransport based on VsmEnableDisabled"""


_VsmSigChanOverrideQSIGInfoElementTransport_Object = MibTableColumn
vsmSigChanOverrideQSIGInfoElementTransport = _VsmSigChanOverrideQSIGInfoElementTransport_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 29),
    _VsmSigChanOverrideQSIGInfoElementTransport_Type()
)
vsmSigChanOverrideQSIGInfoElementTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOverrideQSIGInfoElementTransport.setStatus("mandatory")


class _VsmSigChanOverrideDataSetup_Type(VsmOnOff):
    """Custom type vsmSigChanOverrideDataSetup based on VsmOnOff"""


_VsmSigChanOverrideDataSetup_Object = MibTableColumn
vsmSigChanOverrideDataSetup = _VsmSigChanOverrideDataSetup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 30),
    _VsmSigChanOverrideDataSetup_Type()
)
vsmSigChanOverrideDataSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOverrideDataSetup.setStatus("mandatory")


class _VsmSigChanOverrideVoiceSetup_Type(VsmOnOff):
    """Custom type vsmSigChanOverrideVoiceSetup based on VsmOnOff"""


_VsmSigChanOverrideVoiceSetup_Object = MibTableColumn
vsmSigChanOverrideVoiceSetup = _VsmSigChanOverrideVoiceSetup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 31),
    _VsmSigChanOverrideVoiceSetup_Type()
)
vsmSigChanOverrideVoiceSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOverrideVoiceSetup.setStatus("mandatory")


class _VsmSigChanOverrideFAXSetup_Type(VsmOnOff):
    """Custom type vsmSigChanOverrideFAXSetup based on VsmOnOff"""


_VsmSigChanOverrideFAXSetup_Object = MibTableColumn
vsmSigChanOverrideFAXSetup = _VsmSigChanOverrideFAXSetup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 32),
    _VsmSigChanOverrideFAXSetup_Type()
)
vsmSigChanOverrideFAXSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOverrideFAXSetup.setStatus("mandatory")


class _VsmSigChanOverrideModemSetup_Type(VsmOnOff):
    """Custom type vsmSigChanOverrideModemSetup based on VsmOnOff"""


_VsmSigChanOverrideModemSetup_Object = MibTableColumn
vsmSigChanOverrideModemSetup = _VsmSigChanOverrideModemSetup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 33),
    _VsmSigChanOverrideModemSetup_Type()
)
vsmSigChanOverrideModemSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOverrideModemSetup.setStatus("mandatory")


class _VsmSigChanCallProgressToneDetControl_Type(Integer32):
    """Custom type vsmSigChanCallProgressToneDetControl based on Integer32"""
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
        *(("off", 1),
          ("on", 2),
          ("relative", 3))
    )


_VsmSigChanCallProgressToneDetControl_Type.__name__ = "Integer32"
_VsmSigChanCallProgressToneDetControl_Object = MibTableColumn
vsmSigChanCallProgressToneDetControl = _VsmSigChanCallProgressToneDetControl_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 34),
    _VsmSigChanCallProgressToneDetControl_Type()
)
vsmSigChanCallProgressToneDetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanCallProgressToneDetControl.setStatus("mandatory")


class _VsmSigChanCallProgressToneDetCfg_Type(Integer32):
    """Custom type vsmSigChanCallProgressToneDetCfg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("default", 1))
    )


_VsmSigChanCallProgressToneDetCfg_Type.__name__ = "Integer32"
_VsmSigChanCallProgressToneDetCfg_Object = MibTableColumn
vsmSigChanCallProgressToneDetCfg = _VsmSigChanCallProgressToneDetCfg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 35),
    _VsmSigChanCallProgressToneDetCfg_Type()
)
vsmSigChanCallProgressToneDetCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanCallProgressToneDetCfg.setStatus("mandatory")
_VsmSigChanAssignTmplName_Type = DisplayString
_VsmSigChanAssignTmplName_Object = MibTableColumn
vsmSigChanAssignTmplName = _VsmSigChanAssignTmplName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 36),
    _VsmSigChanAssignTmplName_Type()
)
vsmSigChanAssignTmplName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanAssignTmplName.setStatus("mandatory")


class _VsmSigChanAssignTmplStatus_Type(Integer32):
    """Custom type vsmSigChanAssignTmplStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("assign", 1)
    )


_VsmSigChanAssignTmplStatus_Type.__name__ = "Integer32"
_VsmSigChanAssignTmplStatus_Object = MibTableColumn
vsmSigChanAssignTmplStatus = _VsmSigChanAssignTmplStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 37),
    _VsmSigChanAssignTmplStatus_Type()
)
vsmSigChanAssignTmplStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vsmSigChanAssignTmplStatus.setStatus("mandatory")


class _VsmSigChanOutDialType_Type(Integer32):
    """Custom type vsmSigChanOutDialType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pulse", 2),
          ("tone", 1))
    )


_VsmSigChanOutDialType_Type.__name__ = "Integer32"
_VsmSigChanOutDialType_Object = MibTableColumn
vsmSigChanOutDialType = _VsmSigChanOutDialType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 38),
    _VsmSigChanOutDialType_Type()
)
vsmSigChanOutDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanOutDialType.setStatus("mandatory")


class _VsmSigChanV18ToneDetThHangTime_Type(Integer32):
    """Custom type vsmSigChanV18ToneDetThHangTime based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32767),
    )


_VsmSigChanV18ToneDetThHangTime_Type.__name__ = "Integer32"
_VsmSigChanV18ToneDetThHangTime_Object = MibTableColumn
vsmSigChanV18ToneDetThHangTime = _VsmSigChanV18ToneDetThHangTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 39),
    _VsmSigChanV18ToneDetThHangTime_Type()
)
vsmSigChanV18ToneDetThHangTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanV18ToneDetThHangTime.setStatus("mandatory")


class _VsmSigChanV18ToneDetThLevel_Type(Integer32):
    """Custom type vsmSigChanV18ToneDetThLevel based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, -15),
    )


_VsmSigChanV18ToneDetThLevel_Type.__name__ = "Integer32"
_VsmSigChanV18ToneDetThLevel_Object = MibTableColumn
vsmSigChanV18ToneDetThLevel = _VsmSigChanV18ToneDetThLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 40),
    _VsmSigChanV18ToneDetThLevel_Type()
)
vsmSigChanV18ToneDetThLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanV18ToneDetThLevel.setStatus("mandatory")


class _VsmSigChanV18ToneDetThFraction_Type(Integer32):
    """Custom type vsmSigChanV18ToneDetThFraction based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_VsmSigChanV18ToneDetThFraction_Type.__name__ = "Integer32"
_VsmSigChanV18ToneDetThFraction_Object = MibTableColumn
vsmSigChanV18ToneDetThFraction = _VsmSigChanV18ToneDetThFraction_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 41),
    _VsmSigChanV18ToneDetThFraction_Type()
)
vsmSigChanV18ToneDetThFraction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanV18ToneDetThFraction.setStatus("mandatory")


class _VsmSigChanSinFreqToneDetThLev_Type(Integer32):
    """Custom type vsmSigChanSinFreqToneDetThLev based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, -15),
    )


_VsmSigChanSinFreqToneDetThLev_Type.__name__ = "Integer32"
_VsmSigChanSinFreqToneDetThLev_Object = MibTableColumn
vsmSigChanSinFreqToneDetThLev = _VsmSigChanSinFreqToneDetThLev_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 42),
    _VsmSigChanSinFreqToneDetThLev_Type()
)
vsmSigChanSinFreqToneDetThLev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanSinFreqToneDetThLev.setStatus("mandatory")


class _VsmSigChanSinFreqToneDetThTime_Type(Integer32):
    """Custom type vsmSigChanSinFreqToneDetThTime based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsmSigChanSinFreqToneDetThTime_Type.__name__ = "Integer32"
_VsmSigChanSinFreqToneDetThTime_Object = MibTableColumn
vsmSigChanSinFreqToneDetThTime = _VsmSigChanSinFreqToneDetThTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 43),
    _VsmSigChanSinFreqToneDetThTime_Type()
)
vsmSigChanSinFreqToneDetThTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanSinFreqToneDetThTime.setStatus("mandatory")


class _VsmSigChanEchoCancelNonSens_Type(Integer32):
    """Custom type vsmSigChanEchoCancelNonSens based on Integer32"""
    defaultValue = 327

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_VsmSigChanEchoCancelNonSens_Type.__name__ = "Integer32"
_VsmSigChanEchoCancelNonSens_Object = MibTableColumn
vsmSigChanEchoCancelNonSens = _VsmSigChanEchoCancelNonSens_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 44),
    _VsmSigChanEchoCancelNonSens_Type()
)
vsmSigChanEchoCancelNonSens.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEchoCancelNonSens.setStatus("mandatory")


class _VsmSigChanAcousticEchoCancellerMode_Type(VsmEnableDisabled):
    """Custom type vsmSigChanAcousticEchoCancellerMode based on VsmEnableDisabled"""


_VsmSigChanAcousticEchoCancellerMode_Object = MibTableColumn
vsmSigChanAcousticEchoCancellerMode = _VsmSigChanAcousticEchoCancellerMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 45),
    _VsmSigChanAcousticEchoCancellerMode_Type()
)
vsmSigChanAcousticEchoCancellerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanAcousticEchoCancellerMode.setStatus("mandatory")


class _VsmSigChanAcouEchoCanNonProc_Type(VsmEnableDisabled):
    """Custom type vsmSigChanAcouEchoCanNonProc based on VsmEnableDisabled"""


_VsmSigChanAcouEchoCanNonProc_Object = MibTableColumn
vsmSigChanAcouEchoCanNonProc = _VsmSigChanAcouEchoCanNonProc_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 46),
    _VsmSigChanAcouEchoCanNonProc_Type()
)
vsmSigChanAcouEchoCanNonProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanAcouEchoCanNonProc.setStatus("mandatory")


class _VsmSigChanAcEchoCanSetSpGain_Type(Integer32):
    """Custom type vsmSigChanAcEchoCanSetSpGain based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_VsmSigChanAcEchoCanSetSpGain_Type.__name__ = "Integer32"
_VsmSigChanAcEchoCanSetSpGain_Object = MibTableColumn
vsmSigChanAcEchoCanSetSpGain = _VsmSigChanAcEchoCanSetSpGain_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 47),
    _VsmSigChanAcEchoCanSetSpGain_Type()
)
vsmSigChanAcEchoCanSetSpGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanAcEchoCanSetSpGain.setStatus("mandatory")


class _VsmSigChanAcEchoCanFreeSpGain_Type(Integer32):
    """Custom type vsmSigChanAcEchoCanFreeSpGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_VsmSigChanAcEchoCanFreeSpGain_Type.__name__ = "Integer32"
_VsmSigChanAcEchoCanFreeSpGain_Object = MibTableColumn
vsmSigChanAcEchoCanFreeSpGain = _VsmSigChanAcEchoCanFreeSpGain_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 48),
    _VsmSigChanAcEchoCanFreeSpGain_Type()
)
vsmSigChanAcEchoCanFreeSpGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanAcEchoCanFreeSpGain.setStatus("mandatory")


class _VsmSigChanAcousticEchoCanOper_Type(Integer32):
    """Custom type vsmSigChanAcousticEchoCanOper based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("handset", 1),
          ("handsfree", 2))
    )


_VsmSigChanAcousticEchoCanOper_Type.__name__ = "Integer32"
_VsmSigChanAcousticEchoCanOper_Object = MibTableColumn
vsmSigChanAcousticEchoCanOper = _VsmSigChanAcousticEchoCanOper_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 49),
    _VsmSigChanAcousticEchoCanOper_Type()
)
vsmSigChanAcousticEchoCanOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanAcousticEchoCanOper.setStatus("mandatory")


class _VsmSigChanFxsLSCadenceCoefficient_Type(Integer32):
    """Custom type vsmSigChanFxsLSCadenceCoefficient based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("europe", 2),
          ("northAmerica", 1))
    )


_VsmSigChanFxsLSCadenceCoefficient_Type.__name__ = "Integer32"
_VsmSigChanFxsLSCadenceCoefficient_Object = MibTableColumn
vsmSigChanFxsLSCadenceCoefficient = _VsmSigChanFxsLSCadenceCoefficient_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 50),
    _VsmSigChanFxsLSCadenceCoefficient_Type()
)
vsmSigChanFxsLSCadenceCoefficient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsLSCadenceCoefficient.setStatus("mandatory")


class _VsmSigChanFxsLSRingId_Type(Integer32):
    """Custom type vsmSigChanFxsLSRingId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("five", 7),
          ("four", 6),
          ("one", 3),
          ("seven", 9),
          ("six", 8),
          ("three", 5),
          ("two", 4),
          ("zero", 2))
    )


_VsmSigChanFxsLSRingId_Type.__name__ = "Integer32"
_VsmSigChanFxsLSRingId_Object = MibTableColumn
vsmSigChanFxsLSRingId = _VsmSigChanFxsLSRingId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 51),
    _VsmSigChanFxsLSRingId_Type()
)
vsmSigChanFxsLSRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsLSRingId.setStatus("mandatory")


class _VsmSigChanFxsGSCadenceCoefficient_Type(Integer32):
    """Custom type vsmSigChanFxsGSCadenceCoefficient based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("europe", 2),
          ("northAmerica", 1))
    )


_VsmSigChanFxsGSCadenceCoefficient_Type.__name__ = "Integer32"
_VsmSigChanFxsGSCadenceCoefficient_Object = MibTableColumn
vsmSigChanFxsGSCadenceCoefficient = _VsmSigChanFxsGSCadenceCoefficient_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 52),
    _VsmSigChanFxsGSCadenceCoefficient_Type()
)
vsmSigChanFxsGSCadenceCoefficient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsGSCadenceCoefficient.setStatus("mandatory")


class _VsmSigChanFxsGSRingId_Type(Integer32):
    """Custom type vsmSigChanFxsGSRingId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("five", 7),
          ("four", 6),
          ("one", 3),
          ("seven", 9),
          ("six", 8),
          ("three", 5),
          ("two", 4),
          ("zero", 2))
    )


_VsmSigChanFxsGSRingId_Type.__name__ = "Integer32"
_VsmSigChanFxsGSRingId_Object = MibTableColumn
vsmSigChanFxsGSRingId = _VsmSigChanFxsGSRingId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 10, 1, 53),
    _VsmSigChanFxsGSRingId_Type()
)
vsmSigChanFxsGSRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsGSRingId.setStatus("mandatory")
_VsmSigChanEmCommonTable_Object = MibTable
vsmSigChanEmCommonTable = _VsmSigChanEmCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 11)
)
if mibBuilder.loadTexts:
    vsmSigChanEmCommonTable.setStatus("mandatory")
_VsmSigChanEmCommonEntry_Object = MibTableRow
vsmSigChanEmCommonEntry = _VsmSigChanEmCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 11, 1)
)
vsmSigChanEmCommonEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmSigChanEmCommonEntry.setStatus("mandatory")


class _VsmSigChanEmCommonOffHookDebounce_Type(Integer32):
    """Custom type vsmSigChanEmCommonOffHookDebounce based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_VsmSigChanEmCommonOffHookDebounce_Type.__name__ = "Integer32"
_VsmSigChanEmCommonOffHookDebounce_Object = MibTableColumn
vsmSigChanEmCommonOffHookDebounce = _VsmSigChanEmCommonOffHookDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 11, 1, 1),
    _VsmSigChanEmCommonOffHookDebounce_Type()
)
vsmSigChanEmCommonOffHookDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmCommonOffHookDebounce.setStatus("mandatory")


class _VsmSigChanEmCommonOnHookDebounce_Type(Integer32):
    """Custom type vsmSigChanEmCommonOnHookDebounce based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_VsmSigChanEmCommonOnHookDebounce_Type.__name__ = "Integer32"
_VsmSigChanEmCommonOnHookDebounce_Object = MibTableColumn
vsmSigChanEmCommonOnHookDebounce = _VsmSigChanEmCommonOnHookDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 11, 1, 2),
    _VsmSigChanEmCommonOnHookDebounce_Type()
)
vsmSigChanEmCommonOnHookDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmCommonOnHookDebounce.setStatus("mandatory")


class _VsmSigChanEmCommonSeizeDetect_Type(Integer32):
    """Custom type vsmSigChanEmCommonSeizeDetect based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5000),
    )


_VsmSigChanEmCommonSeizeDetect_Type.__name__ = "Integer32"
_VsmSigChanEmCommonSeizeDetect_Object = MibTableColumn
vsmSigChanEmCommonSeizeDetect = _VsmSigChanEmCommonSeizeDetect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 11, 1, 3),
    _VsmSigChanEmCommonSeizeDetect_Type()
)
vsmSigChanEmCommonSeizeDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmCommonSeizeDetect.setStatus("mandatory")


class _VsmSigChanEmCommonClearDetect_Type(Integer32):
    """Custom type vsmSigChanEmCommonClearDetect based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5000),
    )


_VsmSigChanEmCommonClearDetect_Type.__name__ = "Integer32"
_VsmSigChanEmCommonClearDetect_Object = MibTableColumn
vsmSigChanEmCommonClearDetect = _VsmSigChanEmCommonClearDetect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 11, 1, 4),
    _VsmSigChanEmCommonClearDetect_Type()
)
vsmSigChanEmCommonClearDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmCommonClearDetect.setStatus("mandatory")


class _VsmSigChanEmCommonClearConfDetect_Type(Integer32):
    """Custom type vsmSigChanEmCommonClearConfDetect based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5000),
    )


_VsmSigChanEmCommonClearConfDetect_Type.__name__ = "Integer32"
_VsmSigChanEmCommonClearConfDetect_Object = MibTableColumn
vsmSigChanEmCommonClearConfDetect = _VsmSigChanEmCommonClearConfDetect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 11, 1, 5),
    _VsmSigChanEmCommonClearConfDetect_Type()
)
vsmSigChanEmCommonClearConfDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmCommonClearConfDetect.setStatus("mandatory")


class _VsmSigChanEmCommonClearConfWaitMax_Type(Integer32):
    """Custom type vsmSigChanEmCommonClearConfWaitMax based on Integer32"""
    defaultValue = 60000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_VsmSigChanEmCommonClearConfWaitMax_Type.__name__ = "Integer32"
_VsmSigChanEmCommonClearConfWaitMax_Object = MibTableColumn
vsmSigChanEmCommonClearConfWaitMax = _VsmSigChanEmCommonClearConfWaitMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 11, 1, 6),
    _VsmSigChanEmCommonClearConfWaitMax_Type()
)
vsmSigChanEmCommonClearConfWaitMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmCommonClearConfWaitMax.setStatus("mandatory")


class _VsmSigChanEmCommonGuardAll_Type(Integer32):
    """Custom type vsmSigChanEmCommonGuardAll based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_VsmSigChanEmCommonGuardAll_Type.__name__ = "Integer32"
_VsmSigChanEmCommonGuardAll_Object = MibTableColumn
vsmSigChanEmCommonGuardAll = _VsmSigChanEmCommonGuardAll_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 11, 1, 7),
    _VsmSigChanEmCommonGuardAll_Type()
)
vsmSigChanEmCommonGuardAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmCommonGuardAll.setStatus("mandatory")


class _VsmSigChanEmCommonGuardOut_Type(Integer32):
    """Custom type vsmSigChanEmCommonGuardOut based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmCommonGuardOut_Type.__name__ = "Integer32"
_VsmSigChanEmCommonGuardOut_Object = MibTableColumn
vsmSigChanEmCommonGuardOut = _VsmSigChanEmCommonGuardOut_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 11, 1, 8),
    _VsmSigChanEmCommonGuardOut_Type()
)
vsmSigChanEmCommonGuardOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmCommonGuardOut.setStatus("mandatory")


class _VsmSigChanEmCommonDialTone_Type(VsmEnableDisabled):
    """Custom type vsmSigChanEmCommonDialTone based on VsmEnableDisabled"""


_VsmSigChanEmCommonDialTone_Object = MibTableColumn
vsmSigChanEmCommonDialTone = _VsmSigChanEmCommonDialTone_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 11, 1, 9),
    _VsmSigChanEmCommonDialTone_Type()
)
vsmSigChanEmCommonDialTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmCommonDialTone.setStatus("mandatory")


class _VsmSigChanEmCommonMinConnectTime_Type(Integer32):
    """Custom type vsmSigChanEmCommonMinConnectTime based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_VsmSigChanEmCommonMinConnectTime_Type.__name__ = "Integer32"
_VsmSigChanEmCommonMinConnectTime_Object = MibTableColumn
vsmSigChanEmCommonMinConnectTime = _VsmSigChanEmCommonMinConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 11, 1, 10),
    _VsmSigChanEmCommonMinConnectTime_Type()
)
vsmSigChanEmCommonMinConnectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmCommonMinConnectTime.setStatus("mandatory")


class _VsmSigChanEmCommonHangUpWait_Type(Integer32):
    """Custom type vsmSigChanEmCommonHangUpWait based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmCommonHangUpWait_Type.__name__ = "Integer32"
_VsmSigChanEmCommonHangUpWait_Object = MibTableColumn
vsmSigChanEmCommonHangUpWait = _VsmSigChanEmCommonHangUpWait_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 11, 1, 11),
    _VsmSigChanEmCommonHangUpWait_Type()
)
vsmSigChanEmCommonHangUpWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmCommonHangUpWait.setStatus("mandatory")
_VsmSigChanEmDelayTable_Object = MibTable
vsmSigChanEmDelayTable = _VsmSigChanEmDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 12)
)
if mibBuilder.loadTexts:
    vsmSigChanEmDelayTable.setStatus("mandatory")
_VsmSigChanEmDelayEntry_Object = MibTableRow
vsmSigChanEmDelayEntry = _VsmSigChanEmDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 12, 1)
)
vsmSigChanEmDelayEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmSigChanEmDelayEntry.setStatus("mandatory")


class _VsmSigChanEmDelayInDelayDurMin_Type(Integer32):
    """Custom type vsmSigChanEmDelayInDelayDurMin based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmDelayInDelayDurMin_Type.__name__ = "Integer32"
_VsmSigChanEmDelayInDelayDurMin_Object = MibTableColumn
vsmSigChanEmDelayInDelayDurMin = _VsmSigChanEmDelayInDelayDurMin_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 12, 1, 1),
    _VsmSigChanEmDelayInDelayDurMin_Type()
)
vsmSigChanEmDelayInDelayDurMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmDelayInDelayDurMin.setStatus("mandatory")


class _VsmSigChanEmDelayInDelayDurMax_Type(Integer32):
    """Custom type vsmSigChanEmDelayInDelayDurMax based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmDelayInDelayDurMax_Type.__name__ = "Integer32"
_VsmSigChanEmDelayInDelayDurMax_Object = MibTableColumn
vsmSigChanEmDelayInDelayDurMax = _VsmSigChanEmDelayInDelayDurMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 12, 1, 2),
    _VsmSigChanEmDelayInDelayDurMax_Type()
)
vsmSigChanEmDelayInDelayDurMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmDelayInDelayDurMax.setStatus("mandatory")


class _VsmSigChanEmDelayInDigitIgnore_Type(Integer32):
    """Custom type vsmSigChanEmDelayInDigitIgnore based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmDelayInDigitIgnore_Type.__name__ = "Integer32"
_VsmSigChanEmDelayInDigitIgnore_Object = MibTableColumn
vsmSigChanEmDelayInDigitIgnore = _VsmSigChanEmDelayInDigitIgnore_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 12, 1, 3),
    _VsmSigChanEmDelayInDigitIgnore_Type()
)
vsmSigChanEmDelayInDigitIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmDelayInDigitIgnore.setStatus("mandatory")


class _VsmSigChanEmDelayOutDelayDurMin_Type(Integer32):
    """Custom type vsmSigChanEmDelayOutDelayDurMin based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmDelayOutDelayDurMin_Type.__name__ = "Integer32"
_VsmSigChanEmDelayOutDelayDurMin_Object = MibTableColumn
vsmSigChanEmDelayOutDelayDurMin = _VsmSigChanEmDelayOutDelayDurMin_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 12, 1, 4),
    _VsmSigChanEmDelayOutDelayDurMin_Type()
)
vsmSigChanEmDelayOutDelayDurMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmDelayOutDelayDurMin.setStatus("mandatory")


class _VsmSigChanEmDelayOutDelayDurMax_Type(Integer32):
    """Custom type vsmSigChanEmDelayOutDelayDurMax based on Integer32"""
    defaultValue = 8000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmDelayOutDelayDurMax_Type.__name__ = "Integer32"
_VsmSigChanEmDelayOutDelayDurMax_Object = MibTableColumn
vsmSigChanEmDelayOutDelayDurMax = _VsmSigChanEmDelayOutDelayDurMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 12, 1, 5),
    _VsmSigChanEmDelayOutDelayDurMax_Type()
)
vsmSigChanEmDelayOutDelayDurMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmDelayOutDelayDurMax.setStatus("mandatory")


class _VsmSigChanEmDelayOutIntegrityChk_Type(VsmEnableDisabled):
    """Custom type vsmSigChanEmDelayOutIntegrityChk based on VsmEnableDisabled"""


_VsmSigChanEmDelayOutIntegrityChk_Object = MibTableColumn
vsmSigChanEmDelayOutIntegrityChk = _VsmSigChanEmDelayOutIntegrityChk_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 12, 1, 6),
    _VsmSigChanEmDelayOutIntegrityChk_Type()
)
vsmSigChanEmDelayOutIntegrityChk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmDelayOutIntegrityChk.setStatus("mandatory")


class _VsmSigChanEmDelayOutDelayChk_Type(Integer32):
    """Custom type vsmSigChanEmDelayOutDelayChk based on Integer32"""
    defaultValue = 170

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmDelayOutDelayChk_Type.__name__ = "Integer32"
_VsmSigChanEmDelayOutDelayChk_Object = MibTableColumn
vsmSigChanEmDelayOutDelayChk = _VsmSigChanEmDelayOutDelayChk_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 12, 1, 7),
    _VsmSigChanEmDelayOutDelayChk_Type()
)
vsmSigChanEmDelayOutDelayChk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmDelayOutDelayChk.setStatus("mandatory")
_VsmSigChanEmImmedTable_Object = MibTable
vsmSigChanEmImmedTable = _VsmSigChanEmImmedTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 13)
)
if mibBuilder.loadTexts:
    vsmSigChanEmImmedTable.setStatus("mandatory")
_VsmSigChanEmImmedEntry_Object = MibTableRow
vsmSigChanEmImmedEntry = _VsmSigChanEmImmedEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 13, 1)
)
vsmSigChanEmImmedEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmSigChanEmImmedEntry.setStatus("mandatory")


class _VsmSigChanEmImmedGlareReport_Type(Integer32):
    """Custom type vsmSigChanEmImmedGlareReport based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_VsmSigChanEmImmedGlareReport_Type.__name__ = "Integer32"
_VsmSigChanEmImmedGlareReport_Object = MibTableColumn
vsmSigChanEmImmedGlareReport = _VsmSigChanEmImmedGlareReport_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 13, 1, 1),
    _VsmSigChanEmImmedGlareReport_Type()
)
vsmSigChanEmImmedGlareReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmImmedGlareReport.setStatus("mandatory")


class _VsmSigChanEmImmedDigitWait_Type(Integer32):
    """Custom type vsmSigChanEmImmedDigitWait based on Integer32"""
    defaultValue = 200


_VsmSigChanEmImmedDigitWait_Object = MibTableColumn
vsmSigChanEmImmedDigitWait = _VsmSigChanEmImmedDigitWait_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 13, 1, 2),
    _VsmSigChanEmImmedDigitWait_Type()
)
vsmSigChanEmImmedDigitWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmImmedDigitWait.setStatus("mandatory")
_VsmSigChanEmWinkTable_Object = MibTable
vsmSigChanEmWinkTable = _VsmSigChanEmWinkTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 14)
)
if mibBuilder.loadTexts:
    vsmSigChanEmWinkTable.setStatus("mandatory")
_VsmSigChanEmWinkEntry_Object = MibTableRow
vsmSigChanEmWinkEntry = _VsmSigChanEmWinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 14, 1)
)
vsmSigChanEmWinkEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmSigChanEmWinkEntry.setStatus("mandatory")


class _VsmSigChanEmWinkInWinkWaitMin_Type(Integer32):
    """Custom type vsmSigChanEmWinkInWinkWaitMin based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmWinkInWinkWaitMin_Type.__name__ = "Integer32"
_VsmSigChanEmWinkInWinkWaitMin_Object = MibTableColumn
vsmSigChanEmWinkInWinkWaitMin = _VsmSigChanEmWinkInWinkWaitMin_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 14, 1, 1),
    _VsmSigChanEmWinkInWinkWaitMin_Type()
)
vsmSigChanEmWinkInWinkWaitMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmWinkInWinkWaitMin.setStatus("mandatory")


class _VsmSigChanEmWinkInWinkWaitMax_Type(Integer32):
    """Custom type vsmSigChanEmWinkInWinkWaitMax based on Integer32"""
    defaultValue = 290

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmWinkInWinkWaitMax_Type.__name__ = "Integer32"
_VsmSigChanEmWinkInWinkWaitMax_Object = MibTableColumn
vsmSigChanEmWinkInWinkWaitMax = _VsmSigChanEmWinkInWinkWaitMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 14, 1, 2),
    _VsmSigChanEmWinkInWinkWaitMax_Type()
)
vsmSigChanEmWinkInWinkWaitMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmWinkInWinkWaitMax.setStatus("mandatory")


class _VsmSigChanEmWinkInWinkDur_Type(Integer32):
    """Custom type vsmSigChanEmWinkInWinkDur based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmWinkInWinkDur_Type.__name__ = "Integer32"
_VsmSigChanEmWinkInWinkDur_Object = MibTableColumn
vsmSigChanEmWinkInWinkDur = _VsmSigChanEmWinkInWinkDur_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 14, 1, 3),
    _VsmSigChanEmWinkInWinkDur_Type()
)
vsmSigChanEmWinkInWinkDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmWinkInWinkDur.setStatus("mandatory")


class _VsmSigChanEmWinkInDigitIgnore_Type(Integer32):
    """Custom type vsmSigChanEmWinkInDigitIgnore based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_VsmSigChanEmWinkInDigitIgnore_Type.__name__ = "Integer32"
_VsmSigChanEmWinkInDigitIgnore_Object = MibTableColumn
vsmSigChanEmWinkInDigitIgnore = _VsmSigChanEmWinkInDigitIgnore_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 14, 1, 4),
    _VsmSigChanEmWinkInDigitIgnore_Type()
)
vsmSigChanEmWinkInDigitIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmWinkInDigitIgnore.setStatus("mandatory")


class _VsmSigChanEmWinkOutWinkWaitMax_Type(Integer32):
    """Custom type vsmSigChanEmWinkOutWinkWaitMax based on Integer32"""
    defaultValue = 8000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmWinkOutWinkWaitMax_Type.__name__ = "Integer32"
_VsmSigChanEmWinkOutWinkWaitMax_Object = MibTableColumn
vsmSigChanEmWinkOutWinkWaitMax = _VsmSigChanEmWinkOutWinkWaitMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 14, 1, 5),
    _VsmSigChanEmWinkOutWinkWaitMax_Type()
)
vsmSigChanEmWinkOutWinkWaitMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmWinkOutWinkWaitMax.setStatus("mandatory")


class _VsmSigChanEmWinkOutWinkDurMin_Type(Integer32):
    """Custom type vsmSigChanEmWinkOutWinkDurMin based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmWinkOutWinkDurMin_Type.__name__ = "Integer32"
_VsmSigChanEmWinkOutWinkDurMin_Object = MibTableColumn
vsmSigChanEmWinkOutWinkDurMin = _VsmSigChanEmWinkOutWinkDurMin_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 14, 1, 6),
    _VsmSigChanEmWinkOutWinkDurMin_Type()
)
vsmSigChanEmWinkOutWinkDurMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmWinkOutWinkDurMin.setStatus("mandatory")


class _VsmSigChanEmWinkOutWinkDurMax_Type(Integer32):
    """Custom type vsmSigChanEmWinkOutWinkDurMax based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60000),
    )


_VsmSigChanEmWinkOutWinkDurMax_Type.__name__ = "Integer32"
_VsmSigChanEmWinkOutWinkDurMax_Object = MibTableColumn
vsmSigChanEmWinkOutWinkDurMax = _VsmSigChanEmWinkOutWinkDurMax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 14, 1, 7),
    _VsmSigChanEmWinkOutWinkDurMax_Type()
)
vsmSigChanEmWinkOutWinkDurMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanEmWinkOutWinkDurMax.setStatus("mandatory")
_VsmSigChanFxoGSTable_Object = MibTable
vsmSigChanFxoGSTable = _VsmSigChanFxoGSTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 15)
)
if mibBuilder.loadTexts:
    vsmSigChanFxoGSTable.setStatus("mandatory")
_VsmSigChanFxoGSEntry_Object = MibTableRow
vsmSigChanFxoGSEntry = _VsmSigChanFxoGSEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 15, 1)
)
vsmSigChanFxoGSEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmSigChanFxoGSEntry.setStatus("mandatory")


class _VsmSigChanFxoGSConnectionLoopOpenDebounce_Type(Integer32):
    """Custom type vsmSigChanFxoGSConnectionLoopOpenDebounce based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_VsmSigChanFxoGSConnectionLoopOpenDebounce_Type.__name__ = "Integer32"
_VsmSigChanFxoGSConnectionLoopOpenDebounce_Object = MibTableColumn
vsmSigChanFxoGSConnectionLoopOpenDebounce = _VsmSigChanFxoGSConnectionLoopOpenDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 15, 1, 1),
    _VsmSigChanFxoGSConnectionLoopOpenDebounce_Type()
)
vsmSigChanFxoGSConnectionLoopOpenDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoGSConnectionLoopOpenDebounce.setStatus("mandatory")


class _VsmSigChanFxoGSMaxTipGroundWait_Type(Integer32):
    """Custom type vsmSigChanFxoGSMaxTipGroundWait based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_VsmSigChanFxoGSMaxTipGroundWait_Type.__name__ = "Integer32"
_VsmSigChanFxoGSMaxTipGroundWait_Object = MibTableColumn
vsmSigChanFxoGSMaxTipGroundWait = _VsmSigChanFxoGSMaxTipGroundWait_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 15, 1, 2),
    _VsmSigChanFxoGSMaxTipGroundWait_Type()
)
vsmSigChanFxoGSMaxTipGroundWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoGSMaxTipGroundWait.setStatus("mandatory")


class _VsmSigChanFxoGSTipGroundDebounce_Type(Integer32):
    """Custom type vsmSigChanFxoGSTipGroundDebounce based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VsmSigChanFxoGSTipGroundDebounce_Type.__name__ = "Integer32"
_VsmSigChanFxoGSTipGroundDebounce_Object = MibTableColumn
vsmSigChanFxoGSTipGroundDebounce = _VsmSigChanFxoGSTipGroundDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 15, 1, 3),
    _VsmSigChanFxoGSTipGroundDebounce_Type()
)
vsmSigChanFxoGSTipGroundDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoGSTipGroundDebounce.setStatus("mandatory")


class _VsmSigChanFxoGSRingingDebounce_Type(Integer32):
    """Custom type vsmSigChanFxoGSRingingDebounce based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VsmSigChanFxoGSRingingDebounce_Type.__name__ = "Integer32"
_VsmSigChanFxoGSRingingDebounce_Object = MibTableColumn
vsmSigChanFxoGSRingingDebounce = _VsmSigChanFxoGSRingingDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 15, 1, 4),
    _VsmSigChanFxoGSRingingDebounce_Type()
)
vsmSigChanFxoGSRingingDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoGSRingingDebounce.setStatus("mandatory")


class _VsmSigChanFxoGSRingingInterCycle_Type(Integer32):
    """Custom type vsmSigChanFxoGSRingingInterCycle based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_VsmSigChanFxoGSRingingInterCycle_Type.__name__ = "Integer32"
_VsmSigChanFxoGSRingingInterCycle_Object = MibTableColumn
vsmSigChanFxoGSRingingInterCycle = _VsmSigChanFxoGSRingingInterCycle_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 15, 1, 5),
    _VsmSigChanFxoGSRingingInterCycle_Type()
)
vsmSigChanFxoGSRingingInterCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoGSRingingInterCycle.setStatus("mandatory")


class _VsmSigChanFxoGSRingingInterPulse_Type(Integer32):
    """Custom type vsmSigChanFxoGSRingingInterPulse based on Integer32"""
    defaultValue = 550

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_VsmSigChanFxoGSRingingInterPulse_Type.__name__ = "Integer32"
_VsmSigChanFxoGSRingingInterPulse_Object = MibTableColumn
vsmSigChanFxoGSRingingInterPulse = _VsmSigChanFxoGSRingingInterPulse_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 15, 1, 6),
    _VsmSigChanFxoGSRingingInterPulse_Type()
)
vsmSigChanFxoGSRingingInterPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoGSRingingInterPulse.setStatus("mandatory")


class _VsmSigChanFxoGSCallerIdDetect_Type(VsmEnableDisabled):
    """Custom type vsmSigChanFxoGSCallerIdDetect based on VsmEnableDisabled"""


_VsmSigChanFxoGSCallerIdDetect_Object = MibTableColumn
vsmSigChanFxoGSCallerIdDetect = _VsmSigChanFxoGSCallerIdDetect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 15, 1, 7),
    _VsmSigChanFxoGSCallerIdDetect_Type()
)
vsmSigChanFxoGSCallerIdDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoGSCallerIdDetect.setStatus("mandatory")


class _VsmSigChanFxoGSAnswerAfterRings_Type(Integer32):
    """Custom type vsmSigChanFxoGSAnswerAfterRings based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VsmSigChanFxoGSAnswerAfterRings_Type.__name__ = "Integer32"
_VsmSigChanFxoGSAnswerAfterRings_Object = MibTableColumn
vsmSigChanFxoGSAnswerAfterRings = _VsmSigChanFxoGSAnswerAfterRings_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 15, 1, 8),
    _VsmSigChanFxoGSAnswerAfterRings_Type()
)
vsmSigChanFxoGSAnswerAfterRings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoGSAnswerAfterRings.setStatus("mandatory")


class _VsmSigChanFxoGSLoopCurrentDebounce_Type(Integer32):
    """Custom type vsmSigChanFxoGSLoopCurrentDebounce based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VsmSigChanFxoGSLoopCurrentDebounce_Type.__name__ = "Integer32"
_VsmSigChanFxoGSLoopCurrentDebounce_Object = MibTableColumn
vsmSigChanFxoGSLoopCurrentDebounce = _VsmSigChanFxoGSLoopCurrentDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 15, 1, 9),
    _VsmSigChanFxoGSLoopCurrentDebounce_Type()
)
vsmSigChanFxoGSLoopCurrentDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoGSLoopCurrentDebounce.setStatus("mandatory")


class _VsmSigChanFxoGSBattReversalDebounce_Type(Integer32):
    """Custom type vsmSigChanFxoGSBattReversalDebounce based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VsmSigChanFxoGSBattReversalDebounce_Type.__name__ = "Integer32"
_VsmSigChanFxoGSBattReversalDebounce_Object = MibTableColumn
vsmSigChanFxoGSBattReversalDebounce = _VsmSigChanFxoGSBattReversalDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 15, 1, 10),
    _VsmSigChanFxoGSBattReversalDebounce_Type()
)
vsmSigChanFxoGSBattReversalDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoGSBattReversalDebounce.setStatus("mandatory")
_VsmSigChanFxoLSTable_Object = MibTable
vsmSigChanFxoLSTable = _VsmSigChanFxoLSTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 16)
)
if mibBuilder.loadTexts:
    vsmSigChanFxoLSTable.setStatus("mandatory")
_VsmSigChanFxoLSEntry_Object = MibTableRow
vsmSigChanFxoLSEntry = _VsmSigChanFxoLSEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 16, 1)
)
vsmSigChanFxoLSEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmSigChanFxoLSEntry.setStatus("mandatory")


class _VsmSigChanFxoLSRingingDebounce_Type(Integer32):
    """Custom type vsmSigChanFxoLSRingingDebounce based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VsmSigChanFxoLSRingingDebounce_Type.__name__ = "Integer32"
_VsmSigChanFxoLSRingingDebounce_Object = MibTableColumn
vsmSigChanFxoLSRingingDebounce = _VsmSigChanFxoLSRingingDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 16, 1, 1),
    _VsmSigChanFxoLSRingingDebounce_Type()
)
vsmSigChanFxoLSRingingDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoLSRingingDebounce.setStatus("mandatory")


class _VsmSigChanFxoLSCPCDetectCtrl_Type(VsmEnableDisabled):
    """Custom type vsmSigChanFxoLSCPCDetectCtrl based on VsmEnableDisabled"""


_VsmSigChanFxoLSCPCDetectCtrl_Object = MibTableColumn
vsmSigChanFxoLSCPCDetectCtrl = _VsmSigChanFxoLSCPCDetectCtrl_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 16, 1, 2),
    _VsmSigChanFxoLSCPCDetectCtrl_Type()
)
vsmSigChanFxoLSCPCDetectCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoLSCPCDetectCtrl.setStatus("mandatory")


class _VsmSigChanFxoLSCPCDetectDur_Type(Integer32):
    """Custom type vsmSigChanFxoLSCPCDetectDur based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_VsmSigChanFxoLSCPCDetectDur_Type.__name__ = "Integer32"
_VsmSigChanFxoLSCPCDetectDur_Object = MibTableColumn
vsmSigChanFxoLSCPCDetectDur = _VsmSigChanFxoLSCPCDetectDur_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 16, 1, 3),
    _VsmSigChanFxoLSCPCDetectDur_Type()
)
vsmSigChanFxoLSCPCDetectDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoLSCPCDetectDur.setStatus("mandatory")


class _VsmSigChanFxoLSGuardOut_Type(Integer32):
    """Custom type vsmSigChanFxoLSGuardOut based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_VsmSigChanFxoLSGuardOut_Type.__name__ = "Integer32"
_VsmSigChanFxoLSGuardOut_Object = MibTableColumn
vsmSigChanFxoLSGuardOut = _VsmSigChanFxoLSGuardOut_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 16, 1, 4),
    _VsmSigChanFxoLSGuardOut_Type()
)
vsmSigChanFxoLSGuardOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoLSGuardOut.setStatus("mandatory")


class _VsmSigChanFxoLSRingingInterCycle_Type(Integer32):
    """Custom type vsmSigChanFxoLSRingingInterCycle based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_VsmSigChanFxoLSRingingInterCycle_Type.__name__ = "Integer32"
_VsmSigChanFxoLSRingingInterCycle_Object = MibTableColumn
vsmSigChanFxoLSRingingInterCycle = _VsmSigChanFxoLSRingingInterCycle_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 16, 1, 5),
    _VsmSigChanFxoLSRingingInterCycle_Type()
)
vsmSigChanFxoLSRingingInterCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoLSRingingInterCycle.setStatus("mandatory")


class _VsmSigChanFxoLSRingingInterPulse_Type(Integer32):
    """Custom type vsmSigChanFxoLSRingingInterPulse based on Integer32"""
    defaultValue = 550

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_VsmSigChanFxoLSRingingInterPulse_Type.__name__ = "Integer32"
_VsmSigChanFxoLSRingingInterPulse_Object = MibTableColumn
vsmSigChanFxoLSRingingInterPulse = _VsmSigChanFxoLSRingingInterPulse_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 16, 1, 6),
    _VsmSigChanFxoLSRingingInterPulse_Type()
)
vsmSigChanFxoLSRingingInterPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoLSRingingInterPulse.setStatus("mandatory")


class _VsmSigChanFxoLSCallerIdDetect_Type(VsmEnableDisabled):
    """Custom type vsmSigChanFxoLSCallerIdDetect based on VsmEnableDisabled"""


_VsmSigChanFxoLSCallerIdDetect_Object = MibTableColumn
vsmSigChanFxoLSCallerIdDetect = _VsmSigChanFxoLSCallerIdDetect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 16, 1, 7),
    _VsmSigChanFxoLSCallerIdDetect_Type()
)
vsmSigChanFxoLSCallerIdDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoLSCallerIdDetect.setStatus("mandatory")


class _VsmSigChanFxoLSAnswerAfterRings_Type(Integer32):
    """Custom type vsmSigChanFxoLSAnswerAfterRings based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VsmSigChanFxoLSAnswerAfterRings_Type.__name__ = "Integer32"
_VsmSigChanFxoLSAnswerAfterRings_Object = MibTableColumn
vsmSigChanFxoLSAnswerAfterRings = _VsmSigChanFxoLSAnswerAfterRings_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 16, 1, 8),
    _VsmSigChanFxoLSAnswerAfterRings_Type()
)
vsmSigChanFxoLSAnswerAfterRings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoLSAnswerAfterRings.setStatus("mandatory")


class _VsmSigChanFxoLSLoopCurrentDebounce_Type(Integer32):
    """Custom type vsmSigChanFxoLSLoopCurrentDebounce based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_VsmSigChanFxoLSLoopCurrentDebounce_Type.__name__ = "Integer32"
_VsmSigChanFxoLSLoopCurrentDebounce_Object = MibTableColumn
vsmSigChanFxoLSLoopCurrentDebounce = _VsmSigChanFxoLSLoopCurrentDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 16, 1, 9),
    _VsmSigChanFxoLSLoopCurrentDebounce_Type()
)
vsmSigChanFxoLSLoopCurrentDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoLSLoopCurrentDebounce.setStatus("mandatory")


class _VsmSigChanFxoLSBattReversalDebounce_Type(Integer32):
    """Custom type vsmSigChanFxoLSBattReversalDebounce based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_VsmSigChanFxoLSBattReversalDebounce_Type.__name__ = "Integer32"
_VsmSigChanFxoLSBattReversalDebounce_Object = MibTableColumn
vsmSigChanFxoLSBattReversalDebounce = _VsmSigChanFxoLSBattReversalDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 16, 1, 10),
    _VsmSigChanFxoLSBattReversalDebounce_Type()
)
vsmSigChanFxoLSBattReversalDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxoLSBattReversalDebounce.setStatus("mandatory")
_VsmSigChanFxsGSTable_Object = MibTable
vsmSigChanFxsGSTable = _VsmSigChanFxsGSTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 17)
)
if mibBuilder.loadTexts:
    vsmSigChanFxsGSTable.setStatus("mandatory")
_VsmSigChanFxsGSEntry_Object = MibTableRow
vsmSigChanFxsGSEntry = _VsmSigChanFxsGSEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 17, 1)
)
vsmSigChanFxsGSEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmSigChanFxsGSEntry.setStatus("mandatory")


class _VsmSigChanFxsGSSeizeDetect_Type(Integer32):
    """Custom type vsmSigChanFxsGSSeizeDetect based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_VsmSigChanFxsGSSeizeDetect_Type.__name__ = "Integer32"
_VsmSigChanFxsGSSeizeDetect_Object = MibTableColumn
vsmSigChanFxsGSSeizeDetect = _VsmSigChanFxsGSSeizeDetect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 17, 1, 1),
    _VsmSigChanFxsGSSeizeDetect_Type()
)
vsmSigChanFxsGSSeizeDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsGSSeizeDetect.setStatus("mandatory")


class _VsmSigChanFxsGSOnHookDebounce_Type(Integer32):
    """Custom type vsmSigChanFxsGSOnHookDebounce based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VsmSigChanFxsGSOnHookDebounce_Type.__name__ = "Integer32"
_VsmSigChanFxsGSOnHookDebounce_Object = MibTableColumn
vsmSigChanFxsGSOnHookDebounce = _VsmSigChanFxsGSOnHookDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 17, 1, 2),
    _VsmSigChanFxsGSOnHookDebounce_Type()
)
vsmSigChanFxsGSOnHookDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsGSOnHookDebounce.setStatus("mandatory")


class _VsmSigChanFxsGSOrigClearDetect_Type(Integer32):
    """Custom type vsmSigChanFxsGSOrigClearDetect based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_VsmSigChanFxsGSOrigClearDetect_Type.__name__ = "Integer32"
_VsmSigChanFxsGSOrigClearDetect_Object = MibTableColumn
vsmSigChanFxsGSOrigClearDetect = _VsmSigChanFxsGSOrigClearDetect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 17, 1, 3),
    _VsmSigChanFxsGSOrigClearDetect_Type()
)
vsmSigChanFxsGSOrigClearDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsGSOrigClearDetect.setStatus("mandatory")


class _VsmSigChanFxsGSAnswClearDetect_Type(Integer32):
    """Custom type vsmSigChanFxsGSAnswClearDetect based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_VsmSigChanFxsGSAnswClearDetect_Type.__name__ = "Integer32"
_VsmSigChanFxsGSAnswClearDetect_Object = MibTableColumn
vsmSigChanFxsGSAnswClearDetect = _VsmSigChanFxsGSAnswClearDetect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 17, 1, 4),
    _VsmSigChanFxsGSAnswClearDetect_Type()
)
vsmSigChanFxsGSAnswClearDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsGSAnswClearDetect.setStatus("mandatory")


class _VsmSigChanFxsGSMinRingGround_Type(Integer32):
    """Custom type vsmSigChanFxsGSMinRingGround based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsmSigChanFxsGSMinRingGround_Type.__name__ = "Integer32"
_VsmSigChanFxsGSMinRingGround_Object = MibTableColumn
vsmSigChanFxsGSMinRingGround = _VsmSigChanFxsGSMinRingGround_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 17, 1, 5),
    _VsmSigChanFxsGSMinRingGround_Type()
)
vsmSigChanFxsGSMinRingGround.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsGSMinRingGround.setStatus("mandatory")


class _VsmSigChanFxsGSMaxWaitLoop_Type(Integer32):
    """Custom type vsmSigChanFxsGSMaxWaitLoop based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsmSigChanFxsGSMaxWaitLoop_Type.__name__ = "Integer32"
_VsmSigChanFxsGSMaxWaitLoop_Object = MibTableColumn
vsmSigChanFxsGSMaxWaitLoop = _VsmSigChanFxsGSMaxWaitLoop_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 17, 1, 6),
    _VsmSigChanFxsGSMaxWaitLoop_Type()
)
vsmSigChanFxsGSMaxWaitLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsGSMaxWaitLoop.setStatus("mandatory")


class _VsmSigChanFxsGSMinLoopOpen_Type(Integer32):
    """Custom type vsmSigChanFxsGSMinLoopOpen based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VsmSigChanFxsGSMinLoopOpen_Type.__name__ = "Integer32"
_VsmSigChanFxsGSMinLoopOpen_Object = MibTableColumn
vsmSigChanFxsGSMinLoopOpen = _VsmSigChanFxsGSMinLoopOpen_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 17, 1, 7),
    _VsmSigChanFxsGSMinLoopOpen_Type()
)
vsmSigChanFxsGSMinLoopOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsGSMinLoopOpen.setStatus("mandatory")


class _VsmSigChanFxsGSGenerateCallerId_Type(VsmEnableDisabled):
    """Custom type vsmSigChanFxsGSGenerateCallerId based on VsmEnableDisabled"""


_VsmSigChanFxsGSGenerateCallerId_Object = MibTableColumn
vsmSigChanFxsGSGenerateCallerId = _VsmSigChanFxsGSGenerateCallerId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 17, 1, 8),
    _VsmSigChanFxsGSGenerateCallerId_Type()
)
vsmSigChanFxsGSGenerateCallerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsGSGenerateCallerId.setStatus("mandatory")


class _VsmSigChanFxsGSOffHookDebounce_Type(Integer32):
    """Custom type vsmSigChanFxsGSOffHookDebounce based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VsmSigChanFxsGSOffHookDebounce_Type.__name__ = "Integer32"
_VsmSigChanFxsGSOffHookDebounce_Object = MibTableColumn
vsmSigChanFxsGSOffHookDebounce = _VsmSigChanFxsGSOffHookDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 17, 1, 9),
    _VsmSigChanFxsGSOffHookDebounce_Type()
)
vsmSigChanFxsGSOffHookDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsGSOffHookDebounce.setStatus("mandatory")


class _VsmSigChanFxsGSRingGroundDebounce_Type(Integer32):
    """Custom type vsmSigChanFxsGSRingGroundDebounce based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VsmSigChanFxsGSRingGroundDebounce_Type.__name__ = "Integer32"
_VsmSigChanFxsGSRingGroundDebounce_Object = MibTableColumn
vsmSigChanFxsGSRingGroundDebounce = _VsmSigChanFxsGSRingGroundDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 17, 1, 10),
    _VsmSigChanFxsGSRingGroundDebounce_Type()
)
vsmSigChanFxsGSRingGroundDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsGSRingGroundDebounce.setStatus("mandatory")
_VsmSigChanFxsLSTable_Object = MibTable
vsmSigChanFxsLSTable = _VsmSigChanFxsLSTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 18)
)
if mibBuilder.loadTexts:
    vsmSigChanFxsLSTable.setStatus("mandatory")
_VsmSigChanFxsLSEntry_Object = MibTableRow
vsmSigChanFxsLSEntry = _VsmSigChanFxsLSEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 18, 1)
)
vsmSigChanFxsLSEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmSigChanFxsLSEntry.setStatus("mandatory")


class _VsmSigChanFxsLSOffHookDebounce_Type(Integer32):
    """Custom type vsmSigChanFxsLSOffHookDebounce based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VsmSigChanFxsLSOffHookDebounce_Type.__name__ = "Integer32"
_VsmSigChanFxsLSOffHookDebounce_Object = MibTableColumn
vsmSigChanFxsLSOffHookDebounce = _VsmSigChanFxsLSOffHookDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 18, 1, 1),
    _VsmSigChanFxsLSOffHookDebounce_Type()
)
vsmSigChanFxsLSOffHookDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsLSOffHookDebounce.setStatus("mandatory")


class _VsmSigChanFxsLSOnHookDebounce_Type(Integer32):
    """Custom type vsmSigChanFxsLSOnHookDebounce based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VsmSigChanFxsLSOnHookDebounce_Type.__name__ = "Integer32"
_VsmSigChanFxsLSOnHookDebounce_Object = MibTableColumn
vsmSigChanFxsLSOnHookDebounce = _VsmSigChanFxsLSOnHookDebounce_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 18, 1, 2),
    _VsmSigChanFxsLSOnHookDebounce_Type()
)
vsmSigChanFxsLSOnHookDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsLSOnHookDebounce.setStatus("mandatory")


class _VsmSigChanFxsLSSeizeDetect_Type(Integer32):
    """Custom type vsmSigChanFxsLSSeizeDetect based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_VsmSigChanFxsLSSeizeDetect_Type.__name__ = "Integer32"
_VsmSigChanFxsLSSeizeDetect_Object = MibTableColumn
vsmSigChanFxsLSSeizeDetect = _VsmSigChanFxsLSSeizeDetect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 18, 1, 3),
    _VsmSigChanFxsLSSeizeDetect_Type()
)
vsmSigChanFxsLSSeizeDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsLSSeizeDetect.setStatus("mandatory")


class _VsmSigChanFxsLSOrigClearDetect_Type(Integer32):
    """Custom type vsmSigChanFxsLSOrigClearDetect based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VsmSigChanFxsLSOrigClearDetect_Type.__name__ = "Integer32"
_VsmSigChanFxsLSOrigClearDetect_Object = MibTableColumn
vsmSigChanFxsLSOrigClearDetect = _VsmSigChanFxsLSOrigClearDetect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 18, 1, 4),
    _VsmSigChanFxsLSOrigClearDetect_Type()
)
vsmSigChanFxsLSOrigClearDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsLSOrigClearDetect.setStatus("mandatory")


class _VsmSigChanFxsLSAnswClearDetect_Type(Integer32):
    """Custom type vsmSigChanFxsLSAnswClearDetect based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_VsmSigChanFxsLSAnswClearDetect_Type.__name__ = "Integer32"
_VsmSigChanFxsLSAnswClearDetect_Object = MibTableColumn
vsmSigChanFxsLSAnswClearDetect = _VsmSigChanFxsLSAnswClearDetect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 18, 1, 5),
    _VsmSigChanFxsLSAnswClearDetect_Type()
)
vsmSigChanFxsLSAnswClearDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsLSAnswClearDetect.setStatus("mandatory")


class _VsmSigChanFxsLSCPCWait_Type(Integer32):
    """Custom type vsmSigChanFxsLSCPCWait based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_VsmSigChanFxsLSCPCWait_Type.__name__ = "Integer32"
_VsmSigChanFxsLSCPCWait_Object = MibTableColumn
vsmSigChanFxsLSCPCWait = _VsmSigChanFxsLSCPCWait_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 18, 1, 6),
    _VsmSigChanFxsLSCPCWait_Type()
)
vsmSigChanFxsLSCPCWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsLSCPCWait.setStatus("mandatory")


class _VsmSigChanFxsLSCPCDur_Type(Integer32):
    """Custom type vsmSigChanFxsLSCPCDur based on Integer32"""
    defaultValue = 850

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_VsmSigChanFxsLSCPCDur_Type.__name__ = "Integer32"
_VsmSigChanFxsLSCPCDur_Object = MibTableColumn
vsmSigChanFxsLSCPCDur = _VsmSigChanFxsLSCPCDur_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 18, 1, 7),
    _VsmSigChanFxsLSCPCDur_Type()
)
vsmSigChanFxsLSCPCDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsLSCPCDur.setStatus("mandatory")


class _VsmSigChanFxsLSGenerateCallerId_Type(VsmEnableDisabled):
    """Custom type vsmSigChanFxsLSGenerateCallerId based on VsmEnableDisabled"""


_VsmSigChanFxsLSGenerateCallerId_Object = MibTableColumn
vsmSigChanFxsLSGenerateCallerId = _VsmSigChanFxsLSGenerateCallerId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 2, 18, 1, 8),
    _VsmSigChanFxsLSGenerateCallerId_Type()
)
vsmSigChanFxsLSGenerateCallerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmSigChanFxsLSGenerateCallerId.setStatus("mandatory")
_VsmCodingProfileGroup_ObjectIdentity = ObjectIdentity
vsmCodingProfileGroup = _VsmCodingProfileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3)
)
_VsmCodingProfileTable_Object = MibTable
vsmCodingProfileTable = _VsmCodingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1)
)
if mibBuilder.loadTexts:
    vsmCodingProfileTable.setStatus("mandatory")
_VsmCodingProfEntry_Object = MibTableRow
vsmCodingProfEntry = _VsmCodingProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1)
)
vsmCodingProfEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmCodingProfName"),
)
if mibBuilder.loadTexts:
    vsmCodingProfEntry.setStatus("mandatory")


class _VsmCodingProfId_Type(Integer32):
    """Custom type vsmCodingProfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VsmCodingProfId_Type.__name__ = "Integer32"
_VsmCodingProfId_Object = MibTableColumn
vsmCodingProfId = _VsmCodingProfId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 1),
    _VsmCodingProfId_Type()
)
vsmCodingProfId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfId.setStatus("mandatory")
_VsmCodingProfName_Type = DisplayString
_VsmCodingProfName_Object = MibTableColumn
vsmCodingProfName = _VsmCodingProfName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 2),
    _VsmCodingProfName_Type()
)
vsmCodingProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfName.setStatus("mandatory")


class _VsmCodingProfCallerId_Type(VsmEnableDisabled):
    """Custom type vsmCodingProfCallerId based on VsmEnableDisabled"""


_VsmCodingProfCallerId_Object = MibTableColumn
vsmCodingProfCallerId = _VsmCodingProfCallerId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 3),
    _VsmCodingProfCallerId_Type()
)
vsmCodingProfCallerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfCallerId.setStatus("mandatory")


class _VsmCodingProfCodingType_Type(VsmVoiceCodingType):
    """Custom type vsmCodingProfCodingType based on VsmVoiceCodingType"""


_VsmCodingProfCodingType_Object = MibTableColumn
vsmCodingProfCodingType = _VsmCodingProfCodingType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 4),
    _VsmCodingProfCodingType_Type()
)
vsmCodingProfCodingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfCodingType.setStatus("mandatory")


class _VsmCodingProfPktInterval_Type(Integer32):
    """Custom type vsmCodingProfPktInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              60,
              70,
              80)
        )
    )
    namedValues = NamedValues(
        *(("interval1", 10),
          ("interval2", 20),
          ("interval3", 30),
          ("interval4", 40),
          ("interval5", 50),
          ("interval6", 60),
          ("interval7", 70),
          ("interval8", 80))
    )


_VsmCodingProfPktInterval_Type.__name__ = "Integer32"
_VsmCodingProfPktInterval_Object = MibTableColumn
vsmCodingProfPktInterval = _VsmCodingProfPktInterval_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 5),
    _VsmCodingProfPktInterval_Type()
)
vsmCodingProfPktInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfPktInterval.setStatus("mandatory")


class _VsmCodingProfVIF_Type(Integer32):
    """Custom type vsmCodingProfVIF based on Integer32"""
    defaultValue = 384


_VsmCodingProfVIF_Object = MibTableColumn
vsmCodingProfVIF = _VsmCodingProfVIF_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 6),
    _VsmCodingProfVIF_Type()
)
vsmCodingProfVIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCodingProfVIF.setStatus("deprecated")


class _VsmCodingProfNetBufMode_Type(Integer32):
    """Custom type vsmCodingProfNetBufMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 1),
          ("static", 2))
    )


_VsmCodingProfNetBufMode_Type.__name__ = "Integer32"
_VsmCodingProfNetBufMode_Object = MibTableColumn
vsmCodingProfNetBufMode = _VsmCodingProfNetBufMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 7),
    _VsmCodingProfNetBufMode_Type()
)
vsmCodingProfNetBufMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfNetBufMode.setStatus("mandatory")


class _VsmCodingProfNetBufNomDelay_Type(Integer32):
    """Custom type vsmCodingProfNetBufNomDelay based on Integer32"""
    defaultValue = 120


_VsmCodingProfNetBufNomDelay_Object = MibTableColumn
vsmCodingProfNetBufNomDelay = _VsmCodingProfNetBufNomDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 8),
    _VsmCodingProfNetBufNomDelay_Type()
)
vsmCodingProfNetBufNomDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfNetBufNomDelay.setStatus("mandatory")


class _VsmCodingProfNetBufMaxDelay_Type(Integer32):
    """Custom type vsmCodingProfNetBufMaxDelay based on Integer32"""
    defaultValue = 240


_VsmCodingProfNetBufMaxDelay_Object = MibTableColumn
vsmCodingProfNetBufMaxDelay = _VsmCodingProfNetBufMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 9),
    _VsmCodingProfNetBufMaxDelay_Type()
)
vsmCodingProfNetBufMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfNetBufMaxDelay.setStatus("mandatory")


class _VsmCodingProfDtmfRelay_Type(VsmEnableDisabled):
    """Custom type vsmCodingProfDtmfRelay based on VsmEnableDisabled"""


_VsmCodingProfDtmfRelay_Object = MibTableColumn
vsmCodingProfDtmfRelay = _VsmCodingProfDtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 10),
    _VsmCodingProfDtmfRelay_Type()
)
vsmCodingProfDtmfRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfDtmfRelay.setStatus("mandatory")


class _VsmCodingProfVAD_Type(VsmEnableDisabled):
    """Custom type vsmCodingProfVAD based on VsmEnableDisabled"""


_VsmCodingProfVAD_Object = MibTableColumn
vsmCodingProfVAD = _VsmCodingProfVAD_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 11),
    _VsmCodingProfVAD_Type()
)
vsmCodingProfVAD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfVAD.setStatus("mandatory")


class _VsmCodingProfEC_Type(VsmEnableDisabled):
    """Custom type vsmCodingProfEC based on VsmEnableDisabled"""


_VsmCodingProfEC_Object = MibTableColumn
vsmCodingProfEC = _VsmCodingProfEC_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 12),
    _VsmCodingProfEC_Type()
)
vsmCodingProfEC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfEC.setStatus("mandatory")


class _VsmCodingProfSwitchover_Type(VsmEnableDisabled):
    """Custom type vsmCodingProfSwitchover based on VsmEnableDisabled"""


_VsmCodingProfSwitchover_Object = MibTableColumn
vsmCodingProfSwitchover = _VsmCodingProfSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 13),
    _VsmCodingProfSwitchover_Type()
)
vsmCodingProfSwitchover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfSwitchover.setStatus("mandatory")


class _VsmCodingProfCallProgToneDet_Type(VsmEnableDisabled):
    """Custom type vsmCodingProfCallProgToneDet based on VsmEnableDisabled"""


_VsmCodingProfCallProgToneDet_Object = MibTableColumn
vsmCodingProfCallProgToneDet = _VsmCodingProfCallProgToneDet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 15),
    _VsmCodingProfCallProgToneDet_Type()
)
vsmCodingProfCallProgToneDet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfCallProgToneDet.setStatus("mandatory")


class _VsmCodingProfV18ToneDet_Type(VsmEnableDisabled):
    """Custom type vsmCodingProfV18ToneDet based on VsmEnableDisabled"""


_VsmCodingProfV18ToneDet_Object = MibTableColumn
vsmCodingProfV18ToneDet = _VsmCodingProfV18ToneDet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 16),
    _VsmCodingProfV18ToneDet_Type()
)
vsmCodingProfV18ToneDet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfV18ToneDet.setStatus("mandatory")


class _VsmCodingProfVADThreshMode_Type(Integer32):
    """Custom type vsmCodingProfVADThreshMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 1),
          ("relative", 2))
    )


_VsmCodingProfVADThreshMode_Type.__name__ = "Integer32"
_VsmCodingProfVADThreshMode_Object = MibTableColumn
vsmCodingProfVADThreshMode = _VsmCodingProfVADThreshMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 17),
    _VsmCodingProfVADThreshMode_Type()
)
vsmCodingProfVADThreshMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfVADThreshMode.setStatus("mandatory")


class _VsmCodingProfVADThreshLevel_Type(Integer32):
    """Custom type vsmCodingProfVADThreshLevel based on Integer32"""
    defaultValue = -13

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_VsmCodingProfVADThreshLevel_Type.__name__ = "Integer32"
_VsmCodingProfVADThreshLevel_Object = MibTableColumn
vsmCodingProfVADThreshLevel = _VsmCodingProfVADThreshLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 18),
    _VsmCodingProfVADThreshLevel_Type()
)
vsmCodingProfVADThreshLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfVADThreshLevel.setStatus("mandatory")


class _VsmCodingProfVEchoCanComfNoiseMode_Type(Integer32):
    """Custom type vsmCodingProfVEchoCanComfNoiseMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("static", 1))
    )


_VsmCodingProfVEchoCanComfNoiseMode_Type.__name__ = "Integer32"
_VsmCodingProfVEchoCanComfNoiseMode_Object = MibTableColumn
vsmCodingProfVEchoCanComfNoiseMode = _VsmCodingProfVEchoCanComfNoiseMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 19),
    _VsmCodingProfVEchoCanComfNoiseMode_Type()
)
vsmCodingProfVEchoCanComfNoiseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfVEchoCanComfNoiseMode.setStatus("mandatory")


class _VsmCodingProfEchoCanRefreshCfg_Type(Integer32):
    """Custom type vsmCodingProfEchoCanRefreshCfg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frozen", 1),
          ("refresh", 2))
    )


_VsmCodingProfEchoCanRefreshCfg_Type.__name__ = "Integer32"
_VsmCodingProfEchoCanRefreshCfg_Object = MibTableColumn
vsmCodingProfEchoCanRefreshCfg = _VsmCodingProfEchoCanRefreshCfg_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 20),
    _VsmCodingProfEchoCanRefreshCfg_Type()
)
vsmCodingProfEchoCanRefreshCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfEchoCanRefreshCfg.setStatus("mandatory")


class _VsmCodingProfEchoCanRefreshState_Type(Integer32):
    """Custom type vsmCodingProfEchoCanRefreshState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_VsmCodingProfEchoCanRefreshState_Type.__name__ = "Integer32"
_VsmCodingProfEchoCanRefreshState_Object = MibTableColumn
vsmCodingProfEchoCanRefreshState = _VsmCodingProfEchoCanRefreshState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 21),
    _VsmCodingProfEchoCanRefreshState_Type()
)
vsmCodingProfEchoCanRefreshState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfEchoCanRefreshState.setStatus("mandatory")


class _VsmCodingProfECTailDelay_Type(Integer32):
    """Custom type vsmCodingProfECTailDelay based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("delay1", 4),
          ("delay2", 8),
          ("delay3", 16),
          ("delay4", 32))
    )


_VsmCodingProfECTailDelay_Type.__name__ = "Integer32"
_VsmCodingProfECTailDelay_Object = MibTableColumn
vsmCodingProfECTailDelay = _VsmCodingProfECTailDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 22),
    _VsmCodingProfECTailDelay_Type()
)
vsmCodingProfECTailDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfECTailDelay.setStatus("mandatory")


class _VsmCodingProfECNonLinear_Type(VsmEnableDisabled):
    """Custom type vsmCodingProfECNonLinear based on VsmEnableDisabled"""


_VsmCodingProfECNonLinear_Object = MibTableColumn
vsmCodingProfECNonLinear = _VsmCodingProfECNonLinear_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 23),
    _VsmCodingProfECNonLinear_Type()
)
vsmCodingProfECNonLinear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfECNonLinear.setStatus("mandatory")


class _VsmCodingProfFaxRate_Type(Integer32):
    """Custom type vsmCodingProfFaxRate based on Integer32"""
    defaultValue = 14400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2400,
              4800,
              7200,
              9600,
              12000,
              14400)
        )
    )
    namedValues = NamedValues(
        *(("rate1", 2400),
          ("rate2", 4800),
          ("rate3", 7200),
          ("rate4", 9600),
          ("rate5", 12000),
          ("rate6", 14400))
    )


_VsmCodingProfFaxRate_Type.__name__ = "Integer32"
_VsmCodingProfFaxRate_Object = MibTableColumn
vsmCodingProfFaxRate = _VsmCodingProfFaxRate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 35),
    _VsmCodingProfFaxRate_Type()
)
vsmCodingProfFaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfFaxRate.setStatus("mandatory")


class _VsmCodingProfFaxTxLevel_Type(Integer32):
    """Custom type vsmCodingProfFaxTxLevel based on Integer32"""
    defaultValue = -13

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-13, 0),
    )


_VsmCodingProfFaxTxLevel_Type.__name__ = "Integer32"
_VsmCodingProfFaxTxLevel_Object = MibTableColumn
vsmCodingProfFaxTxLevel = _VsmCodingProfFaxTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 36),
    _VsmCodingProfFaxTxLevel_Type()
)
vsmCodingProfFaxTxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfFaxTxLevel.setStatus("mandatory")


class _VsmCodingProfFaxCdThresh_Type(Integer32):
    """Custom type vsmCodingProfFaxCdThresh based on Integer32"""
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
        *(("n26dBm", 1),
          ("n33dBm", 2),
          ("n43dBm", 3))
    )


_VsmCodingProfFaxCdThresh_Type.__name__ = "Integer32"
_VsmCodingProfFaxCdThresh_Object = MibTableColumn
vsmCodingProfFaxCdThresh = _VsmCodingProfFaxCdThresh_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 37),
    _VsmCodingProfFaxCdThresh_Type()
)
vsmCodingProfFaxCdThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfFaxCdThresh.setStatus("mandatory")


class _VsmCodingProfFaxTimeOut_Type(Integer32):
    """Custom type vsmCodingProfFaxTimeOut based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3200),
    )


_VsmCodingProfFaxTimeOut_Type.__name__ = "Integer32"
_VsmCodingProfFaxTimeOut_Object = MibTableColumn
vsmCodingProfFaxTimeOut = _VsmCodingProfFaxTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 38),
    _VsmCodingProfFaxTimeOut_Type()
)
vsmCodingProfFaxTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfFaxTimeOut.setStatus("mandatory")


class _VsmCodingProfFaxHsPktRate_Type(Integer32):
    """Custom type vsmCodingProfFaxHsPktRate based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40)
        )
    )
    namedValues = NamedValues(
        *(("rate1", 10),
          ("rate2", 20),
          ("rate3", 30),
          ("rate4", 40))
    )


_VsmCodingProfFaxHsPktRate_Type.__name__ = "Integer32"
_VsmCodingProfFaxHsPktRate_Object = MibTableColumn
vsmCodingProfFaxHsPktRate = _VsmCodingProfFaxHsPktRate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 39),
    _VsmCodingProfFaxHsPktRate_Type()
)
vsmCodingProfFaxHsPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfFaxHsPktRate.setStatus("mandatory")


class _VsmCodingProfFaxLsRedun_Type(Integer32):
    """Custom type vsmCodingProfFaxLsRedun based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_VsmCodingProfFaxLsRedun_Type.__name__ = "Integer32"
_VsmCodingProfFaxLsRedun_Object = MibTableColumn
vsmCodingProfFaxLsRedun = _VsmCodingProfFaxLsRedun_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 40),
    _VsmCodingProfFaxLsRedun_Type()
)
vsmCodingProfFaxLsRedun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfFaxLsRedun.setStatus("mandatory")


class _VsmCodingProfFaxHsRedun_Type(Integer32):
    """Custom type vsmCodingProfFaxHsRedun based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_VsmCodingProfFaxHsRedun_Type.__name__ = "Integer32"
_VsmCodingProfFaxHsRedun_Object = MibTableColumn
vsmCodingProfFaxHsRedun = _VsmCodingProfFaxHsRedun_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 41),
    _VsmCodingProfFaxHsRedun_Type()
)
vsmCodingProfFaxHsRedun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfFaxHsRedun.setStatus("mandatory")


class _VsmCodingProfFaxTcfMethod_Type(Integer32):
    """Custom type vsmCodingProfFaxTcfMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("network", 2))
    )


_VsmCodingProfFaxTcfMethod_Type.__name__ = "Integer32"
_VsmCodingProfFaxTcfMethod_Object = MibTableColumn
vsmCodingProfFaxTcfMethod = _VsmCodingProfFaxTcfMethod_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 42),
    _VsmCodingProfFaxTcfMethod_Type()
)
vsmCodingProfFaxTcfMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfFaxTcfMethod.setStatus("mandatory")


class _VsmCodingProfSilenceDetect_Type(VsmEnableDisabled):
    """Custom type vsmCodingProfSilenceDetect based on VsmEnableDisabled"""


_VsmCodingProfSilenceDetect_Object = MibTableColumn
vsmCodingProfSilenceDetect = _VsmCodingProfSilenceDetect_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 43),
    _VsmCodingProfSilenceDetect_Type()
)
vsmCodingProfSilenceDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfSilenceDetect.setStatus("mandatory")


class _VsmCodingProfSilenceDetectTime_Type(Integer32):
    """Custom type vsmCodingProfSilenceDetectTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32000),
    )


_VsmCodingProfSilenceDetectTime_Type.__name__ = "Integer32"
_VsmCodingProfSilenceDetectTime_Object = MibTableColumn
vsmCodingProfSilenceDetectTime = _VsmCodingProfSilenceDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 44),
    _VsmCodingProfSilenceDetectTime_Type()
)
vsmCodingProfSilenceDetectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfSilenceDetectTime.setStatus("mandatory")


class _VsmCodingProfSilenceLevel_Type(Integer32):
    """Custom type vsmCodingProfSilenceLevel based on Integer32"""
    defaultValue = -50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, -40),
    )


_VsmCodingProfSilenceLevel_Type.__name__ = "Integer32"
_VsmCodingProfSilenceLevel_Object = MibTableColumn
vsmCodingProfSilenceLevel = _VsmCodingProfSilenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 45),
    _VsmCodingProfSilenceLevel_Type()
)
vsmCodingProfSilenceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfSilenceLevel.setStatus("mandatory")


class _VsmCodingProfVoiceComfortNoiseLevel_Type(Integer32):
    """Custom type vsmCodingProfVoiceComfortNoiseLevel based on Integer32"""
    defaultValue = -40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, -40),
    )


_VsmCodingProfVoiceComfortNoiseLevel_Type.__name__ = "Integer32"
_VsmCodingProfVoiceComfortNoiseLevel_Object = MibTableColumn
vsmCodingProfVoiceComfortNoiseLevel = _VsmCodingProfVoiceComfortNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 46),
    _VsmCodingProfVoiceComfortNoiseLevel_Type()
)
vsmCodingProfVoiceComfortNoiseLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfVoiceComfortNoiseLevel.setStatus("mandatory")


class _VsmCodingProfG711ModemResampMode_Type(VsmEnableDisabled):
    """Custom type vsmCodingProfG711ModemResampMode based on VsmEnableDisabled"""


_VsmCodingProfG711ModemResampMode_Object = MibTableColumn
vsmCodingProfG711ModemResampMode = _VsmCodingProfG711ModemResampMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 47),
    _VsmCodingProfG711ModemResampMode_Type()
)
vsmCodingProfG711ModemResampMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfG711ModemResampMode.setStatus("mandatory")


class _VsmCodingProfSinFreqToneDet_Type(VsmEnableDisabled):
    """Custom type vsmCodingProfSinFreqToneDet based on VsmEnableDisabled"""


_VsmCodingProfSinFreqToneDet_Object = MibTableColumn
vsmCodingProfSinFreqToneDet = _VsmCodingProfSinFreqToneDet_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 48),
    _VsmCodingProfSinFreqToneDet_Type()
)
vsmCodingProfSinFreqToneDet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfSinFreqToneDet.setStatus("mandatory")
_VsmCodingProfRowStatus_Type = RowStatus
_VsmCodingProfRowStatus_Object = MibTableColumn
vsmCodingProfRowStatus = _VsmCodingProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 3, 1, 1, 49),
    _VsmCodingProfRowStatus_Type()
)
vsmCodingProfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCodingProfRowStatus.setStatus("mandatory")
_VsmDialSchemeGroup_ObjectIdentity = ObjectIdentity
vsmDialSchemeGroup = _VsmDialSchemeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4)
)
_VsmDestinationsTable_Object = MibTable
vsmDestinationsTable = _VsmDestinationsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 1)
)
if mibBuilder.loadTexts:
    vsmDestinationsTable.setStatus("mandatory")
_VsmDestinationsEntry_Object = MibTableRow
vsmDestinationsEntry = _VsmDestinationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 1, 1)
)
vsmDestinationsEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmDestinationsName"),
)
if mibBuilder.loadTexts:
    vsmDestinationsEntry.setStatus("mandatory")
_VsmDestinationsName_Type = DisplayString
_VsmDestinationsName_Object = MibTableColumn
vsmDestinationsName = _VsmDestinationsName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 1, 1, 1),
    _VsmDestinationsName_Type()
)
vsmDestinationsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmDestinationsName.setStatus("mandatory")
_VsmDestinationsIpAddr_Type = IpAddress
_VsmDestinationsIpAddr_Object = MibTableColumn
vsmDestinationsIpAddr = _VsmDestinationsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 1, 1, 2),
    _VsmDestinationsIpAddr_Type()
)
vsmDestinationsIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmDestinationsIpAddr.setStatus("mandatory")
_VsmDestinationsNetworkPort_Type = Integer32
_VsmDestinationsNetworkPort_Object = MibTableColumn
vsmDestinationsNetworkPort = _VsmDestinationsNetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 1, 1, 3),
    _VsmDestinationsNetworkPort_Type()
)
vsmDestinationsNetworkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmDestinationsNetworkPort.setStatus("mandatory")
_VsmDestinationsH323Name_Type = DisplayString
_VsmDestinationsH323Name_Object = MibTableColumn
vsmDestinationsH323Name = _VsmDestinationsH323Name_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 1, 1, 4),
    _VsmDestinationsH323Name_Type()
)
vsmDestinationsH323Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmDestinationsH323Name.setStatus("mandatory")
_VsmDestinationsLocalPort_Type = Integer32
_VsmDestinationsLocalPort_Object = MibTableColumn
vsmDestinationsLocalPort = _VsmDestinationsLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 1, 1, 5),
    _VsmDestinationsLocalPort_Type()
)
vsmDestinationsLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmDestinationsLocalPort.setStatus("mandatory")
_VsmDestinationsStartChan_Type = Integer32
_VsmDestinationsStartChan_Object = MibTableColumn
vsmDestinationsStartChan = _VsmDestinationsStartChan_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 1, 1, 6),
    _VsmDestinationsStartChan_Type()
)
vsmDestinationsStartChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmDestinationsStartChan.setStatus("mandatory")
_VsmDestinationsEndChan_Type = Integer32
_VsmDestinationsEndChan_Object = MibTableColumn
vsmDestinationsEndChan = _VsmDestinationsEndChan_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 1, 1, 7),
    _VsmDestinationsEndChan_Type()
)
vsmDestinationsEndChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmDestinationsEndChan.setStatus("mandatory")


class _VsmDestinationsType_Type(Integer32):
    """Custom type vsmDestinationsType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("h323", 1)
    )


_VsmDestinationsType_Type.__name__ = "Integer32"
_VsmDestinationsType_Object = MibTableColumn
vsmDestinationsType = _VsmDestinationsType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 1, 1, 8),
    _VsmDestinationsType_Type()
)
vsmDestinationsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmDestinationsType.setStatus("mandatory")
_VsmDestinationsRowStatus_Type = RowStatus
_VsmDestinationsRowStatus_Object = MibTableColumn
vsmDestinationsRowStatus = _VsmDestinationsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 1, 1, 9),
    _VsmDestinationsRowStatus_Type()
)
vsmDestinationsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmDestinationsRowStatus.setStatus("mandatory")
_VsmPhoneGroupTable_Object = MibTable
vsmPhoneGroupTable = _VsmPhoneGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2)
)
if mibBuilder.loadTexts:
    vsmPhoneGroupTable.setStatus("mandatory")
_VsmPhoneGroupEntry_Object = MibTableRow
vsmPhoneGroupEntry = _VsmPhoneGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1)
)
vsmPhoneGroupEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmPhoneGroupName"),
)
if mibBuilder.loadTexts:
    vsmPhoneGroupEntry.setStatus("mandatory")
_VsmPhoneGroupName_Type = DisplayString
_VsmPhoneGroupName_Object = MibTableColumn
vsmPhoneGroupName = _VsmPhoneGroupName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1, 1),
    _VsmPhoneGroupName_Type()
)
vsmPhoneGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPhoneGroupName.setStatus("mandatory")


class _VsmPhoneGroupType_Type(Integer32):
    """Custom type vsmPhoneGroupType based on Integer32"""
    defaultValue = 1

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
        *(("internationalExt", 3),
          ("internationalPstn", 5),
          ("localExt", 1),
          ("nanpExt", 2),
          ("nanpPstn", 4))
    )


_VsmPhoneGroupType_Type.__name__ = "Integer32"
_VsmPhoneGroupType_Object = MibTableColumn
vsmPhoneGroupType = _VsmPhoneGroupType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1, 2),
    _VsmPhoneGroupType_Type()
)
vsmPhoneGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPhoneGroupType.setStatus("mandatory")
_VsmPhoneGroupFormat_Type = DisplayString
_VsmPhoneGroupFormat_Object = MibTableColumn
vsmPhoneGroupFormat = _VsmPhoneGroupFormat_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1, 3),
    _VsmPhoneGroupFormat_Type()
)
vsmPhoneGroupFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPhoneGroupFormat.setStatus("mandatory")


class _VsmPhoneGroupUsageVoice_Type(VsmEnableDisabled):
    """Custom type vsmPhoneGroupUsageVoice based on VsmEnableDisabled"""


_VsmPhoneGroupUsageVoice_Object = MibTableColumn
vsmPhoneGroupUsageVoice = _VsmPhoneGroupUsageVoice_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1, 4),
    _VsmPhoneGroupUsageVoice_Type()
)
vsmPhoneGroupUsageVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPhoneGroupUsageVoice.setStatus("mandatory")


class _VsmPhoneGroupUsageFax_Type(VsmEnableDisabled):
    """Custom type vsmPhoneGroupUsageFax based on VsmEnableDisabled"""


_VsmPhoneGroupUsageFax_Object = MibTableColumn
vsmPhoneGroupUsageFax = _VsmPhoneGroupUsageFax_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1, 5),
    _VsmPhoneGroupUsageFax_Type()
)
vsmPhoneGroupUsageFax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPhoneGroupUsageFax.setStatus("mandatory")


class _VsmPhoneGroupUsageModem_Type(VsmEnableDisabled):
    """Custom type vsmPhoneGroupUsageModem based on VsmEnableDisabled"""


_VsmPhoneGroupUsageModem_Object = MibTableColumn
vsmPhoneGroupUsageModem = _VsmPhoneGroupUsageModem_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1, 6),
    _VsmPhoneGroupUsageModem_Type()
)
vsmPhoneGroupUsageModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPhoneGroupUsageModem.setStatus("mandatory")


class _VsmPhoneGroupUsageData_Type(VsmEnableDisabled):
    """Custom type vsmPhoneGroupUsageData based on VsmEnableDisabled"""


_VsmPhoneGroupUsageData_Object = MibTableColumn
vsmPhoneGroupUsageData = _VsmPhoneGroupUsageData_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1, 7),
    _VsmPhoneGroupUsageData_Type()
)
vsmPhoneGroupUsageData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPhoneGroupUsageData.setStatus("mandatory")


class _VsmPhoneGroupSitePrefixEnable_Type(VsmEnableDisabled):
    """Custom type vsmPhoneGroupSitePrefixEnable based on VsmEnableDisabled"""


_VsmPhoneGroupSitePrefixEnable_Object = MibTableColumn
vsmPhoneGroupSitePrefixEnable = _VsmPhoneGroupSitePrefixEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1, 8),
    _VsmPhoneGroupSitePrefixEnable_Type()
)
vsmPhoneGroupSitePrefixEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPhoneGroupSitePrefixEnable.setStatus("mandatory")
_VsmPhoneGroupSitePrefixString_Type = DisplayString
_VsmPhoneGroupSitePrefixString_Object = MibTableColumn
vsmPhoneGroupSitePrefixString = _VsmPhoneGroupSitePrefixString_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1, 9),
    _VsmPhoneGroupSitePrefixString_Type()
)
vsmPhoneGroupSitePrefixString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPhoneGroupSitePrefixString.setStatus("mandatory")


class _VsmPhoneGroupStripDigitLength_Type(Integer32):
    """Custom type vsmPhoneGroupStripDigitLength based on Integer32"""
    defaultValue = 0


_VsmPhoneGroupStripDigitLength_Object = MibTableColumn
vsmPhoneGroupStripDigitLength = _VsmPhoneGroupStripDigitLength_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1, 10),
    _VsmPhoneGroupStripDigitLength_Type()
)
vsmPhoneGroupStripDigitLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPhoneGroupStripDigitLength.setStatus("mandatory")


class _VsmPhoneGroupForwardingPrefixEnable_Type(VsmEnableDisabled):
    """Custom type vsmPhoneGroupForwardingPrefixEnable based on VsmEnableDisabled"""


_VsmPhoneGroupForwardingPrefixEnable_Object = MibTableColumn
vsmPhoneGroupForwardingPrefixEnable = _VsmPhoneGroupForwardingPrefixEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1, 11),
    _VsmPhoneGroupForwardingPrefixEnable_Type()
)
vsmPhoneGroupForwardingPrefixEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPhoneGroupForwardingPrefixEnable.setStatus("mandatory")
_VsmPhoneGroupForwardingPrefix_Type = DisplayString
_VsmPhoneGroupForwardingPrefix_Object = MibTableColumn
vsmPhoneGroupForwardingPrefix = _VsmPhoneGroupForwardingPrefix_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1, 12),
    _VsmPhoneGroupForwardingPrefix_Type()
)
vsmPhoneGroupForwardingPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPhoneGroupForwardingPrefix.setStatus("mandatory")
_VsmPhoneGroupRowStatus_Type = RowStatus
_VsmPhoneGroupRowStatus_Object = MibTableColumn
vsmPhoneGroupRowStatus = _VsmPhoneGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 2, 1, 13),
    _VsmPhoneGroupRowStatus_Type()
)
vsmPhoneGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPhoneGroupRowStatus.setStatus("mandatory")
_VsmPGNumbersTable_Object = MibTable
vsmPGNumbersTable = _VsmPGNumbersTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 3)
)
if mibBuilder.loadTexts:
    vsmPGNumbersTable.setStatus("mandatory")
_VsmPGNumbersEntry_Object = MibTableRow
vsmPGNumbersEntry = _VsmPGNumbersEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 3, 1)
)
vsmPGNumbersEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmPhoneGroupName"),
    (0, "XYLAN-VSM-MIB", "vsmPGNumber"),
)
if mibBuilder.loadTexts:
    vsmPGNumbersEntry.setStatus("mandatory")
_VsmPGNumber_Type = DisplayString
_VsmPGNumber_Object = MibTableColumn
vsmPGNumber = _VsmPGNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 3, 1, 1),
    _VsmPGNumber_Type()
)
vsmPGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmPGNumber.setStatus("mandatory")
_VsmPGNumbersRowStatus_Type = RowStatus
_VsmPGNumbersRowStatus_Object = MibTableColumn
vsmPGNumbersRowStatus = _VsmPGNumbersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 3, 1, 2),
    _VsmPGNumbersRowStatus_Type()
)
vsmPGNumbersRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPGNumbersRowStatus.setStatus("mandatory")
_VsmNumPlanTable_Object = MibTable
vsmNumPlanTable = _VsmNumPlanTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 4)
)
if mibBuilder.loadTexts:
    vsmNumPlanTable.setStatus("mandatory")
_VsmNumPlanEntry_Object = MibTableRow
vsmNumPlanEntry = _VsmNumPlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 4, 1)
)
vsmNumPlanEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmNumPlanName"),
)
if mibBuilder.loadTexts:
    vsmNumPlanEntry.setStatus("mandatory")
_VsmNumPlanName_Type = DisplayString
_VsmNumPlanName_Object = MibTableColumn
vsmNumPlanName = _VsmNumPlanName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 4, 1, 1),
    _VsmNumPlanName_Type()
)
vsmNumPlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmNumPlanName.setStatus("mandatory")


class _VsmNumPlanHuntMethod_Type(Integer32):
    """Custom type vsmNumPlanHuntMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("roundRobin", 1),
          ("topDown", 2))
    )


_VsmNumPlanHuntMethod_Type.__name__ = "Integer32"
_VsmNumPlanHuntMethod_Object = MibTableColumn
vsmNumPlanHuntMethod = _VsmNumPlanHuntMethod_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 4, 1, 2),
    _VsmNumPlanHuntMethod_Type()
)
vsmNumPlanHuntMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmNumPlanHuntMethod.setStatus("mandatory")
_VsmNumPlanDescription_Type = DisplayString
_VsmNumPlanDescription_Object = MibTableColumn
vsmNumPlanDescription = _VsmNumPlanDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 4, 1, 3),
    _VsmNumPlanDescription_Type()
)
vsmNumPlanDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmNumPlanDescription.setStatus("mandatory")


class _VsmNumPlanAllActivate_Type(Integer32):
    """Custom type vsmNumPlanAllActivate based on Integer32"""
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
        *(("activate", 1),
          ("active", 2),
          ("inactive", 3),
          ("invalid", 4))
    )


_VsmNumPlanAllActivate_Type.__name__ = "Integer32"
_VsmNumPlanAllActivate_Object = MibTableColumn
vsmNumPlanAllActivate = _VsmNumPlanAllActivate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 4, 1, 4),
    _VsmNumPlanAllActivate_Type()
)
vsmNumPlanAllActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmNumPlanAllActivate.setStatus("mandatory")
_VsmNumPlanRowStatus_Type = RowStatus
_VsmNumPlanRowStatus_Object = MibTableColumn
vsmNumPlanRowStatus = _VsmNumPlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 4, 1, 5),
    _VsmNumPlanRowStatus_Type()
)
vsmNumPlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmNumPlanRowStatus.setStatus("mandatory")
_VsmNPPhoneGroupTable_Object = MibTable
vsmNPPhoneGroupTable = _VsmNPPhoneGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 5)
)
if mibBuilder.loadTexts:
    vsmNPPhoneGroupTable.setStatus("mandatory")
_VsmNPPhoneGroupEntry_Object = MibTableRow
vsmNPPhoneGroupEntry = _VsmNPPhoneGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 5, 1)
)
vsmNPPhoneGroupEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmNumPlanName"),
    (0, "XYLAN-VSM-MIB", "vsmPhoneGroupName"),
)
if mibBuilder.loadTexts:
    vsmNPPhoneGroupEntry.setStatus("mandatory")
_VsmNPPhoneGroupRowStatus_Type = RowStatus
_VsmNPPhoneGroupRowStatus_Object = MibTableColumn
vsmNPPhoneGroupRowStatus = _VsmNPPhoneGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 5, 1, 1),
    _VsmNPPhoneGroupRowStatus_Type()
)
vsmNPPhoneGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmNPPhoneGroupRowStatus.setStatus("mandatory")
_VsmNPDestinationsTable_Object = MibTable
vsmNPDestinationsTable = _VsmNPDestinationsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 6)
)
if mibBuilder.loadTexts:
    vsmNPDestinationsTable.setStatus("mandatory")
_VsmNPDestinationsEntry_Object = MibTableRow
vsmNPDestinationsEntry = _VsmNPDestinationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 6, 1)
)
vsmNPDestinationsEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmNumPlanName"),
    (0, "XYLAN-VSM-MIB", "vsmDestinationsName"),
)
if mibBuilder.loadTexts:
    vsmNPDestinationsEntry.setStatus("mandatory")
_VsmNPDestinationsRowStatus_Type = RowStatus
_VsmNPDestinationsRowStatus_Object = MibTableColumn
vsmNPDestinationsRowStatus = _VsmNPDestinationsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 4, 6, 1, 1),
    _VsmNPDestinationsRowStatus_Type()
)
vsmNPDestinationsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmNPDestinationsRowStatus.setStatus("mandatory")
_VsmPhysicalGroup_ObjectIdentity = ObjectIdentity
vsmPhysicalGroup = _VsmPhysicalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5)
)
_VsmCardConfTable_Object = MibTable
vsmCardConfTable = _VsmCardConfTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1)
)
if mibBuilder.loadTexts:
    vsmCardConfTable.setStatus("mandatory")
_VsmCardConfEntry_Object = MibTableRow
vsmCardConfEntry = _VsmCardConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1)
)
vsmCardConfEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmCardSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmCardSubunitIndex"),
)
if mibBuilder.loadTexts:
    vsmCardConfEntry.setStatus("mandatory")


class _VsmCardSlotIndex_Type(Integer32):
    """Custom type vsmCardSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_VsmCardSlotIndex_Type.__name__ = "Integer32"
_VsmCardSlotIndex_Object = MibTableColumn
vsmCardSlotIndex = _VsmCardSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1, 1),
    _VsmCardSlotIndex_Type()
)
vsmCardSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardSlotIndex.setStatus("mandatory")
_VsmCardSubunitIndex_Type = XylanModuleSubunit
_VsmCardSubunitIndex_Object = MibTableColumn
vsmCardSubunitIndex = _VsmCardSubunitIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1, 2),
    _VsmCardSubunitIndex_Type()
)
vsmCardSubunitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmCardSubunitIndex.setStatus("mandatory")
_VsmCardIpAddr_Type = IpAddress
_VsmCardIpAddr_Object = MibTableColumn
vsmCardIpAddr = _VsmCardIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1, 3),
    _VsmCardIpAddr_Type()
)
vsmCardIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCardIpAddr.setStatus("mandatory")
_VsmCardIpMask_Type = IpAddress
_VsmCardIpMask_Object = MibTableColumn
vsmCardIpMask = _VsmCardIpMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1, 4),
    _VsmCardIpMask_Type()
)
vsmCardIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCardIpMask.setStatus("mandatory")
_VsmCardIpDefGateway_Type = IpAddress
_VsmCardIpDefGateway_Object = MibTableColumn
vsmCardIpDefGateway = _VsmCardIpDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1, 5),
    _VsmCardIpDefGateway_Type()
)
vsmCardIpDefGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCardIpDefGateway.setStatus("mandatory")


class _VsmCardFirstDigitWaitDur_Type(Integer32):
    """Custom type vsmCardFirstDigitWaitDur based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VsmCardFirstDigitWaitDur_Type.__name__ = "Integer32"
_VsmCardFirstDigitWaitDur_Object = MibTableColumn
vsmCardFirstDigitWaitDur = _VsmCardFirstDigitWaitDur_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1, 6),
    _VsmCardFirstDigitWaitDur_Type()
)
vsmCardFirstDigitWaitDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCardFirstDigitWaitDur.setStatus("mandatory")


class _VsmCardInterDigitWaitDur_Type(Integer32):
    """Custom type vsmCardInterDigitWaitDur based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VsmCardInterDigitWaitDur_Type.__name__ = "Integer32"
_VsmCardInterDigitWaitDur_Object = MibTableColumn
vsmCardInterDigitWaitDur = _VsmCardInterDigitWaitDur_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1, 7),
    _VsmCardInterDigitWaitDur_Type()
)
vsmCardInterDigitWaitDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCardInterDigitWaitDur.setStatus("mandatory")


class _VsmCardDialTimeDur_Type(Integer32):
    """Custom type vsmCardDialTimeDur based on Integer32"""
    defaultValue = 30000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VsmCardDialTimeDur_Type.__name__ = "Integer32"
_VsmCardDialTimeDur_Object = MibTableColumn
vsmCardDialTimeDur = _VsmCardDialTimeDur_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1, 8),
    _VsmCardDialTimeDur_Type()
)
vsmCardDialTimeDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCardDialTimeDur.setStatus("mandatory")
_VsmCardTermDigitStr_Type = DisplayString
_VsmCardTermDigitStr_Object = MibTableColumn
vsmCardTermDigitStr = _VsmCardTermDigitStr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1, 9),
    _VsmCardTermDigitStr_Type()
)
vsmCardTermDigitStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCardTermDigitStr.setStatus("mandatory")


class _VsmCardH323InFastStart_Type(VsmEnableDisabled):
    """Custom type vsmCardH323InFastStart based on VsmEnableDisabled"""


_VsmCardH323InFastStart_Object = MibTableColumn
vsmCardH323InFastStart = _VsmCardH323InFastStart_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1, 10),
    _VsmCardH323InFastStart_Type()
)
vsmCardH323InFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCardH323InFastStart.setStatus("mandatory")


class _VsmCardH323OutFastStart_Type(VsmEnableDisabled):
    """Custom type vsmCardH323OutFastStart based on VsmEnableDisabled"""


_VsmCardH323OutFastStart_Object = MibTableColumn
vsmCardH323OutFastStart = _VsmCardH323OutFastStart_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1, 11),
    _VsmCardH323OutFastStart_Type()
)
vsmCardH323OutFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCardH323OutFastStart.setStatus("mandatory")


class _VsmCardH323AutomaticAnswer_Type(VsmEnableDisabled):
    """Custom type vsmCardH323AutomaticAnswer based on VsmEnableDisabled"""


_VsmCardH323AutomaticAnswer_Object = MibTableColumn
vsmCardH323AutomaticAnswer = _VsmCardH323AutomaticAnswer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1, 12),
    _VsmCardH323AutomaticAnswer_Type()
)
vsmCardH323AutomaticAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCardH323AutomaticAnswer.setStatus("mandatory")


class _VsmCardConfigStatus_Type(Integer32):
    """Custom type vsmCardConfigStatus based on Integer32"""
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
        *(("activate", 1),
          ("active", 2),
          ("inactive", 3),
          ("invalid", 4))
    )


_VsmCardConfigStatus_Type.__name__ = "Integer32"
_VsmCardConfigStatus_Object = MibTableColumn
vsmCardConfigStatus = _VsmCardConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 1, 1, 13),
    _VsmCardConfigStatus_Type()
)
vsmCardConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmCardConfigStatus.setStatus("mandatory")
_VsmPortConfTable_Object = MibTable
vsmPortConfTable = _VsmPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2)
)
if mibBuilder.loadTexts:
    vsmPortConfTable.setStatus("mandatory")
_VsmPortConfEntry_Object = MibTableRow
vsmPortConfEntry = _VsmPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1)
)
vsmPortConfEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmPortSlotNum"),
    (0, "XYLAN-VSM-MIB", "vsmPortNum"),
)
if mibBuilder.loadTexts:
    vsmPortConfEntry.setStatus("mandatory")
_VsmPortSlotNum_Type = Integer32
_VsmPortSlotNum_Object = MibTableColumn
vsmPortSlotNum = _VsmPortSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 1),
    _VsmPortSlotNum_Type()
)
vsmPortSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmPortSlotNum.setStatus("mandatory")
_VsmPortNum_Type = Integer32
_VsmPortNum_Object = MibTableColumn
vsmPortNum = _VsmPortNum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 2),
    _VsmPortNum_Type()
)
vsmPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmPortNum.setStatus("mandatory")


class _VsmPortInterfaceType_Type(Integer32):
    """Custom type vsmPortInterfaceType based on Integer32"""
    defaultValue = 1

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
        *(("briEuro", 5),
          ("e1", 2),
          ("e1IsdnPri", 4),
          ("prie1", 3),
          ("t1", 1))
    )


_VsmPortInterfaceType_Type.__name__ = "Integer32"
_VsmPortInterfaceType_Object = MibTableColumn
vsmPortInterfaceType = _VsmPortInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 3),
    _VsmPortInterfaceType_Type()
)
vsmPortInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmPortInterfaceType.setStatus("mandatory")


class _VsmPortDialType_Type(Integer32):
    """Custom type vsmPortDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pulse", 2),
          ("tone", 1))
    )


_VsmPortDialType_Type.__name__ = "Integer32"
_VsmPortDialType_Object = MibTableColumn
vsmPortDialType = _VsmPortDialType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 4),
    _VsmPortDialType_Type()
)
vsmPortDialType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDialType.setStatus("deprecated")


class _VsmPortDsx1LineType_Type(Integer32):
    """Custom type vsmPortDsx1LineType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("vsmPortDsx1D4", 3),
          ("vsmPortDsx1E1", 4),
          ("vsmPortDsx1E1-CRC", 5),
          ("vsmPortDsx1E1-CRC-MF", 7),
          ("vsmPortDsx1E1-MF", 6),
          ("vsmPortDsx1E1Unframed", 8),
          ("vsmPortDsx1ESF", 2))
    )


_VsmPortDsx1LineType_Type.__name__ = "Integer32"
_VsmPortDsx1LineType_Object = MibTableColumn
vsmPortDsx1LineType = _VsmPortDsx1LineType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 5),
    _VsmPortDsx1LineType_Type()
)
vsmPortDsx1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1LineType.setStatus("mandatory")


class _VsmPortDsx1LineCoding_Type(Integer32):
    """Custom type vsmPortDsx1LineCoding based on Integer32"""
    defaultValue = 1

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
        *(("other", 5),
          ("vsmPortDsx1AMI", 4),
          ("vsmPortDsx1B8ZS", 2),
          ("vsmPortDsx1HDB3", 3),
          ("vsmPortDsx1JBZS", 1))
    )


_VsmPortDsx1LineCoding_Type.__name__ = "Integer32"
_VsmPortDsx1LineCoding_Object = MibTableColumn
vsmPortDsx1LineCoding = _VsmPortDsx1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 6),
    _VsmPortDsx1LineCoding_Type()
)
vsmPortDsx1LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1LineCoding.setStatus("mandatory")


class _VsmPortDsx1SendCode_Type(Integer32):
    """Custom type vsmPortDsx1SendCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("vsmPortDsx1Send3in24Pattern", 7),
          ("vsmPortDsx1Send511Pattern", 6),
          ("vsmPortDsx1SendLineCode", 2),
          ("vsmPortDsx1SendNoCode", 1),
          ("vsmPortDsx1SendOtherTestPattern", 8),
          ("vsmPortDsx1SendPayloadCode", 3),
          ("vsmPortDsx1SendQRS", 5),
          ("vsmPortDsx1SendResetCode", 4))
    )


_VsmPortDsx1SendCode_Type.__name__ = "Integer32"
_VsmPortDsx1SendCode_Object = MibTableColumn
vsmPortDsx1SendCode = _VsmPortDsx1SendCode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 7),
    _VsmPortDsx1SendCode_Type()
)
vsmPortDsx1SendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1SendCode.setStatus("mandatory")


class _VsmPortDsx1CircuitIdentifier_Type(DisplayString):
    """Custom type vsmPortDsx1CircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VsmPortDsx1CircuitIdentifier_Type.__name__ = "DisplayString"
_VsmPortDsx1CircuitIdentifier_Object = MibTableColumn
vsmPortDsx1CircuitIdentifier = _VsmPortDsx1CircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 8),
    _VsmPortDsx1CircuitIdentifier_Type()
)
vsmPortDsx1CircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1CircuitIdentifier.setStatus("mandatory")


class _VsmPortDsx1LoopbackConfig_Type(Integer32):
    """Custom type vsmPortDsx1LoopbackConfig based on Integer32"""
    defaultValue = 1

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
        *(("vsmDSx1Inward", 4),
          ("vsmPortDsx1LineLoop", 3),
          ("vsmPortDsx1NoLoop", 1),
          ("vsmPortDsx1OtherLoop", 5),
          ("vsmPortDsx1PayloadLoop", 2))
    )


_VsmPortDsx1LoopbackConfig_Type.__name__ = "Integer32"
_VsmPortDsx1LoopbackConfig_Object = MibTableColumn
vsmPortDsx1LoopbackConfig = _VsmPortDsx1LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 9),
    _VsmPortDsx1LoopbackConfig_Type()
)
vsmPortDsx1LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1LoopbackConfig.setStatus("mandatory")


class _VsmPortDsx1LineStatus_Type(Integer32):
    """Custom type vsmPortDsx1LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_VsmPortDsx1LineStatus_Type.__name__ = "Integer32"
_VsmPortDsx1LineStatus_Object = MibTableColumn
vsmPortDsx1LineStatus = _VsmPortDsx1LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 10),
    _VsmPortDsx1LineStatus_Type()
)
vsmPortDsx1LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmPortDsx1LineStatus.setStatus("deprecated")


class _VsmPortDsx1SignalMode_Type(Integer32):
    """Custom type vsmPortDsx1SignalMode based on Integer32"""
    defaultValue = 1

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
        *(("cas", 2),
          ("ccs", 3),
          ("messageOriented", 4),
          ("none", 1))
    )


_VsmPortDsx1SignalMode_Type.__name__ = "Integer32"
_VsmPortDsx1SignalMode_Object = MibTableColumn
vsmPortDsx1SignalMode = _VsmPortDsx1SignalMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 11),
    _VsmPortDsx1SignalMode_Type()
)
vsmPortDsx1SignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1SignalMode.setStatus("mandatory")


class _VsmPortDsx1TransmitClockSource_Type(Integer32):
    """Custom type vsmPortDsx1TransmitClockSource based on Integer32"""
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
        *(("localTiming", 2),
          ("loopTiming", 1),
          ("throughTiming", 3))
    )


_VsmPortDsx1TransmitClockSource_Type.__name__ = "Integer32"
_VsmPortDsx1TransmitClockSource_Object = MibTableColumn
vsmPortDsx1TransmitClockSource = _VsmPortDsx1TransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 12),
    _VsmPortDsx1TransmitClockSource_Type()
)
vsmPortDsx1TransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1TransmitClockSource.setStatus("mandatory")


class _VsmPortDsx1Fdl_Type(Integer32):
    """Custom type vsmPortDsx1Fdl based on Integer32"""
    defaultValue = 1

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
        *(("other", 5),
          ("vsmPortDsx1Ansi-T1-403", 3),
          ("vsmPortDsx1Att-54016", 2),
          ("vsmPortDsx1Fdl-none", 1),
          ("vsmPortDsx1T1-403-ATT", 4))
    )


_VsmPortDsx1Fdl_Type.__name__ = "Integer32"
_VsmPortDsx1Fdl_Object = MibTableColumn
vsmPortDsx1Fdl = _VsmPortDsx1Fdl_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 13),
    _VsmPortDsx1Fdl_Type()
)
vsmPortDsx1Fdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1Fdl.setStatus("mandatory")


class _VsmPortDsx1LineBuildOut_Type(Integer32):
    """Custom type vsmPortDsx1LineBuildOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("longHaul", 2),
          ("shortHaul", 1))
    )


_VsmPortDsx1LineBuildOut_Type.__name__ = "Integer32"
_VsmPortDsx1LineBuildOut_Object = MibTableColumn
vsmPortDsx1LineBuildOut = _VsmPortDsx1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 14),
    _VsmPortDsx1LineBuildOut_Type()
)
vsmPortDsx1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1LineBuildOut.setStatus("mandatory")


class _VsmPortDsx1CableType_Type(Integer32):
    """Custom type vsmPortDsx1CableType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cable120ohm", 2),
          ("cable75ohm", 1))
    )


_VsmPortDsx1CableType_Type.__name__ = "Integer32"
_VsmPortDsx1CableType_Object = MibTableColumn
vsmPortDsx1CableType = _VsmPortDsx1CableType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 15),
    _VsmPortDsx1CableType_Type()
)
vsmPortDsx1CableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1CableType.setStatus("mandatory")


class _VsmPortDsx1LineLength_Type(Integer32):
    """Custom type vsmPortDsx1LineLength based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_VsmPortDsx1LineLength_Type.__name__ = "Integer32"
_VsmPortDsx1LineLength_Object = MibTableColumn
vsmPortDsx1LineLength = _VsmPortDsx1LineLength_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 16),
    _VsmPortDsx1LineLength_Type()
)
vsmPortDsx1LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1LineLength.setStatus("mandatory")


class _VsmPortDsx1LineStatusChangeTrapEnable_Type(Integer32):
    """Custom type vsmPortDsx1LineStatusChangeTrapEnable based on Integer32"""
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


_VsmPortDsx1LineStatusChangeTrapEnable_Type.__name__ = "Integer32"
_VsmPortDsx1LineStatusChangeTrapEnable_Object = MibTableColumn
vsmPortDsx1LineStatusChangeTrapEnable = _VsmPortDsx1LineStatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 17),
    _VsmPortDsx1LineStatusChangeTrapEnable_Type()
)
vsmPortDsx1LineStatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1LineStatusChangeTrapEnable.setStatus("mandatory")


class _VsmPortDsx1LoopbackStatus_Type(Integer32):
    """Custom type vsmPortDsx1LoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_VsmPortDsx1LoopbackStatus_Type.__name__ = "Integer32"
_VsmPortDsx1LoopbackStatus_Object = MibTableColumn
vsmPortDsx1LoopbackStatus = _VsmPortDsx1LoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 18),
    _VsmPortDsx1LoopbackStatus_Type()
)
vsmPortDsx1LoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmPortDsx1LoopbackStatus.setStatus("deprecated")


class _VsmPortDsx1PortFdlRole_Type(Integer32):
    """Custom type vsmPortDsx1PortFdlRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("user", 2))
    )


_VsmPortDsx1PortFdlRole_Type.__name__ = "Integer32"
_VsmPortDsx1PortFdlRole_Object = MibTableColumn
vsmPortDsx1PortFdlRole = _VsmPortDsx1PortFdlRole_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 19),
    _VsmPortDsx1PortFdlRole_Type()
)
vsmPortDsx1PortFdlRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1PortFdlRole.setStatus("mandatory")


class _VsmPortDsx1PortNfasAlign_Type(Integer32):
    """Custom type vsmPortDsx1PortNfasAlign based on Integer32"""
    defaultValue = 2

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


_VsmPortDsx1PortNfasAlign_Type.__name__ = "Integer32"
_VsmPortDsx1PortNfasAlign_Object = MibTableColumn
vsmPortDsx1PortNfasAlign = _VsmPortDsx1PortNfasAlign_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 20),
    _VsmPortDsx1PortNfasAlign_Type()
)
vsmPortDsx1PortNfasAlign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1PortNfasAlign.setStatus("mandatory")


class _VsmPortDsx1PortAttenuation_Type(Integer32):
    """Custom type vsmPortDsx1PortAttenuation based on Integer32"""
    defaultValue = 1

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
        *(("att1", 1),
          ("att2", 2),
          ("att3", 3),
          ("att4", 4))
    )


_VsmPortDsx1PortAttenuation_Type.__name__ = "Integer32"
_VsmPortDsx1PortAttenuation_Object = MibTableColumn
vsmPortDsx1PortAttenuation = _VsmPortDsx1PortAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 21),
    _VsmPortDsx1PortAttenuation_Type()
)
vsmPortDsx1PortAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortDsx1PortAttenuation.setStatus("mandatory")


class _VsmPortIsdnProtocol_Type(Integer32):
    """Custom type vsmPortIsdnProtocol based on Integer32"""
    defaultValue = 3

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
        *(("net", 1),
          ("qmaster", 3),
          ("qslave", 4),
          ("user", 2))
    )


_VsmPortIsdnProtocol_Type.__name__ = "Integer32"
_VsmPortIsdnProtocol_Object = MibTableColumn
vsmPortIsdnProtocol = _VsmPortIsdnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 22),
    _VsmPortIsdnProtocol_Type()
)
vsmPortIsdnProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortIsdnProtocol.setStatus("mandatory")


class _VsmPortIsdnSwitchType_Type(Integer32):
    """Custom type vsmPortIsdnSwitchType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("net3", 1),
          ("net5", 2))
    )


_VsmPortIsdnSwitchType_Type.__name__ = "Integer32"
_VsmPortIsdnSwitchType_Object = MibTableColumn
vsmPortIsdnSwitchType = _VsmPortIsdnSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 2, 1, 23),
    _VsmPortIsdnSwitchType_Type()
)
vsmPortIsdnSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmPortIsdnSwitchType.setStatus("mandatory")
_VsmChanConfTable_Object = MibTable
vsmChanConfTable = _VsmChanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3)
)
if mibBuilder.loadTexts:
    vsmChanConfTable.setStatus("mandatory")
_VsmChanConfEntry_Object = MibTableRow
vsmChanConfEntry = _VsmChanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1)
)
vsmChanConfEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmChanConfEntry.setStatus("mandatory")
_VsmChanSlotIndex_Type = Integer32
_VsmChanSlotIndex_Object = MibTableColumn
vsmChanSlotIndex = _VsmChanSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1, 1),
    _VsmChanSlotIndex_Type()
)
vsmChanSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmChanSlotIndex.setStatus("mandatory")
_VsmChanPortIndex_Type = Integer32
_VsmChanPortIndex_Object = MibTableColumn
vsmChanPortIndex = _VsmChanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1, 2),
    _VsmChanPortIndex_Type()
)
vsmChanPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmChanPortIndex.setStatus("mandatory")
_VsmChanIndex_Type = Integer32
_VsmChanIndex_Object = MibTableColumn
vsmChanIndex = _VsmChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1, 3),
    _VsmChanIndex_Type()
)
vsmChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmChanIndex.setStatus("mandatory")


class _VsmChanMode_Type(Integer32):
    """Custom type vsmChanMode based on Integer32"""
    defaultValue = 1

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
        *(("passThrough", 2),
          ("plar", 3),
          ("telephony", 1),
          ("wan", 4))
    )


_VsmChanMode_Type.__name__ = "Integer32"
_VsmChanMode_Object = MibTableColumn
vsmChanMode = _VsmChanMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1, 4),
    _VsmChanMode_Type()
)
vsmChanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmChanMode.setStatus("mandatory")
_VsmChanPlarNumber_Type = DisplayString
_VsmChanPlarNumber_Object = MibTableColumn
vsmChanPlarNumber = _VsmChanPlarNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1, 5),
    _VsmChanPlarNumber_Type()
)
vsmChanPlarNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmChanPlarNumber.setStatus("mandatory")
_VsmChanPerferredVoiceProfile_Type = DisplayString
_VsmChanPerferredVoiceProfile_Object = MibTableColumn
vsmChanPerferredVoiceProfile = _VsmChanPerferredVoiceProfile_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1, 6),
    _VsmChanPerferredVoiceProfile_Type()
)
vsmChanPerferredVoiceProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmChanPerferredVoiceProfile.setStatus("mandatory")
_VsmChanPerferredFaxProfile_Type = DisplayString
_VsmChanPerferredFaxProfile_Object = MibTableColumn
vsmChanPerferredFaxProfile = _VsmChanPerferredFaxProfile_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1, 7),
    _VsmChanPerferredFaxProfile_Type()
)
vsmChanPerferredFaxProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmChanPerferredFaxProfile.setStatus("mandatory")
_VsmChanPerferredModemProfile_Type = DisplayString
_VsmChanPerferredModemProfile_Object = MibTableColumn
vsmChanPerferredModemProfile = _VsmChanPerferredModemProfile_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1, 8),
    _VsmChanPerferredModemProfile_Type()
)
vsmChanPerferredModemProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmChanPerferredModemProfile.setStatus("mandatory")


class _VsmChanISDNChanType_Type(Integer32):
    """Custom type vsmChanISDNChanType based on Integer32"""
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
        *(("bchannel", 2),
          ("dchannel", 1),
          ("none", 3))
    )


_VsmChanISDNChanType_Type.__name__ = "Integer32"
_VsmChanISDNChanType_Object = MibTableColumn
vsmChanISDNChanType = _VsmChanISDNChanType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1, 9),
    _VsmChanISDNChanType_Type()
)
vsmChanISDNChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmChanISDNChanType.setStatus("mandatory")
_VsmChanDslId_Type = Integer32
_VsmChanDslId_Object = MibTableColumn
vsmChanDslId = _VsmChanDslId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1, 10),
    _VsmChanDslId_Type()
)
vsmChanDslId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmChanDslId.setStatus("deprecated")
_VsmChanDChannelPort_Type = Integer32
_VsmChanDChannelPort_Object = MibTableColumn
vsmChanDChannelPort = _VsmChanDChannelPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1, 11),
    _VsmChanDChannelPort_Type()
)
vsmChanDChannelPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmChanDChannelPort.setStatus("deprecated")
_VsmChanDChannel_Type = Integer32
_VsmChanDChannel_Object = MibTableColumn
vsmChanDChannel = _VsmChanDChannel_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1, 12),
    _VsmChanDChannel_Type()
)
vsmChanDChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmChanDChannel.setStatus("deprecated")


class _VsmChanStatus_Type(Integer32):
    """Custom type vsmChanStatus based on Integer32"""
    defaultValue = 4

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
        *(("activate", 1),
          ("deactivate", 2),
          ("in-service", 3),
          ("invalid", 5),
          ("out-of-service", 4))
    )


_VsmChanStatus_Type.__name__ = "Integer32"
_VsmChanStatus_Object = MibTableColumn
vsmChanStatus = _VsmChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 3, 1, 13),
    _VsmChanStatus_Type()
)
vsmChanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmChanStatus.setStatus("mandatory")
_VsmAllowedCodingProfileTable_Object = MibTable
vsmAllowedCodingProfileTable = _VsmAllowedCodingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 4)
)
if mibBuilder.loadTexts:
    vsmAllowedCodingProfileTable.setStatus("mandatory")
_VsmAllowedCodingProfileEntry_Object = MibTableRow
vsmAllowedCodingProfileEntry = _VsmAllowedCodingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 4, 1)
)
vsmAllowedCodingProfileEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
    (0, "XYLAN-VSM-MIB", "vsmCodingProfName"),
)
if mibBuilder.loadTexts:
    vsmAllowedCodingProfileEntry.setStatus("mandatory")
_VsmAllowedCodingProfileRowStatus_Type = RowStatus
_VsmAllowedCodingProfileRowStatus_Object = MibTableColumn
vsmAllowedCodingProfileRowStatus = _VsmAllowedCodingProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 5, 4, 1, 1),
    _VsmAllowedCodingProfileRowStatus_Type()
)
vsmAllowedCodingProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmAllowedCodingProfileRowStatus.setStatus("mandatory")
_VsmConfigControlGroup_ObjectIdentity = ObjectIdentity
vsmConfigControlGroup = _VsmConfigControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 6)
)
_VsmConfigDumpFlag_Type = Integer32
_VsmConfigDumpFlag_Object = MibScalar
vsmConfigDumpFlag = _VsmConfigDumpFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 6, 1),
    _VsmConfigDumpFlag_Type()
)
vsmConfigDumpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmConfigDumpFlag.setStatus("mandatory")
_VsmConfigRebootFlag_Type = Integer32
_VsmConfigRebootFlag_Object = MibScalar
vsmConfigRebootFlag = _VsmConfigRebootFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 6, 2),
    _VsmConfigRebootFlag_Type()
)
vsmConfigRebootFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmConfigRebootFlag.setStatus("mandatory")


class _VsmConfigDumpFileName_Type(DisplayString):
    """Custom type vsmConfigDumpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_VsmConfigDumpFileName_Type.__name__ = "DisplayString"
_VsmConfigDumpFileName_Object = MibScalar
vsmConfigDumpFileName = _VsmConfigDumpFileName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 6, 3),
    _VsmConfigDumpFileName_Type()
)
vsmConfigDumpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsmConfigDumpFileName.setStatus("mandatory")
_VsmStatsGroup_ObjectIdentity = ObjectIdentity
vsmStatsGroup = _VsmStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7)
)
_VsmTeleLevelTable_Object = MibTable
vsmTeleLevelTable = _VsmTeleLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 1)
)
if mibBuilder.loadTexts:
    vsmTeleLevelTable.setStatus("mandatory")
_VsmTeleLevelEntry_Object = MibTableRow
vsmTeleLevelEntry = _VsmTeleLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 1, 1)
)
vsmTeleLevelEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmTeleLevelEntry.setStatus("mandatory")
_VsmTeleLevelRx_Type = Integer32
_VsmTeleLevelRx_Object = MibTableColumn
vsmTeleLevelRx = _VsmTeleLevelRx_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 1, 1, 1),
    _VsmTeleLevelRx_Type()
)
vsmTeleLevelRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTeleLevelRx.setStatus("mandatory")
_VsmTeleLevelTx_Type = Integer32
_VsmTeleLevelTx_Object = MibTableColumn
vsmTeleLevelTx = _VsmTeleLevelTx_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 1, 1, 2),
    _VsmTeleLevelTx_Type()
)
vsmTeleLevelTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTeleLevelTx.setStatus("mandatory")
_VsmTeleLevelRxMean_Type = Integer32
_VsmTeleLevelRxMean_Object = MibTableColumn
vsmTeleLevelRxMean = _VsmTeleLevelRxMean_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 1, 1, 3),
    _VsmTeleLevelRxMean_Type()
)
vsmTeleLevelRxMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTeleLevelRxMean.setStatus("mandatory")
_VsmTeleLevelTxMean_Type = Integer32
_VsmTeleLevelTxMean_Object = MibTableColumn
vsmTeleLevelTxMean = _VsmTeleLevelTxMean_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 1, 1, 4),
    _VsmTeleLevelTxMean_Type()
)
vsmTeleLevelTxMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTeleLevelTxMean.setStatus("mandatory")
_VsmTeleStatsTable_Object = MibTable
vsmTeleStatsTable = _VsmTeleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 2)
)
if mibBuilder.loadTexts:
    vsmTeleStatsTable.setStatus("mandatory")
_VsmTeleStatsEntry_Object = MibTableRow
vsmTeleStatsEntry = _VsmTeleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 2, 1)
)
vsmTeleStatsEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmTeleStatsEntry.setStatus("mandatory")
_VsmNumOffHooks_Type = Integer32
_VsmNumOffHooks_Object = MibTableColumn
vsmNumOffHooks = _VsmNumOffHooks_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 2, 1, 1),
    _VsmNumOffHooks_Type()
)
vsmNumOffHooks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmNumOffHooks.setStatus("mandatory")
_VsmNumOnHooks_Type = Integer32
_VsmNumOnHooks_Object = MibTableColumn
vsmNumOnHooks = _VsmNumOnHooks_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 2, 1, 2),
    _VsmNumOnHooks_Type()
)
vsmNumOnHooks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmNumOnHooks.setStatus("mandatory")
_VsmNumSeizures_Type = Integer32
_VsmNumSeizures_Object = MibTableColumn
vsmNumSeizures = _VsmNumSeizures_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 2, 1, 3),
    _VsmNumSeizures_Type()
)
vsmNumSeizures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmNumSeizures.setStatus("mandatory")
_VsmNumToneDigits_Type = Integer32
_VsmNumToneDigits_Object = MibTableColumn
vsmNumToneDigits = _VsmNumToneDigits_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 2, 1, 4),
    _VsmNumToneDigits_Type()
)
vsmNumToneDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmNumToneDigits.setStatus("mandatory")
_VsmNumPulseDigits_Type = Integer32
_VsmNumPulseDigits_Object = MibTableColumn
vsmNumPulseDigits = _VsmNumPulseDigits_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 2, 1, 5),
    _VsmNumPulseDigits_Type()
)
vsmNumPulseDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmNumPulseDigits.setStatus("mandatory")
_VsmResetTeleStats_Type = Integer32
_VsmResetTeleStats_Object = MibTableColumn
vsmResetTeleStats = _VsmResetTeleStats_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 2, 1, 6),
    _VsmResetTeleStats_Type()
)
vsmResetTeleStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vsmResetTeleStats.setStatus("mandatory")
_VsmDspVPStatsTable_Object = MibTable
vsmDspVPStatsTable = _VsmDspVPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 3)
)
if mibBuilder.loadTexts:
    vsmDspVPStatsTable.setStatus("mandatory")
_VsmDspVPStatsEntry_Object = MibTableRow
vsmDspVPStatsEntry = _VsmDspVPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 3, 1)
)
vsmDspVPStatsEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmDspVPStatsEntry.setStatus("mandatory")
_VsmDspAvgPlayoutDelay_Type = Integer32
_VsmDspAvgPlayoutDelay_Object = MibTableColumn
vsmDspAvgPlayoutDelay = _VsmDspAvgPlayoutDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 3, 1, 1),
    _VsmDspAvgPlayoutDelay_Type()
)
vsmDspAvgPlayoutDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspAvgPlayoutDelay.setStatus("mandatory")
_VsmDspLostPackets_Type = Integer32
_VsmDspLostPackets_Object = MibTableColumn
vsmDspLostPackets = _VsmDspLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 3, 1, 2),
    _VsmDspLostPackets_Type()
)
vsmDspLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspLostPackets.setStatus("mandatory")
_VsmDspReplayPackets_Type = Integer32
_VsmDspReplayPackets_Object = MibTableColumn
vsmDspReplayPackets = _VsmDspReplayPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 3, 1, 3),
    _VsmDspReplayPackets_Type()
)
vsmDspReplayPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspReplayPackets.setStatus("mandatory")
_VsmDspIdlePackets_Type = Integer32
_VsmDspIdlePackets_Object = MibTableColumn
vsmDspIdlePackets = _VsmDspIdlePackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 3, 1, 4),
    _VsmDspIdlePackets_Type()
)
vsmDspIdlePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspIdlePackets.setStatus("mandatory")
_VsmDspDroppedPackets_Type = Integer32
_VsmDspDroppedPackets_Object = MibTableColumn
vsmDspDroppedPackets = _VsmDspDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 3, 1, 5),
    _VsmDspDroppedPackets_Type()
)
vsmDspDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspDroppedPackets.setStatus("mandatory")
_VsmDspReceivedPackets_Type = Integer32
_VsmDspReceivedPackets_Object = MibTableColumn
vsmDspReceivedPackets = _VsmDspReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 3, 1, 6),
    _VsmDspReceivedPackets_Type()
)
vsmDspReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspReceivedPackets.setStatus("mandatory")
_VsmDspRxAvgFrameJitter_Type = Integer32
_VsmDspRxAvgFrameJitter_Object = MibTableColumn
vsmDspRxAvgFrameJitter = _VsmDspRxAvgFrameJitter_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 3, 1, 7),
    _VsmDspRxAvgFrameJitter_Type()
)
vsmDspRxAvgFrameJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspRxAvgFrameJitter.setStatus("mandatory")
_VsmResetDspPlayOutStats_Type = Integer32
_VsmResetDspPlayOutStats_Object = MibTableColumn
vsmResetDspPlayOutStats = _VsmResetDspPlayOutStats_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 3, 1, 8),
    _VsmResetDspPlayOutStats_Type()
)
vsmResetDspPlayOutStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vsmResetDspPlayOutStats.setStatus("mandatory")
_VsmDspRxTxStatsTable_Object = MibTable
vsmDspRxTxStatsTable = _VsmDspRxTxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4)
)
if mibBuilder.loadTexts:
    vsmDspRxTxStatsTable.setStatus("mandatory")
_VsmDspRxTxStatsEntry_Object = MibTableRow
vsmDspRxTxStatsEntry = _VsmDspRxTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1)
)
vsmDspRxTxStatsEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmDspRxTxStatsEntry.setStatus("mandatory")
_VsmDspRxPackets_Type = Integer32
_VsmDspRxPackets_Object = MibTableColumn
vsmDspRxPackets = _VsmDspRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1, 1),
    _VsmDspRxPackets_Type()
)
vsmDspRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspRxPackets.setStatus("mandatory")
_VsmDspTxPackets_Type = Integer32
_VsmDspTxPackets_Object = MibTableColumn
vsmDspTxPackets = _VsmDspTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1, 2),
    _VsmDspTxPackets_Type()
)
vsmDspTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspTxPackets.setStatus("mandatory")
_VsmDspSilencePackets_Type = Integer32
_VsmDspSilencePackets_Object = MibTableColumn
vsmDspSilencePackets = _VsmDspSilencePackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1, 3),
    _VsmDspSilencePackets_Type()
)
vsmDspSilencePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspSilencePackets.setStatus("mandatory")
_VsmDspRxMinJitter_Type = Integer32
_VsmDspRxMinJitter_Object = MibTableColumn
vsmDspRxMinJitter = _VsmDspRxMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1, 4),
    _VsmDspRxMinJitter_Type()
)
vsmDspRxMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspRxMinJitter.setStatus("mandatory")
_VsmDspRxMaxJitter_Type = Integer32
_VsmDspRxMaxJitter_Object = MibTableColumn
vsmDspRxMaxJitter = _VsmDspRxMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1, 5),
    _VsmDspRxMaxJitter_Type()
)
vsmDspRxMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspRxMaxJitter.setStatus("mandatory")
_VsmDspRxAvgJitter_Type = Integer32
_VsmDspRxAvgJitter_Object = MibTableColumn
vsmDspRxAvgJitter = _VsmDspRxAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1, 6),
    _VsmDspRxAvgJitter_Type()
)
vsmDspRxAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspRxAvgJitter.setStatus("mandatory")
_VsmTxDroppedFrames_Type = Integer32
_VsmTxDroppedFrames_Object = MibTableColumn
vsmTxDroppedFrames = _VsmTxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1, 7),
    _VsmTxDroppedFrames_Type()
)
vsmTxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTxDroppedFrames.setStatus("mandatory")
_VsmTxOctets_Type = Integer32
_VsmTxOctets_Object = MibTableColumn
vsmTxOctets = _VsmTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1, 8),
    _VsmTxOctets_Type()
)
vsmTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmTxOctets.setStatus("mandatory")
_VsmRxOctets_Type = Integer32
_VsmRxOctets_Object = MibTableColumn
vsmRxOctets = _VsmRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1, 9),
    _VsmRxOctets_Type()
)
vsmRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmRxOctets.setStatus("mandatory")
_VsmAal2CodPrfChgs_Type = Integer32
_VsmAal2CodPrfChgs_Object = MibTableColumn
vsmAal2CodPrfChgs = _VsmAal2CodPrfChgs_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1, 10),
    _VsmAal2CodPrfChgs_Type()
)
vsmAal2CodPrfChgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmAal2CodPrfChgs.setStatus("mandatory")
_VsmDtmfTxOctets_Type = Integer32
_VsmDtmfTxOctets_Object = MibTableColumn
vsmDtmfTxOctets = _VsmDtmfTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1, 11),
    _VsmDtmfTxOctets_Type()
)
vsmDtmfTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDtmfTxOctets.setStatus("mandatory")
_VsmDtmfRxOctets_Type = Integer32
_VsmDtmfRxOctets_Object = MibTableColumn
vsmDtmfRxOctets = _VsmDtmfRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1, 12),
    _VsmDtmfRxOctets_Type()
)
vsmDtmfRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDtmfRxOctets.setStatus("mandatory")
_VsmResetDspRxTxStats_Type = Integer32
_VsmResetDspRxTxStats_Object = MibTableColumn
vsmResetDspRxTxStats = _VsmResetDspRxTxStats_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 4, 1, 13),
    _VsmResetDspRxTxStats_Type()
)
vsmResetDspRxTxStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vsmResetDspRxTxStats.setStatus("mandatory")
_VsmDspVoiceErrorStatsTable_Object = MibTable
vsmDspVoiceErrorStatsTable = _VsmDspVoiceErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 5)
)
if mibBuilder.loadTexts:
    vsmDspVoiceErrorStatsTable.setStatus("mandatory")
_VsmDspVoiceErrorStatsEntry_Object = MibTableRow
vsmDspVoiceErrorStatsEntry = _VsmDspVoiceErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 5, 1)
)
vsmDspVoiceErrorStatsEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmDspVoiceErrorStatsEntry.setStatus("mandatory")
_VsmDspInvalidHeaderCount_Type = Integer32
_VsmDspInvalidHeaderCount_Object = MibTableColumn
vsmDspInvalidHeaderCount = _VsmDspInvalidHeaderCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 5, 1, 1),
    _VsmDspInvalidHeaderCount_Type()
)
vsmDspInvalidHeaderCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspInvalidHeaderCount.setStatus("mandatory")
_VsmDspMicroOverflowCount_Type = Integer32
_VsmDspMicroOverflowCount_Object = MibTableColumn
vsmDspMicroOverflowCount = _VsmDspMicroOverflowCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 5, 1, 2),
    _VsmDspMicroOverflowCount_Type()
)
vsmDspMicroOverflowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspMicroOverflowCount.setStatus("mandatory")
_VsmDspLostEnhPackets_Type = Integer32
_VsmDspLostEnhPackets_Object = MibTableColumn
vsmDspLostEnhPackets = _VsmDspLostEnhPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 5, 1, 3),
    _VsmDspLostEnhPackets_Type()
)
vsmDspLostEnhPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspLostEnhPackets.setStatus("mandatory")
_VsmDspMissingCorePackets_Type = Integer32
_VsmDspMissingCorePackets_Object = MibTableColumn
vsmDspMissingCorePackets = _VsmDspMissingCorePackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 5, 1, 4),
    _VsmDspMissingCorePackets_Type()
)
vsmDspMissingCorePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspMissingCorePackets.setStatus("mandatory")
_VsmDspPktsLostByNetwork_Type = Integer32
_VsmDspPktsLostByNetwork_Object = MibTableColumn
vsmDspPktsLostByNetwork = _VsmDspPktsLostByNetwork_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 5, 1, 5),
    _VsmDspPktsLostByNetwork_Type()
)
vsmDspPktsLostByNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspPktsLostByNetwork.setStatus("mandatory")
_VsmResetDspErrorStats_Type = Integer32
_VsmResetDspErrorStats_Object = MibTableColumn
vsmResetDspErrorStats = _VsmResetDspErrorStats_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 5, 1, 6),
    _VsmResetDspErrorStats_Type()
)
vsmResetDspErrorStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vsmResetDspErrorStats.setStatus("mandatory")
_VsmDspModemStatsTable_Object = MibTable
vsmDspModemStatsTable = _VsmDspModemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 6)
)
if mibBuilder.loadTexts:
    vsmDspModemStatsTable.setStatus("mandatory")
_VsmDspModemStatsEntry_Object = MibTableRow
vsmDspModemStatsEntry = _VsmDspModemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 6, 1)
)
vsmDspModemStatsEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmDspModemStatsEntry.setStatus("mandatory")
_VsmDspModemStatus_Type = Integer32
_VsmDspModemStatus_Object = MibTableColumn
vsmDspModemStatus = _VsmDspModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 6, 1, 1),
    _VsmDspModemStatus_Type()
)
vsmDspModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspModemStatus.setStatus("mandatory")
_VsmDspModemRxLevel_Type = Integer32
_VsmDspModemRxLevel_Object = MibTableColumn
vsmDspModemRxLevel = _VsmDspModemRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 6, 1, 2),
    _VsmDspModemRxLevel_Type()
)
vsmDspModemRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspModemRxLevel.setStatus("mandatory")
_VsmDspModemRxRate_Type = Integer32
_VsmDspModemRxRate_Object = MibTableColumn
vsmDspModemRxRate = _VsmDspModemRxRate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 6, 1, 3),
    _VsmDspModemRxRate_Type()
)
vsmDspModemRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspModemRxRate.setStatus("mandatory")
_VsmDspModemTxLevel_Type = Integer32
_VsmDspModemTxLevel_Object = MibTableColumn
vsmDspModemTxLevel = _VsmDspModemTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 6, 1, 4),
    _VsmDspModemTxLevel_Type()
)
vsmDspModemTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspModemTxLevel.setStatus("mandatory")
_VsmDspModemTxRate_Type = Integer32
_VsmDspModemTxRate_Object = MibTableColumn
vsmDspModemTxRate = _VsmDspModemTxRate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 6, 1, 5),
    _VsmDspModemTxRate_Type()
)
vsmDspModemTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspModemTxRate.setStatus("mandatory")
_VsmDspModemCarrFreqOffset_Type = Integer32
_VsmDspModemCarrFreqOffset_Object = MibTableColumn
vsmDspModemCarrFreqOffset = _VsmDspModemCarrFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 6, 1, 6),
    _VsmDspModemCarrFreqOffset_Type()
)
vsmDspModemCarrFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspModemCarrFreqOffset.setStatus("mandatory")
_VsmDspModemTimeFreqOffset_Type = Integer32
_VsmDspModemTimeFreqOffset_Object = MibTableColumn
vsmDspModemTimeFreqOffset = _VsmDspModemTimeFreqOffset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 6, 1, 7),
    _VsmDspModemTimeFreqOffset_Type()
)
vsmDspModemTimeFreqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspModemTimeFreqOffset.setStatus("mandatory")
_VsmResetDspModemStats_Type = Integer32
_VsmResetDspModemStats_Object = MibTableColumn
vsmResetDspModemStats = _VsmResetDspModemStats_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 6, 1, 8),
    _VsmResetDspModemStats_Type()
)
vsmResetDspModemStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vsmResetDspModemStats.setStatus("mandatory")
_VsmDspFaxStatsTable_Object = MibTable
vsmDspFaxStatsTable = _VsmDspFaxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 7)
)
if mibBuilder.loadTexts:
    vsmDspFaxStatsTable.setStatus("mandatory")
_VsmDspFaxStatsEntry_Object = MibTableRow
vsmDspFaxStatsEntry = _VsmDspFaxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 7, 1)
)
vsmDspFaxStatsEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmDspFaxStatsEntry.setStatus("mandatory")
_VsmDspFaxTxPackets_Type = Integer32
_VsmDspFaxTxPackets_Object = MibTableColumn
vsmDspFaxTxPackets = _VsmDspFaxTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 7, 1, 1),
    _VsmDspFaxTxPackets_Type()
)
vsmDspFaxTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspFaxTxPackets.setStatus("mandatory")
_VsmDspFaxRxPackets_Type = Integer32
_VsmDspFaxRxPackets_Object = MibTableColumn
vsmDspFaxRxPackets = _VsmDspFaxRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 7, 1, 2),
    _VsmDspFaxRxPackets_Type()
)
vsmDspFaxRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspFaxRxPackets.setStatus("mandatory")
_VsmDspFaxLostPackets_Type = Integer32
_VsmDspFaxLostPackets_Object = MibTableColumn
vsmDspFaxLostPackets = _VsmDspFaxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 7, 1, 3),
    _VsmDspFaxLostPackets_Type()
)
vsmDspFaxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspFaxLostPackets.setStatus("mandatory")
_VsmDspFaxDroppedPackets_Type = Integer32
_VsmDspFaxDroppedPackets_Object = MibTableColumn
vsmDspFaxDroppedPackets = _VsmDspFaxDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 7, 1, 4),
    _VsmDspFaxDroppedPackets_Type()
)
vsmDspFaxDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspFaxDroppedPackets.setStatus("mandatory")
_VsmDspFaxRxOutOfSeqPkts_Type = Integer32
_VsmDspFaxRxOutOfSeqPkts_Object = MibTableColumn
vsmDspFaxRxOutOfSeqPkts = _VsmDspFaxRxOutOfSeqPkts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 7, 1, 5),
    _VsmDspFaxRxOutOfSeqPkts_Type()
)
vsmDspFaxRxOutOfSeqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmDspFaxRxOutOfSeqPkts.setStatus("mandatory")
_VsmResetDspFaxStats_Type = Integer32
_VsmResetDspFaxStats_Object = MibTableColumn
vsmResetDspFaxStats = _VsmResetDspFaxStats_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 7, 1, 6),
    _VsmResetDspFaxStats_Type()
)
vsmResetDspFaxStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vsmResetDspFaxStats.setStatus("mandatory")
_VsmISDNTeleStatsTable_Object = MibTable
vsmISDNTeleStatsTable = _VsmISDNTeleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 9)
)
if mibBuilder.loadTexts:
    vsmISDNTeleStatsTable.setStatus("mandatory")
_VsmISDNTeleStatsEntry_Object = MibTableRow
vsmISDNTeleStatsEntry = _VsmISDNTeleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 9, 1)
)
vsmISDNTeleStatsEntry.setIndexNames(
    (0, "XYLAN-VSM-MIB", "vsmChanSlotIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanPortIndex"),
    (0, "XYLAN-VSM-MIB", "vsmChanIndex"),
)
if mibBuilder.loadTexts:
    vsmISDNTeleStatsEntry.setStatus("mandatory")
_VsmNbCalls_Type = Integer32
_VsmNbCalls_Object = MibTableColumn
vsmNbCalls = _VsmNbCalls_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 9, 1, 1),
    _VsmNbCalls_Type()
)
vsmNbCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmNbCalls.setStatus("mandatory")
_VsmNbLocalSetup_Type = Integer32
_VsmNbLocalSetup_Object = MibTableColumn
vsmNbLocalSetup = _VsmNbLocalSetup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 9, 1, 2),
    _VsmNbLocalSetup_Type()
)
vsmNbLocalSetup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmNbLocalSetup.setStatus("mandatory")
_VsmNbRemoteSetup_Type = Integer32
_VsmNbRemoteSetup_Object = MibTableColumn
vsmNbRemoteSetup = _VsmNbRemoteSetup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 9, 1, 3),
    _VsmNbRemoteSetup_Type()
)
vsmNbRemoteSetup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmNbRemoteSetup.setStatus("mandatory")
_VsmNbDropCalls_Type = Integer32
_VsmNbDropCalls_Object = MibTableColumn
vsmNbDropCalls = _VsmNbDropCalls_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 9, 1, 4),
    _VsmNbDropCalls_Type()
)
vsmNbDropCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmNbDropCalls.setStatus("mandatory")
_VsmNbFaxSwitch_Type = Integer32
_VsmNbFaxSwitch_Object = MibTableColumn
vsmNbFaxSwitch = _VsmNbFaxSwitch_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 9, 1, 5),
    _VsmNbFaxSwitch_Type()
)
vsmNbFaxSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmNbFaxSwitch.setStatus("mandatory")
_VsmNbModemSwitch_Type = Integer32
_VsmNbModemSwitch_Object = MibTableColumn
vsmNbModemSwitch = _VsmNbModemSwitch_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 9, 1, 6),
    _VsmNbModemSwitch_Type()
)
vsmNbModemSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsmNbModemSwitch.setStatus("mandatory")
_VsmResetISDNTeleStats_Type = Integer32
_VsmResetISDNTeleStats_Object = MibTableColumn
vsmResetISDNTeleStats = _VsmResetISDNTeleStats_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 26, 7, 9, 1, 7),
    _VsmResetISDNTeleStats_Type()
)
vsmResetISDNTeleStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vsmResetISDNTeleStats.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-VSM-MIB",
    **{"RowStatus": RowStatus,
       "VsmEnableDisabled": VsmEnableDisabled,
       "VsmOnOff": VsmOnOff,
       "VsmVoiceCodingType": VsmVoiceCodingType,
       "vsmNetworkGroup": vsmNetworkGroup,
       "vsmVNTemplateTable": vsmVNTemplateTable,
       "vsmVNTemplateEntry": vsmVNTemplateEntry,
       "vsmVNTmplIndex": vsmVNTmplIndex,
       "vsmVNTmplName": vsmVNTmplName,
       "vsmVNTmplRowStatus": vsmVNTmplRowStatus,
       "vsmVNTmplH323GateKeeperPhoneGroupTable": vsmVNTmplH323GateKeeperPhoneGroupTable,
       "vsmVNTmplH323GateKeeperPhoneGroupEntry": vsmVNTmplH323GateKeeperPhoneGroupEntry,
       "vsmVNTmplH323GateKeeperPhoneGroupRowStatus": vsmVNTmplH323GateKeeperPhoneGroupRowStatus,
       "vsmVNCardTable": vsmVNCardTable,
       "vsmVNCardEntry": vsmVNCardEntry,
       "vsmVNCardH323DisplayName": vsmVNCardH323DisplayName,
       "vsmVNCardRTPPortMode": vsmVNCardRTPPortMode,
       "vsmVNCardRTPPortBase": vsmVNCardRTPPortBase,
       "vsmVNCardH323OutFastStart": vsmVNCardH323OutFastStart,
       "vsmVNCardH323InFastStart": vsmVNCardH323InFastStart,
       "vsmVNCardH323GatekeeperCtrl": vsmVNCardH323GatekeeperCtrl,
       "vsmVNCardH323GatekeeperMode": vsmVNCardH323GatekeeperMode,
       "vsmVNCardH323GatekeeperAddr": vsmVNCardH323GatekeeperAddr,
       "vsmVNCardH323AllowCallsWithoutGatekeeper": vsmVNCardH323AllowCallsWithoutGatekeeper,
       "vsmVNCardH323GatekeeperMaxRetries": vsmVNCardH323GatekeeperMaxRetries,
       "vsmVNCardH323EndpointRegType": vsmVNCardH323EndpointRegType,
       "vsmVNCardH323Notification": vsmVNCardH323Notification,
       "vsmVNCardH323GateKeeperPhoneGroupTable": vsmVNCardH323GateKeeperPhoneGroupTable,
       "vsmVNCardH323GateKeeperPhoneGroupEntry": vsmVNCardH323GateKeeperPhoneGroupEntry,
       "vsmVNCardH323GateKeeperPhoneGroupRowStatus": vsmVNCardH323GateKeeperPhoneGroupRowStatus,
       "vsmSignalingGroup": vsmSignalingGroup,
       "vsmSignalingTemplateTable": vsmSignalingTemplateTable,
       "vsmSignalingTemplateEntry": vsmSignalingTemplateEntry,
       "vsmSigTmplIndex": vsmSigTmplIndex,
       "vsmSigTmplName": vsmSigTmplName,
       "vsmSigTmplRowStatus": vsmSigTmplRowStatus,
       "vsmSigTmplEmCommonTable": vsmSigTmplEmCommonTable,
       "vsmSigTmplEmCommonEntry": vsmSigTmplEmCommonEntry,
       "vsmSigTmplEmCommonOffHookDebounce": vsmSigTmplEmCommonOffHookDebounce,
       "vsmSigTmplEmDelayTable": vsmSigTmplEmDelayTable,
       "vsmSigTmplEmDelayEntry": vsmSigTmplEmDelayEntry,
       "vsmSigTmplEmDelayInDelayDurMin": vsmSigTmplEmDelayInDelayDurMin,
       "vsmSigTmplEmImmedTable": vsmSigTmplEmImmedTable,
       "vsmSigTmplEmImmedEntry": vsmSigTmplEmImmedEntry,
       "vsmSigTmplEmImmedGlareReport": vsmSigTmplEmImmedGlareReport,
       "vsmSigTmplEmWinkTable": vsmSigTmplEmWinkTable,
       "vsmSigTmplEmWinkEntry": vsmSigTmplEmWinkEntry,
       "vsmSigTmplEmWinkInWinkWaitMin": vsmSigTmplEmWinkInWinkWaitMin,
       "vsmSigTmplFxoGSTable": vsmSigTmplFxoGSTable,
       "vsmSigTmplFxoGSEntry": vsmSigTmplFxoGSEntry,
       "vsmSigTmplFxoGSConnectionLoopOpenDebounce": vsmSigTmplFxoGSConnectionLoopOpenDebounce,
       "vsmSigTmplFxoLSTable": vsmSigTmplFxoLSTable,
       "vsmSigTmplFxoLSEntry": vsmSigTmplFxoLSEntry,
       "vsmSigTmplFxoLSRingingDebounce": vsmSigTmplFxoLSRingingDebounce,
       "vsmSigTmplFxsGSTable": vsmSigTmplFxsGSTable,
       "vsmSigTmplFxsGSEntry": vsmSigTmplFxsGSEntry,
       "vsmSigTmplFxsGSSeizeDetect": vsmSigTmplFxsGSSeizeDetect,
       "vsmSigTmplFxsLSTable": vsmSigTmplFxsLSTable,
       "vsmSigTmplFxsLSEntry": vsmSigTmplFxsLSEntry,
       "vsmSigTmplFxsLSOffHookDebounce": vsmSigTmplFxsLSOffHookDebounce,
       "vsmSignalingChannelTable": vsmSignalingChannelTable,
       "vsmSignalingChannelEntry": vsmSignalingChannelEntry,
       "vsmSigChanProtocol": vsmSigChanProtocol,
       "vsmSigChanCallerIdName": vsmSigChanCallerIdName,
       "vsmSigChanCallerIdNameStr": vsmSigChanCallerIdNameStr,
       "vsmSigChanCallerIdNumber": vsmSigChanCallerIdNumber,
       "vsmSigChanCallerIdNumberStr": vsmSigChanCallerIdNumberStr,
       "vsmSigChanToneTable": vsmSigChanToneTable,
       "vsmSigChanOutWait": vsmSigChanOutWait,
       "vsmSigChanOutToneDigitDur": vsmSigChanOutToneDigitDur,
       "vsmSigChanOutToneInterDigitDur": vsmSigChanOutToneInterDigitDur,
       "vsmSigChanUnused": vsmSigChanUnused,
       "vsmSigChanCallLimitCtrl": vsmSigChanCallLimitCtrl,
       "vsmSigChanCallLimit": vsmSigChanCallLimit,
       "vsmSigChanAnswerWaitLimitCtrl": vsmSigChanAnswerWaitLimitCtrl,
       "vsmSigChanAnswerWaitLimit": vsmSigChanAnswerWaitLimit,
       "vsmSigChanHangupWaitLimitCtrl": vsmSigChanHangupWaitLimitCtrl,
       "vsmSigChanHangupWaitLimit": vsmSigChanHangupWaitLimit,
       "vsmSigChanFaxHoldoverDelay": vsmSigChanFaxHoldoverDelay,
       "vsmSigChanCompanding": vsmSigChanCompanding,
       "vsmSigChanReceiveGain": vsmSigChanReceiveGain,
       "vsmSigChanTransmitGain": vsmSigChanTransmitGain,
       "vsmSigChanIdleNoise": vsmSigChanIdleNoise,
       "vsmSigChanOverrideInBandCallProgressTones": vsmSigChanOverrideInBandCallProgressTones,
       "vsmSigChanOverrideInBandCodecSwitching": vsmSigChanOverrideInBandCodecSwitching,
       "vsmSigChanOverridePSUCodecSwitching": vsmSigChanOverridePSUCodecSwitching,
       "vsmSigChanOverrideNetworkOverlapDialing": vsmSigChanOverrideNetworkOverlapDialing,
       "vsmSigChanOverrideFullCallProgressTones": vsmSigChanOverrideFullCallProgressTones,
       "vsmSigChanOverrideRingBack": vsmSigChanOverrideRingBack,
       "vsmSigChanOverrideInfoElementTransport": vsmSigChanOverrideInfoElementTransport,
       "vsmSigChanOverrideQSIGInfoElementTransport": vsmSigChanOverrideQSIGInfoElementTransport,
       "vsmSigChanOverrideDataSetup": vsmSigChanOverrideDataSetup,
       "vsmSigChanOverrideVoiceSetup": vsmSigChanOverrideVoiceSetup,
       "vsmSigChanOverrideFAXSetup": vsmSigChanOverrideFAXSetup,
       "vsmSigChanOverrideModemSetup": vsmSigChanOverrideModemSetup,
       "vsmSigChanCallProgressToneDetControl": vsmSigChanCallProgressToneDetControl,
       "vsmSigChanCallProgressToneDetCfg": vsmSigChanCallProgressToneDetCfg,
       "vsmSigChanAssignTmplName": vsmSigChanAssignTmplName,
       "vsmSigChanAssignTmplStatus": vsmSigChanAssignTmplStatus,
       "vsmSigChanOutDialType": vsmSigChanOutDialType,
       "vsmSigChanV18ToneDetThHangTime": vsmSigChanV18ToneDetThHangTime,
       "vsmSigChanV18ToneDetThLevel": vsmSigChanV18ToneDetThLevel,
       "vsmSigChanV18ToneDetThFraction": vsmSigChanV18ToneDetThFraction,
       "vsmSigChanSinFreqToneDetThLev": vsmSigChanSinFreqToneDetThLev,
       "vsmSigChanSinFreqToneDetThTime": vsmSigChanSinFreqToneDetThTime,
       "vsmSigChanEchoCancelNonSens": vsmSigChanEchoCancelNonSens,
       "vsmSigChanAcousticEchoCancellerMode": vsmSigChanAcousticEchoCancellerMode,
       "vsmSigChanAcouEchoCanNonProc": vsmSigChanAcouEchoCanNonProc,
       "vsmSigChanAcEchoCanSetSpGain": vsmSigChanAcEchoCanSetSpGain,
       "vsmSigChanAcEchoCanFreeSpGain": vsmSigChanAcEchoCanFreeSpGain,
       "vsmSigChanAcousticEchoCanOper": vsmSigChanAcousticEchoCanOper,
       "vsmSigChanFxsLSCadenceCoefficient": vsmSigChanFxsLSCadenceCoefficient,
       "vsmSigChanFxsLSRingId": vsmSigChanFxsLSRingId,
       "vsmSigChanFxsGSCadenceCoefficient": vsmSigChanFxsGSCadenceCoefficient,
       "vsmSigChanFxsGSRingId": vsmSigChanFxsGSRingId,
       "vsmSigChanEmCommonTable": vsmSigChanEmCommonTable,
       "vsmSigChanEmCommonEntry": vsmSigChanEmCommonEntry,
       "vsmSigChanEmCommonOffHookDebounce": vsmSigChanEmCommonOffHookDebounce,
       "vsmSigChanEmCommonOnHookDebounce": vsmSigChanEmCommonOnHookDebounce,
       "vsmSigChanEmCommonSeizeDetect": vsmSigChanEmCommonSeizeDetect,
       "vsmSigChanEmCommonClearDetect": vsmSigChanEmCommonClearDetect,
       "vsmSigChanEmCommonClearConfDetect": vsmSigChanEmCommonClearConfDetect,
       "vsmSigChanEmCommonClearConfWaitMax": vsmSigChanEmCommonClearConfWaitMax,
       "vsmSigChanEmCommonGuardAll": vsmSigChanEmCommonGuardAll,
       "vsmSigChanEmCommonGuardOut": vsmSigChanEmCommonGuardOut,
       "vsmSigChanEmCommonDialTone": vsmSigChanEmCommonDialTone,
       "vsmSigChanEmCommonMinConnectTime": vsmSigChanEmCommonMinConnectTime,
       "vsmSigChanEmCommonHangUpWait": vsmSigChanEmCommonHangUpWait,
       "vsmSigChanEmDelayTable": vsmSigChanEmDelayTable,
       "vsmSigChanEmDelayEntry": vsmSigChanEmDelayEntry,
       "vsmSigChanEmDelayInDelayDurMin": vsmSigChanEmDelayInDelayDurMin,
       "vsmSigChanEmDelayInDelayDurMax": vsmSigChanEmDelayInDelayDurMax,
       "vsmSigChanEmDelayInDigitIgnore": vsmSigChanEmDelayInDigitIgnore,
       "vsmSigChanEmDelayOutDelayDurMin": vsmSigChanEmDelayOutDelayDurMin,
       "vsmSigChanEmDelayOutDelayDurMax": vsmSigChanEmDelayOutDelayDurMax,
       "vsmSigChanEmDelayOutIntegrityChk": vsmSigChanEmDelayOutIntegrityChk,
       "vsmSigChanEmDelayOutDelayChk": vsmSigChanEmDelayOutDelayChk,
       "vsmSigChanEmImmedTable": vsmSigChanEmImmedTable,
       "vsmSigChanEmImmedEntry": vsmSigChanEmImmedEntry,
       "vsmSigChanEmImmedGlareReport": vsmSigChanEmImmedGlareReport,
       "vsmSigChanEmImmedDigitWait": vsmSigChanEmImmedDigitWait,
       "vsmSigChanEmWinkTable": vsmSigChanEmWinkTable,
       "vsmSigChanEmWinkEntry": vsmSigChanEmWinkEntry,
       "vsmSigChanEmWinkInWinkWaitMin": vsmSigChanEmWinkInWinkWaitMin,
       "vsmSigChanEmWinkInWinkWaitMax": vsmSigChanEmWinkInWinkWaitMax,
       "vsmSigChanEmWinkInWinkDur": vsmSigChanEmWinkInWinkDur,
       "vsmSigChanEmWinkInDigitIgnore": vsmSigChanEmWinkInDigitIgnore,
       "vsmSigChanEmWinkOutWinkWaitMax": vsmSigChanEmWinkOutWinkWaitMax,
       "vsmSigChanEmWinkOutWinkDurMin": vsmSigChanEmWinkOutWinkDurMin,
       "vsmSigChanEmWinkOutWinkDurMax": vsmSigChanEmWinkOutWinkDurMax,
       "vsmSigChanFxoGSTable": vsmSigChanFxoGSTable,
       "vsmSigChanFxoGSEntry": vsmSigChanFxoGSEntry,
       "vsmSigChanFxoGSConnectionLoopOpenDebounce": vsmSigChanFxoGSConnectionLoopOpenDebounce,
       "vsmSigChanFxoGSMaxTipGroundWait": vsmSigChanFxoGSMaxTipGroundWait,
       "vsmSigChanFxoGSTipGroundDebounce": vsmSigChanFxoGSTipGroundDebounce,
       "vsmSigChanFxoGSRingingDebounce": vsmSigChanFxoGSRingingDebounce,
       "vsmSigChanFxoGSRingingInterCycle": vsmSigChanFxoGSRingingInterCycle,
       "vsmSigChanFxoGSRingingInterPulse": vsmSigChanFxoGSRingingInterPulse,
       "vsmSigChanFxoGSCallerIdDetect": vsmSigChanFxoGSCallerIdDetect,
       "vsmSigChanFxoGSAnswerAfterRings": vsmSigChanFxoGSAnswerAfterRings,
       "vsmSigChanFxoGSLoopCurrentDebounce": vsmSigChanFxoGSLoopCurrentDebounce,
       "vsmSigChanFxoGSBattReversalDebounce": vsmSigChanFxoGSBattReversalDebounce,
       "vsmSigChanFxoLSTable": vsmSigChanFxoLSTable,
       "vsmSigChanFxoLSEntry": vsmSigChanFxoLSEntry,
       "vsmSigChanFxoLSRingingDebounce": vsmSigChanFxoLSRingingDebounce,
       "vsmSigChanFxoLSCPCDetectCtrl": vsmSigChanFxoLSCPCDetectCtrl,
       "vsmSigChanFxoLSCPCDetectDur": vsmSigChanFxoLSCPCDetectDur,
       "vsmSigChanFxoLSGuardOut": vsmSigChanFxoLSGuardOut,
       "vsmSigChanFxoLSRingingInterCycle": vsmSigChanFxoLSRingingInterCycle,
       "vsmSigChanFxoLSRingingInterPulse": vsmSigChanFxoLSRingingInterPulse,
       "vsmSigChanFxoLSCallerIdDetect": vsmSigChanFxoLSCallerIdDetect,
       "vsmSigChanFxoLSAnswerAfterRings": vsmSigChanFxoLSAnswerAfterRings,
       "vsmSigChanFxoLSLoopCurrentDebounce": vsmSigChanFxoLSLoopCurrentDebounce,
       "vsmSigChanFxoLSBattReversalDebounce": vsmSigChanFxoLSBattReversalDebounce,
       "vsmSigChanFxsGSTable": vsmSigChanFxsGSTable,
       "vsmSigChanFxsGSEntry": vsmSigChanFxsGSEntry,
       "vsmSigChanFxsGSSeizeDetect": vsmSigChanFxsGSSeizeDetect,
       "vsmSigChanFxsGSOnHookDebounce": vsmSigChanFxsGSOnHookDebounce,
       "vsmSigChanFxsGSOrigClearDetect": vsmSigChanFxsGSOrigClearDetect,
       "vsmSigChanFxsGSAnswClearDetect": vsmSigChanFxsGSAnswClearDetect,
       "vsmSigChanFxsGSMinRingGround": vsmSigChanFxsGSMinRingGround,
       "vsmSigChanFxsGSMaxWaitLoop": vsmSigChanFxsGSMaxWaitLoop,
       "vsmSigChanFxsGSMinLoopOpen": vsmSigChanFxsGSMinLoopOpen,
       "vsmSigChanFxsGSGenerateCallerId": vsmSigChanFxsGSGenerateCallerId,
       "vsmSigChanFxsGSOffHookDebounce": vsmSigChanFxsGSOffHookDebounce,
       "vsmSigChanFxsGSRingGroundDebounce": vsmSigChanFxsGSRingGroundDebounce,
       "vsmSigChanFxsLSTable": vsmSigChanFxsLSTable,
       "vsmSigChanFxsLSEntry": vsmSigChanFxsLSEntry,
       "vsmSigChanFxsLSOffHookDebounce": vsmSigChanFxsLSOffHookDebounce,
       "vsmSigChanFxsLSOnHookDebounce": vsmSigChanFxsLSOnHookDebounce,
       "vsmSigChanFxsLSSeizeDetect": vsmSigChanFxsLSSeizeDetect,
       "vsmSigChanFxsLSOrigClearDetect": vsmSigChanFxsLSOrigClearDetect,
       "vsmSigChanFxsLSAnswClearDetect": vsmSigChanFxsLSAnswClearDetect,
       "vsmSigChanFxsLSCPCWait": vsmSigChanFxsLSCPCWait,
       "vsmSigChanFxsLSCPCDur": vsmSigChanFxsLSCPCDur,
       "vsmSigChanFxsLSGenerateCallerId": vsmSigChanFxsLSGenerateCallerId,
       "vsmCodingProfileGroup": vsmCodingProfileGroup,
       "vsmCodingProfileTable": vsmCodingProfileTable,
       "vsmCodingProfEntry": vsmCodingProfEntry,
       "vsmCodingProfId": vsmCodingProfId,
       "vsmCodingProfName": vsmCodingProfName,
       "vsmCodingProfCallerId": vsmCodingProfCallerId,
       "vsmCodingProfCodingType": vsmCodingProfCodingType,
       "vsmCodingProfPktInterval": vsmCodingProfPktInterval,
       "vsmCodingProfVIF": vsmCodingProfVIF,
       "vsmCodingProfNetBufMode": vsmCodingProfNetBufMode,
       "vsmCodingProfNetBufNomDelay": vsmCodingProfNetBufNomDelay,
       "vsmCodingProfNetBufMaxDelay": vsmCodingProfNetBufMaxDelay,
       "vsmCodingProfDtmfRelay": vsmCodingProfDtmfRelay,
       "vsmCodingProfVAD": vsmCodingProfVAD,
       "vsmCodingProfEC": vsmCodingProfEC,
       "vsmCodingProfSwitchover": vsmCodingProfSwitchover,
       "vsmCodingProfCallProgToneDet": vsmCodingProfCallProgToneDet,
       "vsmCodingProfV18ToneDet": vsmCodingProfV18ToneDet,
       "vsmCodingProfVADThreshMode": vsmCodingProfVADThreshMode,
       "vsmCodingProfVADThreshLevel": vsmCodingProfVADThreshLevel,
       "vsmCodingProfVEchoCanComfNoiseMode": vsmCodingProfVEchoCanComfNoiseMode,
       "vsmCodingProfEchoCanRefreshCfg": vsmCodingProfEchoCanRefreshCfg,
       "vsmCodingProfEchoCanRefreshState": vsmCodingProfEchoCanRefreshState,
       "vsmCodingProfECTailDelay": vsmCodingProfECTailDelay,
       "vsmCodingProfECNonLinear": vsmCodingProfECNonLinear,
       "vsmCodingProfFaxRate": vsmCodingProfFaxRate,
       "vsmCodingProfFaxTxLevel": vsmCodingProfFaxTxLevel,
       "vsmCodingProfFaxCdThresh": vsmCodingProfFaxCdThresh,
       "vsmCodingProfFaxTimeOut": vsmCodingProfFaxTimeOut,
       "vsmCodingProfFaxHsPktRate": vsmCodingProfFaxHsPktRate,
       "vsmCodingProfFaxLsRedun": vsmCodingProfFaxLsRedun,
       "vsmCodingProfFaxHsRedun": vsmCodingProfFaxHsRedun,
       "vsmCodingProfFaxTcfMethod": vsmCodingProfFaxTcfMethod,
       "vsmCodingProfSilenceDetect": vsmCodingProfSilenceDetect,
       "vsmCodingProfSilenceDetectTime": vsmCodingProfSilenceDetectTime,
       "vsmCodingProfSilenceLevel": vsmCodingProfSilenceLevel,
       "vsmCodingProfVoiceComfortNoiseLevel": vsmCodingProfVoiceComfortNoiseLevel,
       "vsmCodingProfG711ModemResampMode": vsmCodingProfG711ModemResampMode,
       "vsmCodingProfSinFreqToneDet": vsmCodingProfSinFreqToneDet,
       "vsmCodingProfRowStatus": vsmCodingProfRowStatus,
       "vsmDialSchemeGroup": vsmDialSchemeGroup,
       "vsmDestinationsTable": vsmDestinationsTable,
       "vsmDestinationsEntry": vsmDestinationsEntry,
       "vsmDestinationsName": vsmDestinationsName,
       "vsmDestinationsIpAddr": vsmDestinationsIpAddr,
       "vsmDestinationsNetworkPort": vsmDestinationsNetworkPort,
       "vsmDestinationsH323Name": vsmDestinationsH323Name,
       "vsmDestinationsLocalPort": vsmDestinationsLocalPort,
       "vsmDestinationsStartChan": vsmDestinationsStartChan,
       "vsmDestinationsEndChan": vsmDestinationsEndChan,
       "vsmDestinationsType": vsmDestinationsType,
       "vsmDestinationsRowStatus": vsmDestinationsRowStatus,
       "vsmPhoneGroupTable": vsmPhoneGroupTable,
       "vsmPhoneGroupEntry": vsmPhoneGroupEntry,
       "vsmPhoneGroupName": vsmPhoneGroupName,
       "vsmPhoneGroupType": vsmPhoneGroupType,
       "vsmPhoneGroupFormat": vsmPhoneGroupFormat,
       "vsmPhoneGroupUsageVoice": vsmPhoneGroupUsageVoice,
       "vsmPhoneGroupUsageFax": vsmPhoneGroupUsageFax,
       "vsmPhoneGroupUsageModem": vsmPhoneGroupUsageModem,
       "vsmPhoneGroupUsageData": vsmPhoneGroupUsageData,
       "vsmPhoneGroupSitePrefixEnable": vsmPhoneGroupSitePrefixEnable,
       "vsmPhoneGroupSitePrefixString": vsmPhoneGroupSitePrefixString,
       "vsmPhoneGroupStripDigitLength": vsmPhoneGroupStripDigitLength,
       "vsmPhoneGroupForwardingPrefixEnable": vsmPhoneGroupForwardingPrefixEnable,
       "vsmPhoneGroupForwardingPrefix": vsmPhoneGroupForwardingPrefix,
       "vsmPhoneGroupRowStatus": vsmPhoneGroupRowStatus,
       "vsmPGNumbersTable": vsmPGNumbersTable,
       "vsmPGNumbersEntry": vsmPGNumbersEntry,
       "vsmPGNumber": vsmPGNumber,
       "vsmPGNumbersRowStatus": vsmPGNumbersRowStatus,
       "vsmNumPlanTable": vsmNumPlanTable,
       "vsmNumPlanEntry": vsmNumPlanEntry,
       "vsmNumPlanName": vsmNumPlanName,
       "vsmNumPlanHuntMethod": vsmNumPlanHuntMethod,
       "vsmNumPlanDescription": vsmNumPlanDescription,
       "vsmNumPlanAllActivate": vsmNumPlanAllActivate,
       "vsmNumPlanRowStatus": vsmNumPlanRowStatus,
       "vsmNPPhoneGroupTable": vsmNPPhoneGroupTable,
       "vsmNPPhoneGroupEntry": vsmNPPhoneGroupEntry,
       "vsmNPPhoneGroupRowStatus": vsmNPPhoneGroupRowStatus,
       "vsmNPDestinationsTable": vsmNPDestinationsTable,
       "vsmNPDestinationsEntry": vsmNPDestinationsEntry,
       "vsmNPDestinationsRowStatus": vsmNPDestinationsRowStatus,
       "vsmPhysicalGroup": vsmPhysicalGroup,
       "vsmCardConfTable": vsmCardConfTable,
       "vsmCardConfEntry": vsmCardConfEntry,
       "vsmCardSlotIndex": vsmCardSlotIndex,
       "vsmCardSubunitIndex": vsmCardSubunitIndex,
       "vsmCardIpAddr": vsmCardIpAddr,
       "vsmCardIpMask": vsmCardIpMask,
       "vsmCardIpDefGateway": vsmCardIpDefGateway,
       "vsmCardFirstDigitWaitDur": vsmCardFirstDigitWaitDur,
       "vsmCardInterDigitWaitDur": vsmCardInterDigitWaitDur,
       "vsmCardDialTimeDur": vsmCardDialTimeDur,
       "vsmCardTermDigitStr": vsmCardTermDigitStr,
       "vsmCardH323InFastStart": vsmCardH323InFastStart,
       "vsmCardH323OutFastStart": vsmCardH323OutFastStart,
       "vsmCardH323AutomaticAnswer": vsmCardH323AutomaticAnswer,
       "vsmCardConfigStatus": vsmCardConfigStatus,
       "vsmPortConfTable": vsmPortConfTable,
       "vsmPortConfEntry": vsmPortConfEntry,
       "vsmPortSlotNum": vsmPortSlotNum,
       "vsmPortNum": vsmPortNum,
       "vsmPortInterfaceType": vsmPortInterfaceType,
       "vsmPortDialType": vsmPortDialType,
       "vsmPortDsx1LineType": vsmPortDsx1LineType,
       "vsmPortDsx1LineCoding": vsmPortDsx1LineCoding,
       "vsmPortDsx1SendCode": vsmPortDsx1SendCode,
       "vsmPortDsx1CircuitIdentifier": vsmPortDsx1CircuitIdentifier,
       "vsmPortDsx1LoopbackConfig": vsmPortDsx1LoopbackConfig,
       "vsmPortDsx1LineStatus": vsmPortDsx1LineStatus,
       "vsmPortDsx1SignalMode": vsmPortDsx1SignalMode,
       "vsmPortDsx1TransmitClockSource": vsmPortDsx1TransmitClockSource,
       "vsmPortDsx1Fdl": vsmPortDsx1Fdl,
       "vsmPortDsx1LineBuildOut": vsmPortDsx1LineBuildOut,
       "vsmPortDsx1CableType": vsmPortDsx1CableType,
       "vsmPortDsx1LineLength": vsmPortDsx1LineLength,
       "vsmPortDsx1LineStatusChangeTrapEnable": vsmPortDsx1LineStatusChangeTrapEnable,
       "vsmPortDsx1LoopbackStatus": vsmPortDsx1LoopbackStatus,
       "vsmPortDsx1PortFdlRole": vsmPortDsx1PortFdlRole,
       "vsmPortDsx1PortNfasAlign": vsmPortDsx1PortNfasAlign,
       "vsmPortDsx1PortAttenuation": vsmPortDsx1PortAttenuation,
       "vsmPortIsdnProtocol": vsmPortIsdnProtocol,
       "vsmPortIsdnSwitchType": vsmPortIsdnSwitchType,
       "vsmChanConfTable": vsmChanConfTable,
       "vsmChanConfEntry": vsmChanConfEntry,
       "vsmChanSlotIndex": vsmChanSlotIndex,
       "vsmChanPortIndex": vsmChanPortIndex,
       "vsmChanIndex": vsmChanIndex,
       "vsmChanMode": vsmChanMode,
       "vsmChanPlarNumber": vsmChanPlarNumber,
       "vsmChanPerferredVoiceProfile": vsmChanPerferredVoiceProfile,
       "vsmChanPerferredFaxProfile": vsmChanPerferredFaxProfile,
       "vsmChanPerferredModemProfile": vsmChanPerferredModemProfile,
       "vsmChanISDNChanType": vsmChanISDNChanType,
       "vsmChanDslId": vsmChanDslId,
       "vsmChanDChannelPort": vsmChanDChannelPort,
       "vsmChanDChannel": vsmChanDChannel,
       "vsmChanStatus": vsmChanStatus,
       "vsmAllowedCodingProfileTable": vsmAllowedCodingProfileTable,
       "vsmAllowedCodingProfileEntry": vsmAllowedCodingProfileEntry,
       "vsmAllowedCodingProfileRowStatus": vsmAllowedCodingProfileRowStatus,
       "vsmConfigControlGroup": vsmConfigControlGroup,
       "vsmConfigDumpFlag": vsmConfigDumpFlag,
       "vsmConfigRebootFlag": vsmConfigRebootFlag,
       "vsmConfigDumpFileName": vsmConfigDumpFileName,
       "vsmStatsGroup": vsmStatsGroup,
       "vsmTeleLevelTable": vsmTeleLevelTable,
       "vsmTeleLevelEntry": vsmTeleLevelEntry,
       "vsmTeleLevelRx": vsmTeleLevelRx,
       "vsmTeleLevelTx": vsmTeleLevelTx,
       "vsmTeleLevelRxMean": vsmTeleLevelRxMean,
       "vsmTeleLevelTxMean": vsmTeleLevelTxMean,
       "vsmTeleStatsTable": vsmTeleStatsTable,
       "vsmTeleStatsEntry": vsmTeleStatsEntry,
       "vsmNumOffHooks": vsmNumOffHooks,
       "vsmNumOnHooks": vsmNumOnHooks,
       "vsmNumSeizures": vsmNumSeizures,
       "vsmNumToneDigits": vsmNumToneDigits,
       "vsmNumPulseDigits": vsmNumPulseDigits,
       "vsmResetTeleStats": vsmResetTeleStats,
       "vsmDspVPStatsTable": vsmDspVPStatsTable,
       "vsmDspVPStatsEntry": vsmDspVPStatsEntry,
       "vsmDspAvgPlayoutDelay": vsmDspAvgPlayoutDelay,
       "vsmDspLostPackets": vsmDspLostPackets,
       "vsmDspReplayPackets": vsmDspReplayPackets,
       "vsmDspIdlePackets": vsmDspIdlePackets,
       "vsmDspDroppedPackets": vsmDspDroppedPackets,
       "vsmDspReceivedPackets": vsmDspReceivedPackets,
       "vsmDspRxAvgFrameJitter": vsmDspRxAvgFrameJitter,
       "vsmResetDspPlayOutStats": vsmResetDspPlayOutStats,
       "vsmDspRxTxStatsTable": vsmDspRxTxStatsTable,
       "vsmDspRxTxStatsEntry": vsmDspRxTxStatsEntry,
       "vsmDspRxPackets": vsmDspRxPackets,
       "vsmDspTxPackets": vsmDspTxPackets,
       "vsmDspSilencePackets": vsmDspSilencePackets,
       "vsmDspRxMinJitter": vsmDspRxMinJitter,
       "vsmDspRxMaxJitter": vsmDspRxMaxJitter,
       "vsmDspRxAvgJitter": vsmDspRxAvgJitter,
       "vsmTxDroppedFrames": vsmTxDroppedFrames,
       "vsmTxOctets": vsmTxOctets,
       "vsmRxOctets": vsmRxOctets,
       "vsmAal2CodPrfChgs": vsmAal2CodPrfChgs,
       "vsmDtmfTxOctets": vsmDtmfTxOctets,
       "vsmDtmfRxOctets": vsmDtmfRxOctets,
       "vsmResetDspRxTxStats": vsmResetDspRxTxStats,
       "vsmDspVoiceErrorStatsTable": vsmDspVoiceErrorStatsTable,
       "vsmDspVoiceErrorStatsEntry": vsmDspVoiceErrorStatsEntry,
       "vsmDspInvalidHeaderCount": vsmDspInvalidHeaderCount,
       "vsmDspMicroOverflowCount": vsmDspMicroOverflowCount,
       "vsmDspLostEnhPackets": vsmDspLostEnhPackets,
       "vsmDspMissingCorePackets": vsmDspMissingCorePackets,
       "vsmDspPktsLostByNetwork": vsmDspPktsLostByNetwork,
       "vsmResetDspErrorStats": vsmResetDspErrorStats,
       "vsmDspModemStatsTable": vsmDspModemStatsTable,
       "vsmDspModemStatsEntry": vsmDspModemStatsEntry,
       "vsmDspModemStatus": vsmDspModemStatus,
       "vsmDspModemRxLevel": vsmDspModemRxLevel,
       "vsmDspModemRxRate": vsmDspModemRxRate,
       "vsmDspModemTxLevel": vsmDspModemTxLevel,
       "vsmDspModemTxRate": vsmDspModemTxRate,
       "vsmDspModemCarrFreqOffset": vsmDspModemCarrFreqOffset,
       "vsmDspModemTimeFreqOffset": vsmDspModemTimeFreqOffset,
       "vsmResetDspModemStats": vsmResetDspModemStats,
       "vsmDspFaxStatsTable": vsmDspFaxStatsTable,
       "vsmDspFaxStatsEntry": vsmDspFaxStatsEntry,
       "vsmDspFaxTxPackets": vsmDspFaxTxPackets,
       "vsmDspFaxRxPackets": vsmDspFaxRxPackets,
       "vsmDspFaxLostPackets": vsmDspFaxLostPackets,
       "vsmDspFaxDroppedPackets": vsmDspFaxDroppedPackets,
       "vsmDspFaxRxOutOfSeqPkts": vsmDspFaxRxOutOfSeqPkts,
       "vsmResetDspFaxStats": vsmResetDspFaxStats,
       "vsmISDNTeleStatsTable": vsmISDNTeleStatsTable,
       "vsmISDNTeleStatsEntry": vsmISDNTeleStatsEntry,
       "vsmNbCalls": vsmNbCalls,
       "vsmNbLocalSetup": vsmNbLocalSetup,
       "vsmNbRemoteSetup": vsmNbRemoteSetup,
       "vsmNbDropCalls": vsmNbDropCalls,
       "vsmNbFaxSwitch": vsmNbFaxSwitch,
       "vsmNbModemSwitch": vsmNbModemSwitch,
       "vsmResetISDNTeleStats": vsmResetISDNTeleStats}
)
