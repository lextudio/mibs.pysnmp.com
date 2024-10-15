# SNMP MIB module (CYAN-GEPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-GEPORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:08 2024
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

(cyanEntityModules,) = mibBuilder.importSymbols(
    "CYAN-MIB",
    "cyanEntityModules")

(CyanAdminStateTc,
 CyanEnDisabledTc,
 CyanLoopbackControlTc,
 CyanOffOnTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanSecServiceStateTc,
 CyanTxControlTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanEnDisabledTc",
    "CyanLoopbackControlTc",
    "CyanOffOnTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanSecServiceStateTc",
    "CyanTxControlTc")

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

cyanGEPortModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160)
)
cyanGEPortModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanGEPortMibObjects_ObjectIdentity = ObjectIdentity
cyanGEPortMibObjects = _CyanGEPortMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1)
)
_CyanGEPortTable_Object = MibTable
cyanGEPortTable = _CyanGEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1)
)
if mibBuilder.loadTexts:
    cyanGEPortTable.setStatus("current")
_CyanGEPortEntry_Object = MibTableRow
cyanGEPortEntry = _CyanGEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1)
)
cyanGEPortEntry.setIndexNames(
    (0, "CYAN-GEPORT-MIB", "cyanGEPortShelfId"),
    (0, "CYAN-GEPORT-MIB", "cyanGEPortModuleId"),
    (0, "CYAN-GEPORT-MIB", "cyanGEPortXcvrId"),
    (0, "CYAN-GEPORT-MIB", "cyanGEPortPortId"),
)
if mibBuilder.loadTexts:
    cyanGEPortEntry.setStatus("current")


class _CyanGEPortShelfId_Type(Unsigned32):
    """Custom type cyanGEPortShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanGEPortShelfId_Type.__name__ = "Unsigned32"
_CyanGEPortShelfId_Object = MibTableColumn
cyanGEPortShelfId = _CyanGEPortShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 1),
    _CyanGEPortShelfId_Type()
)
cyanGEPortShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanGEPortShelfId.setStatus("current")
_CyanGEPortModuleId_Type = Unsigned32
_CyanGEPortModuleId_Object = MibTableColumn
cyanGEPortModuleId = _CyanGEPortModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 2),
    _CyanGEPortModuleId_Type()
)
cyanGEPortModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanGEPortModuleId.setStatus("current")
_CyanGEPortXcvrId_Type = Unsigned32
_CyanGEPortXcvrId_Object = MibTableColumn
cyanGEPortXcvrId = _CyanGEPortXcvrId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 3),
    _CyanGEPortXcvrId_Type()
)
cyanGEPortXcvrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanGEPortXcvrId.setStatus("current")
_CyanGEPortPortId_Type = Unsigned32
_CyanGEPortPortId_Object = MibTableColumn
cyanGEPortPortId = _CyanGEPortPortId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 4),
    _CyanGEPortPortId_Type()
)
cyanGEPortPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanGEPortPortId.setStatus("current")
_CyanGEPortAdminState_Type = CyanAdminStateTc
_CyanGEPortAdminState_Object = MibTableColumn
cyanGEPortAdminState = _CyanGEPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 5),
    _CyanGEPortAdminState_Type()
)
cyanGEPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGEPortAdminState.setStatus("current")
_CyanGEPortAutoinserviceSoakTimeSec_Type = Integer32
_CyanGEPortAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanGEPortAutoinserviceSoakTimeSec = _CyanGEPortAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 6),
    _CyanGEPortAutoinserviceSoakTimeSec_Type()
)
cyanGEPortAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGEPortAutoinserviceSoakTimeSec.setStatus("current")


class _CyanGEPortDescription_Type(DisplayString):
    """Custom type cyanGEPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanGEPortDescription_Type.__name__ = "DisplayString"
_CyanGEPortDescription_Object = MibTableColumn
cyanGEPortDescription = _CyanGEPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 7),
    _CyanGEPortDescription_Type()
)
cyanGEPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGEPortDescription.setStatus("current")
_CyanGEPortExternalFiberMultishelfLink_Type = CyanEnDisabledTc
_CyanGEPortExternalFiberMultishelfLink_Object = MibTableColumn
cyanGEPortExternalFiberMultishelfLink = _CyanGEPortExternalFiberMultishelfLink_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 8),
    _CyanGEPortExternalFiberMultishelfLink_Type()
)
cyanGEPortExternalFiberMultishelfLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGEPortExternalFiberMultishelfLink.setStatus("current")


class _CyanGEPortExternalFiberRemotePort_Type(DisplayString):
    """Custom type cyanGEPortExternalFiberRemotePort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_CyanGEPortExternalFiberRemotePort_Type.__name__ = "DisplayString"
_CyanGEPortExternalFiberRemotePort_Object = MibTableColumn
cyanGEPortExternalFiberRemotePort = _CyanGEPortExternalFiberRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 9),
    _CyanGEPortExternalFiberRemotePort_Type()
)
cyanGEPortExternalFiberRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGEPortExternalFiberRemotePort.setStatus("current")
_CyanGEPortLoopbackControl_Type = CyanLoopbackControlTc
_CyanGEPortLoopbackControl_Object = MibTableColumn
cyanGEPortLoopbackControl = _CyanGEPortLoopbackControl_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 10),
    _CyanGEPortLoopbackControl_Type()
)
cyanGEPortLoopbackControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGEPortLoopbackControl.setStatus("current")
_CyanGEPortOperState_Type = CyanOpStateTc
_CyanGEPortOperState_Object = MibTableColumn
cyanGEPortOperState = _CyanGEPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 11),
    _CyanGEPortOperState_Type()
)
cyanGEPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGEPortOperState.setStatus("current")
_CyanGEPortOperStateQual_Type = CyanOpStateQualTc
_CyanGEPortOperStateQual_Object = MibTableColumn
cyanGEPortOperStateQual = _CyanGEPortOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 12),
    _CyanGEPortOperStateQual_Type()
)
cyanGEPortOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGEPortOperStateQual.setStatus("current")
_CyanGEPortRxPwr_Type = Integer32
_CyanGEPortRxPwr_Object = MibTableColumn
cyanGEPortRxPwr = _CyanGEPortRxPwr_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 13),
    _CyanGEPortRxPwr_Type()
)
cyanGEPortRxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGEPortRxPwr.setStatus("current")
_CyanGEPortSecServState_Type = CyanSecServiceStateTc
_CyanGEPortSecServState_Object = MibTableColumn
cyanGEPortSecServState = _CyanGEPortSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 14),
    _CyanGEPortSecServState_Type()
)
cyanGEPortSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGEPortSecServState.setStatus("current")
_CyanGEPortTransmitControl_Type = CyanTxControlTc
_CyanGEPortTransmitControl_Object = MibTableColumn
cyanGEPortTransmitControl = _CyanGEPortTransmitControl_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 15),
    _CyanGEPortTransmitControl_Type()
)
cyanGEPortTransmitControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGEPortTransmitControl.setStatus("current")
_CyanGEPortTxPwr_Type = Integer32
_CyanGEPortTxPwr_Object = MibTableColumn
cyanGEPortTxPwr = _CyanGEPortTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 16),
    _CyanGEPortTxPwr_Type()
)
cyanGEPortTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGEPortTxPwr.setStatus("current")
_CyanGEPortTxStatus_Type = CyanOffOnTc
_CyanGEPortTxStatus_Object = MibTableColumn
cyanGEPortTxStatus = _CyanGEPortTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 1, 1, 1, 17),
    _CyanGEPortTxStatus_Type()
)
cyanGEPortTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanGEPortTxStatus.setStatus("current")

# Managed Objects groups

cyanGEPortObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 20)
)
cyanGEPortObjectGroup.setObjects(
      *(("CYAN-GEPORT-MIB", "cyanGEPortAdminState"),
        ("CYAN-GEPORT-MIB", "cyanGEPortAutoinserviceSoakTimeSec"),
        ("CYAN-GEPORT-MIB", "cyanGEPortDescription"),
        ("CYAN-GEPORT-MIB", "cyanGEPortExternalFiberMultishelfLink"),
        ("CYAN-GEPORT-MIB", "cyanGEPortExternalFiberRemotePort"),
        ("CYAN-GEPORT-MIB", "cyanGEPortLoopbackControl"),
        ("CYAN-GEPORT-MIB", "cyanGEPortOperState"),
        ("CYAN-GEPORT-MIB", "cyanGEPortOperStateQual"),
        ("CYAN-GEPORT-MIB", "cyanGEPortRxPwr"),
        ("CYAN-GEPORT-MIB", "cyanGEPortSecServState"),
        ("CYAN-GEPORT-MIB", "cyanGEPortTransmitControl"),
        ("CYAN-GEPORT-MIB", "cyanGEPortTxPwr"),
        ("CYAN-GEPORT-MIB", "cyanGEPortTxStatus"))
)
if mibBuilder.loadTexts:
    cyanGEPortObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanGEPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 160, 30)
)
if mibBuilder.loadTexts:
    cyanGEPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-GEPORT-MIB",
    **{"cyanGEPortModule": cyanGEPortModule,
       "cyanGEPortMibObjects": cyanGEPortMibObjects,
       "cyanGEPortTable": cyanGEPortTable,
       "cyanGEPortEntry": cyanGEPortEntry,
       "cyanGEPortShelfId": cyanGEPortShelfId,
       "cyanGEPortModuleId": cyanGEPortModuleId,
       "cyanGEPortXcvrId": cyanGEPortXcvrId,
       "cyanGEPortPortId": cyanGEPortPortId,
       "cyanGEPortAdminState": cyanGEPortAdminState,
       "cyanGEPortAutoinserviceSoakTimeSec": cyanGEPortAutoinserviceSoakTimeSec,
       "cyanGEPortDescription": cyanGEPortDescription,
       "cyanGEPortExternalFiberMultishelfLink": cyanGEPortExternalFiberMultishelfLink,
       "cyanGEPortExternalFiberRemotePort": cyanGEPortExternalFiberRemotePort,
       "cyanGEPortLoopbackControl": cyanGEPortLoopbackControl,
       "cyanGEPortOperState": cyanGEPortOperState,
       "cyanGEPortOperStateQual": cyanGEPortOperStateQual,
       "cyanGEPortRxPwr": cyanGEPortRxPwr,
       "cyanGEPortSecServState": cyanGEPortSecServState,
       "cyanGEPortTransmitControl": cyanGEPortTransmitControl,
       "cyanGEPortTxPwr": cyanGEPortTxPwr,
       "cyanGEPortTxStatus": cyanGEPortTxStatus,
       "cyanGEPortObjectGroup": cyanGEPortObjectGroup,
       "cyanGEPortCompliance": cyanGEPortCompliance}
)
