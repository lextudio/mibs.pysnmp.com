# SNMP MIB module (EICON-MIB-PORT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EICON-MIB-PORT
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:45 2024
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class OperState(Integer32):
    """Custom type OperState based on Integer32"""
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
        *(("active", 4),
          ("busy", 5),
          ("disabled", 2),
          ("other", 1),
          ("ready", 3))
    )





class AdminState(Integer32):
    """Custom type AdminState based on Integer32"""
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
        *(("dump", 3),
          ("invalid", 5),
          ("start", 1),
          ("stop", 2),
          ("test", 4))
    )





class ActionState(Integer32):
    """Custom type ActionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("failed", 2),
          ("in-progress", 3))
    )





class CardRef(Integer32):
    """Custom type CardRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )





class PortRef(Integer32):
    """Custom type PortRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )





class PortName(DisplayString):
    """Custom type PortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )





class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Eicon_ObjectIdentity = ObjectIdentity
eicon = _Eicon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434)
)
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2)
)
_Mibv2_ObjectIdentity = ObjectIdentity
mibv2 = _Mibv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2)
)
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3)
)
_PortNumberOfPorts_Type = PortRef
_PortNumberOfPorts_Object = MibScalar
portNumberOfPorts = _PortNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 1),
    _PortNumberOfPorts_Type()
)
portNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumberOfPorts.setStatus("mandatory")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1)
)
portEntry.setIndexNames(
    (0, "EICON-MIB-PORT", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_PortIndex_Type = PortRef
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("mandatory")
_PortLanaNo_Type = PortRef
_PortLanaNo_Object = MibTableColumn
portLanaNo = _PortLanaNo_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 2),
    _PortLanaNo_Type()
)
portLanaNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLanaNo.setStatus("mandatory")
_PortName_Type = PortName
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 3),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("mandatory")
_PortCardLocation_Type = CardRef
_PortCardLocation_Object = MibTableColumn
portCardLocation = _PortCardLocation_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 4),
    _PortCardLocation_Type()
)
portCardLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCardLocation.setStatus("mandatory")


class _PortDescription_Type(DisplayString):
    """Custom type portDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PortDescription_Type.__name__ = "DisplayString"
_PortDescription_Object = MibTableColumn
portDescription = _PortDescription_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 5),
    _PortDescription_Type()
)
portDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDescription.setStatus("mandatory")
_PortOperState_Type = OperState
_PortOperState_Object = MibTableColumn
portOperState = _PortOperState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 6),
    _PortOperState_Type()
)
portOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperState.setStatus("mandatory")
_PortAdminStateCtr_Type = AdminState
_PortAdminStateCtr_Object = MibTableColumn
portAdminStateCtr = _PortAdminStateCtr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 7),
    _PortAdminStateCtr_Type()
)
portAdminStateCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminStateCtr.setStatus("mandatory")
_PortOpenTime_Type = TimeTicks
_PortOpenTime_Object = MibTableColumn
portOpenTime = _PortOpenTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 8),
    _PortOpenTime_Type()
)
portOpenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpenTime.setStatus("mandatory")
_PortProtocols_Type = Integer32
_PortProtocols_Object = MibTableColumn
portProtocols = _PortProtocols_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 9),
    _PortProtocols_Type()
)
portProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portProtocols.setStatus("mandatory")


class _PortDialerType_Type(Integer32):
    """Custom type portDialerType based on Integer32"""
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
        *(("at-cmd", 4),
          ("direct", 1),
          ("isdn-stat", 5),
          ("none", 7),
          ("other", 8),
          ("v22bis", 3),
          ("v25bis", 2),
          ("v32bis", 6))
    )


_PortDialerType_Type.__name__ = "Integer32"
_PortDialerType_Object = MibTableColumn
portDialerType = _PortDialerType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 10),
    _PortDialerType_Type()
)
portDialerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDialerType.setStatus("mandatory")
_PortActionState_Type = ActionState
_PortActionState_Object = MibTableColumn
portActionState = _PortActionState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 11),
    _PortActionState_Type()
)
portActionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portActionState.setStatus("mandatory")


class _PortActionError_Type(Integer32):
    """Custom type portActionError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("err-ABORT", 3),
          ("err-FAILED", 4),
          ("err-PARTIAL", 2),
          ("err-WARNING", 1),
          ("no-error", 0))
    )


_PortActionError_Type.__name__ = "Integer32"
_PortActionError_Object = MibTableColumn
portActionError = _PortActionError_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 12),
    _PortActionError_Type()
)
portActionError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portActionError.setStatus("mandatory")
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4)
)

# Managed Objects groups


# Notification objects

portTrapStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 434, 0, 31)
)
portTrapStateChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("EICON-MIB-PORT", "portIndex"),
        ("EICON-MIB-PORT", "portOperState"))
)
if mibBuilder.loadTexts:
    portTrapStateChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EICON-MIB-PORT",
    **{"OperState": OperState,
       "AdminState": AdminState,
       "ActionState": ActionState,
       "CardRef": CardRef,
       "PortRef": PortRef,
       "PortName": PortName,
       "PositiveInteger": PositiveInteger,
       "eicon": eicon,
       "portTrapStateChange": portTrapStateChange,
       "management": management,
       "mibv2": mibv2,
       "port": port,
       "portNumberOfPorts": portNumberOfPorts,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portLanaNo": portLanaNo,
       "portName": portName,
       "portCardLocation": portCardLocation,
       "portDescription": portDescription,
       "portOperState": portOperState,
       "portAdminStateCtr": portAdminStateCtr,
       "portOpenTime": portOpenTime,
       "portProtocols": portProtocols,
       "portDialerType": portDialerType,
       "portActionState": portActionState,
       "portActionError": portActionError,
       "module": module}
)
