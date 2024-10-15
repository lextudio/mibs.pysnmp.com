# SNMP MIB module (XYLAN-FW1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-FW1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:02 2024
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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Checkpoint_ObjectIdentity = ObjectIdentity
checkpoint = _Checkpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1919)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1919, 1)
)
_Fw_ObjectIdentity = ObjectIdentity
fw = _Fw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1919, 1, 1)
)


class _FwModuleState_Type(DisplayString):
    """Custom type fwModuleState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwModuleState_Type.__name__ = "DisplayString"
_FwModuleState_Object = MibScalar
fwModuleState = _FwModuleState_Object(
    (1, 3, 6, 1, 4, 1, 1919, 1, 1, 1),
    _FwModuleState_Type()
)
fwModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwModuleState.setStatus("mandatory")


class _FwFilterName_Type(DisplayString):
    """Custom type fwFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwFilterName_Type.__name__ = "DisplayString"
_FwFilterName_Object = MibScalar
fwFilterName = _FwFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1919, 1, 1, 2),
    _FwFilterName_Type()
)
fwFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwFilterName.setStatus("mandatory")


class _FwFilterDate_Type(DisplayString):
    """Custom type fwFilterDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FwFilterDate_Type.__name__ = "DisplayString"
_FwFilterDate_Object = MibScalar
fwFilterDate = _FwFilterDate_Object(
    (1, 3, 6, 1, 4, 1, 1919, 1, 1, 3),
    _FwFilterDate_Type()
)
fwFilterDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwFilterDate.setStatus("mandatory")
_FwAccepted_Type = Integer32
_FwAccepted_Object = MibScalar
fwAccepted = _FwAccepted_Object(
    (1, 3, 6, 1, 4, 1, 1919, 1, 1, 4),
    _FwAccepted_Type()
)
fwAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwAccepted.setStatus("mandatory")
_FwRejected_Type = Integer32
_FwRejected_Object = MibScalar
fwRejected = _FwRejected_Object(
    (1, 3, 6, 1, 4, 1, 1919, 1, 1, 5),
    _FwRejected_Type()
)
fwRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwRejected.setStatus("mandatory")
_FwDropped_Type = Integer32
_FwDropped_Object = MibScalar
fwDropped = _FwDropped_Object(
    (1, 3, 6, 1, 4, 1, 1919, 1, 1, 6),
    _FwDropped_Type()
)
fwDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwDropped.setStatus("mandatory")
_FwLogged_Type = Integer32
_FwLogged_Object = MibScalar
fwLogged = _FwLogged_Object(
    (1, 3, 6, 1, 4, 1, 1919, 1, 1, 7),
    _FwLogged_Type()
)
fwLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwLogged.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-FW1-MIB",
    **{"DisplayString": DisplayString,
       "checkpoint": checkpoint,
       "products": products,
       "fw": fw,
       "fwModuleState": fwModuleState,
       "fwFilterName": fwFilterName,
       "fwFilterDate": fwFilterDate,
       "fwAccepted": fwAccepted,
       "fwRejected": fwRejected,
       "fwDropped": fwDropped,
       "fwLogged": fwLogged}
)
