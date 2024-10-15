# SNMP MIB module (CYAN-TENGPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-TENGPORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:17 2024
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
 CyanTPConnectionStateTc,
 CyanTxControlTc,
 CyanXGOSignalTypeTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanEnDisabledTc",
    "CyanLoopbackControlTc",
    "CyanOffOnTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanSecServiceStateTc",
    "CyanTPConnectionStateTc",
    "CyanTxControlTc",
    "CyanXGOSignalTypeTc")

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

cyanTENGPortModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150)
)
cyanTENGPortModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanTENGPortMibObjects_ObjectIdentity = ObjectIdentity
cyanTENGPortMibObjects = _CyanTENGPortMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1)
)
_CyanTENGPortTable_Object = MibTable
cyanTENGPortTable = _CyanTENGPortTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1)
)
if mibBuilder.loadTexts:
    cyanTENGPortTable.setStatus("current")
_CyanTENGPortEntry_Object = MibTableRow
cyanTENGPortEntry = _CyanTENGPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1)
)
cyanTENGPortEntry.setIndexNames(
    (0, "CYAN-TENGPORT-MIB", "cyanTENGPortShelfId"),
    (0, "CYAN-TENGPORT-MIB", "cyanTENGPortModuleId"),
    (0, "CYAN-TENGPORT-MIB", "cyanTENGPortXcvrId"),
    (0, "CYAN-TENGPORT-MIB", "cyanTENGPortPortId"),
)
if mibBuilder.loadTexts:
    cyanTENGPortEntry.setStatus("current")


class _CyanTENGPortShelfId_Type(Unsigned32):
    """Custom type cyanTENGPortShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanTENGPortShelfId_Type.__name__ = "Unsigned32"
_CyanTENGPortShelfId_Object = MibTableColumn
cyanTENGPortShelfId = _CyanTENGPortShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 1),
    _CyanTENGPortShelfId_Type()
)
cyanTENGPortShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanTENGPortShelfId.setStatus("current")
_CyanTENGPortModuleId_Type = Unsigned32
_CyanTENGPortModuleId_Object = MibTableColumn
cyanTENGPortModuleId = _CyanTENGPortModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 2),
    _CyanTENGPortModuleId_Type()
)
cyanTENGPortModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanTENGPortModuleId.setStatus("current")
_CyanTENGPortXcvrId_Type = Unsigned32
_CyanTENGPortXcvrId_Object = MibTableColumn
cyanTENGPortXcvrId = _CyanTENGPortXcvrId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 3),
    _CyanTENGPortXcvrId_Type()
)
cyanTENGPortXcvrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanTENGPortXcvrId.setStatus("current")
_CyanTENGPortPortId_Type = Unsigned32
_CyanTENGPortPortId_Object = MibTableColumn
cyanTENGPortPortId = _CyanTENGPortPortId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 4),
    _CyanTENGPortPortId_Type()
)
cyanTENGPortPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanTENGPortPortId.setStatus("current")
_CyanTENGPortAdminState_Type = CyanAdminStateTc
_CyanTENGPortAdminState_Object = MibTableColumn
cyanTENGPortAdminState = _CyanTENGPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 5),
    _CyanTENGPortAdminState_Type()
)
cyanTENGPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortAdminState.setStatus("current")
_CyanTENGPortAutoinserviceSoakTimeSec_Type = Integer32
_CyanTENGPortAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanTENGPortAutoinserviceSoakTimeSec = _CyanTENGPortAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 6),
    _CyanTENGPortAutoinserviceSoakTimeSec_Type()
)
cyanTENGPortAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortAutoinserviceSoakTimeSec.setStatus("current")
_CyanTENGPortConnectionState_Type = CyanTPConnectionStateTc
_CyanTENGPortConnectionState_Object = MibTableColumn
cyanTENGPortConnectionState = _CyanTENGPortConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 7),
    _CyanTENGPortConnectionState_Type()
)
cyanTENGPortConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortConnectionState.setStatus("current")


class _CyanTENGPortDescription_Type(DisplayString):
    """Custom type cyanTENGPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CyanTENGPortDescription_Type.__name__ = "DisplayString"
_CyanTENGPortDescription_Object = MibTableColumn
cyanTENGPortDescription = _CyanTENGPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 8),
    _CyanTENGPortDescription_Type()
)
cyanTENGPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortDescription.setStatus("current")
_CyanTENGPortExternalFiberMultishelfLink_Type = CyanEnDisabledTc
_CyanTENGPortExternalFiberMultishelfLink_Object = MibTableColumn
cyanTENGPortExternalFiberMultishelfLink = _CyanTENGPortExternalFiberMultishelfLink_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 9),
    _CyanTENGPortExternalFiberMultishelfLink_Type()
)
cyanTENGPortExternalFiberMultishelfLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortExternalFiberMultishelfLink.setStatus("current")


class _CyanTENGPortExternalFiberRemotePort_Type(DisplayString):
    """Custom type cyanTENGPortExternalFiberRemotePort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_CyanTENGPortExternalFiberRemotePort_Type.__name__ = "DisplayString"
_CyanTENGPortExternalFiberRemotePort_Object = MibTableColumn
cyanTENGPortExternalFiberRemotePort = _CyanTENGPortExternalFiberRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 10),
    _CyanTENGPortExternalFiberRemotePort_Type()
)
cyanTENGPortExternalFiberRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortExternalFiberRemotePort.setStatus("current")
_CyanTENGPortLoopbackControl_Type = CyanLoopbackControlTc
_CyanTENGPortLoopbackControl_Object = MibTableColumn
cyanTENGPortLoopbackControl = _CyanTENGPortLoopbackControl_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 11),
    _CyanTENGPortLoopbackControl_Type()
)
cyanTENGPortLoopbackControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortLoopbackControl.setStatus("current")
_CyanTENGPortOperState_Type = CyanOpStateTc
_CyanTENGPortOperState_Object = MibTableColumn
cyanTENGPortOperState = _CyanTENGPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 12),
    _CyanTENGPortOperState_Type()
)
cyanTENGPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortOperState.setStatus("current")
_CyanTENGPortOperStateQual_Type = CyanOpStateQualTc
_CyanTENGPortOperStateQual_Object = MibTableColumn
cyanTENGPortOperStateQual = _CyanTENGPortOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 13),
    _CyanTENGPortOperStateQual_Type()
)
cyanTENGPortOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortOperStateQual.setStatus("current")
_CyanTENGPortRxPwr_Type = Integer32
_CyanTENGPortRxPwr_Object = MibTableColumn
cyanTENGPortRxPwr = _CyanTENGPortRxPwr_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 14),
    _CyanTENGPortRxPwr_Type()
)
cyanTENGPortRxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortRxPwr.setStatus("current")
_CyanTENGPortSecServState_Type = CyanSecServiceStateTc
_CyanTENGPortSecServState_Object = MibTableColumn
cyanTENGPortSecServState = _CyanTENGPortSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 15),
    _CyanTENGPortSecServState_Type()
)
cyanTENGPortSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortSecServState.setStatus("current")
_CyanTENGPortSignalType_Type = CyanXGOSignalTypeTc
_CyanTENGPortSignalType_Object = MibTableColumn
cyanTENGPortSignalType = _CyanTENGPortSignalType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 16),
    _CyanTENGPortSignalType_Type()
)
cyanTENGPortSignalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortSignalType.setStatus("current")
_CyanTENGPortTransmitControl_Type = CyanTxControlTc
_CyanTENGPortTransmitControl_Object = MibTableColumn
cyanTENGPortTransmitControl = _CyanTENGPortTransmitControl_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 17),
    _CyanTENGPortTransmitControl_Type()
)
cyanTENGPortTransmitControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortTransmitControl.setStatus("current")
_CyanTENGPortTxPwr_Type = Integer32
_CyanTENGPortTxPwr_Object = MibTableColumn
cyanTENGPortTxPwr = _CyanTENGPortTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 18),
    _CyanTENGPortTxPwr_Type()
)
cyanTENGPortTxPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortTxPwr.setStatus("current")
_CyanTENGPortTxStatus_Type = CyanOffOnTc
_CyanTENGPortTxStatus_Object = MibTableColumn
cyanTENGPortTxStatus = _CyanTENGPortTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 1, 1, 1, 19),
    _CyanTENGPortTxStatus_Type()
)
cyanTENGPortTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanTENGPortTxStatus.setStatus("current")

# Managed Objects groups

cyanTENGPortObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 20)
)
cyanTENGPortObjectGroup.setObjects(
      *(("CYAN-TENGPORT-MIB", "cyanTENGPortAdminState"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortAutoinserviceSoakTimeSec"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortConnectionState"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortDescription"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortExternalFiberMultishelfLink"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortExternalFiberRemotePort"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortLoopbackControl"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortOperState"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortOperStateQual"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortRxPwr"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortSecServState"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortSignalType"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortTransmitControl"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortTxPwr"),
        ("CYAN-TENGPORT-MIB", "cyanTENGPortTxStatus"))
)
if mibBuilder.loadTexts:
    cyanTENGPortObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanTENGPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 150, 30)
)
if mibBuilder.loadTexts:
    cyanTENGPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-TENGPORT-MIB",
    **{"cyanTENGPortModule": cyanTENGPortModule,
       "cyanTENGPortMibObjects": cyanTENGPortMibObjects,
       "cyanTENGPortTable": cyanTENGPortTable,
       "cyanTENGPortEntry": cyanTENGPortEntry,
       "cyanTENGPortShelfId": cyanTENGPortShelfId,
       "cyanTENGPortModuleId": cyanTENGPortModuleId,
       "cyanTENGPortXcvrId": cyanTENGPortXcvrId,
       "cyanTENGPortPortId": cyanTENGPortPortId,
       "cyanTENGPortAdminState": cyanTENGPortAdminState,
       "cyanTENGPortAutoinserviceSoakTimeSec": cyanTENGPortAutoinserviceSoakTimeSec,
       "cyanTENGPortConnectionState": cyanTENGPortConnectionState,
       "cyanTENGPortDescription": cyanTENGPortDescription,
       "cyanTENGPortExternalFiberMultishelfLink": cyanTENGPortExternalFiberMultishelfLink,
       "cyanTENGPortExternalFiberRemotePort": cyanTENGPortExternalFiberRemotePort,
       "cyanTENGPortLoopbackControl": cyanTENGPortLoopbackControl,
       "cyanTENGPortOperState": cyanTENGPortOperState,
       "cyanTENGPortOperStateQual": cyanTENGPortOperStateQual,
       "cyanTENGPortRxPwr": cyanTENGPortRxPwr,
       "cyanTENGPortSecServState": cyanTENGPortSecServState,
       "cyanTENGPortSignalType": cyanTENGPortSignalType,
       "cyanTENGPortTransmitControl": cyanTENGPortTransmitControl,
       "cyanTENGPortTxPwr": cyanTENGPortTxPwr,
       "cyanTENGPortTxStatus": cyanTENGPortTxStatus,
       "cyanTENGPortObjectGroup": cyanTENGPortObjectGroup,
       "cyanTENGPortCompliance": cyanTENGPortCompliance}
)
