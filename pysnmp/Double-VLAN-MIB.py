# SNMP MIB module (Double-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Double-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:35:58 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swDoubleVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 28)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwDoubleVlanCtrl_ObjectIdentity = ObjectIdentity
swDoubleVlanCtrl = _SwDoubleVlanCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 1)
)


class _SwDoubleVlanGlobalState_Type(Integer32):
    """Custom type swDoubleVlanGlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwDoubleVlanGlobalState_Type.__name__ = "Integer32"
_SwDoubleVlanGlobalState_Object = MibScalar
swDoubleVlanGlobalState = _SwDoubleVlanGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 1, 1),
    _SwDoubleVlanGlobalState_Type()
)
swDoubleVlanGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDoubleVlanGlobalState.setStatus("current")
_SwDoubleVlanInfo_ObjectIdentity = ObjectIdentity
swDoubleVlanInfo = _SwDoubleVlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 2)
)
_SwDoubleVlanMgmt_ObjectIdentity = ObjectIdentity
swDoubleVlanMgmt = _SwDoubleVlanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 3)
)
_SwDoubleVlanCtrlTable_Object = MibTable
swDoubleVlanCtrlTable = _SwDoubleVlanCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1)
)
if mibBuilder.loadTexts:
    swDoubleVlanCtrlTable.setStatus("current")
_SwDoubleVlanCtrlEntry_Object = MibTableRow
swDoubleVlanCtrlEntry = _SwDoubleVlanCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1)
)
swDoubleVlanCtrlEntry.setIndexNames(
    (0, "Double-VLAN-MIB", "swDoubleVlanSPVIDIndex"),
)
if mibBuilder.loadTexts:
    swDoubleVlanCtrlEntry.setStatus("current")


class _SwDoubleVlanSPVIDIndex_Type(Integer32):
    """Custom type swDoubleVlanSPVIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwDoubleVlanSPVIDIndex_Type.__name__ = "Integer32"
_SwDoubleVlanSPVIDIndex_Object = MibTableColumn
swDoubleVlanSPVIDIndex = _SwDoubleVlanSPVIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 1),
    _SwDoubleVlanSPVIDIndex_Type()
)
swDoubleVlanSPVIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDoubleVlanSPVIDIndex.setStatus("current")


class _SwDoubleVlanName_Type(DisplayString):
    """Custom type swDoubleVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwDoubleVlanName_Type.__name__ = "DisplayString"
_SwDoubleVlanName_Object = MibTableColumn
swDoubleVlanName = _SwDoubleVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 2),
    _SwDoubleVlanName_Type()
)
swDoubleVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDoubleVlanName.setStatus("current")


class _SwDoubleVlanTPID_Type(OctetString):
    """Custom type swDoubleVlanTPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwDoubleVlanTPID_Type.__name__ = "OctetString"
_SwDoubleVlanTPID_Object = MibTableColumn
swDoubleVlanTPID = _SwDoubleVlanTPID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 3),
    _SwDoubleVlanTPID_Type()
)
swDoubleVlanTPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDoubleVlanTPID.setStatus("current")
_SwDoubleVlanUplinkPorts_Type = PortList
_SwDoubleVlanUplinkPorts_Object = MibTableColumn
swDoubleVlanUplinkPorts = _SwDoubleVlanUplinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 4),
    _SwDoubleVlanUplinkPorts_Type()
)
swDoubleVlanUplinkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDoubleVlanUplinkPorts.setStatus("current")
_SwDoubleVlanAccessPorts_Type = PortList
_SwDoubleVlanAccessPorts_Object = MibTableColumn
swDoubleVlanAccessPorts = _SwDoubleVlanAccessPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 5),
    _SwDoubleVlanAccessPorts_Type()
)
swDoubleVlanAccessPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDoubleVlanAccessPorts.setStatus("current")
_SwDoubleVlanUnknowPorts_Type = PortList
_SwDoubleVlanUnknowPorts_Object = MibTableColumn
swDoubleVlanUnknowPorts = _SwDoubleVlanUnknowPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 6),
    _SwDoubleVlanUnknowPorts_Type()
)
swDoubleVlanUnknowPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDoubleVlanUnknowPorts.setStatus("current")
_SwDoubleVlanDeletePorts_Type = PortList
_SwDoubleVlanDeletePorts_Object = MibTableColumn
swDoubleVlanDeletePorts = _SwDoubleVlanDeletePorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 7),
    _SwDoubleVlanDeletePorts_Type()
)
swDoubleVlanDeletePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDoubleVlanDeletePorts.setStatus("current")
_SwDoubleVlanStatus_Type = RowStatus
_SwDoubleVlanStatus_Object = MibTableColumn
swDoubleVlanStatus = _SwDoubleVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 28, 3, 1, 1, 9),
    _SwDoubleVlanStatus_Type()
)
swDoubleVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDoubleVlanStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Double-VLAN-MIB",
    **{"PortList": PortList,
       "swDoubleVlanMIB": swDoubleVlanMIB,
       "swDoubleVlanCtrl": swDoubleVlanCtrl,
       "swDoubleVlanGlobalState": swDoubleVlanGlobalState,
       "swDoubleVlanInfo": swDoubleVlanInfo,
       "swDoubleVlanMgmt": swDoubleVlanMgmt,
       "swDoubleVlanCtrlTable": swDoubleVlanCtrlTable,
       "swDoubleVlanCtrlEntry": swDoubleVlanCtrlEntry,
       "swDoubleVlanSPVIDIndex": swDoubleVlanSPVIDIndex,
       "swDoubleVlanName": swDoubleVlanName,
       "swDoubleVlanTPID": swDoubleVlanTPID,
       "swDoubleVlanUplinkPorts": swDoubleVlanUplinkPorts,
       "swDoubleVlanAccessPorts": swDoubleVlanAccessPorts,
       "swDoubleVlanUnknowPorts": swDoubleVlanUnknowPorts,
       "swDoubleVlanDeletePorts": swDoubleVlanDeletePorts,
       "swDoubleVlanStatus": swDoubleVlanStatus}
)
