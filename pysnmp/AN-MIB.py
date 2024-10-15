# SNMP MIB module (AN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:51 2024
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
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SiemensUnits_ObjectIdentity = ObjectIdentity
siemensUnits = _SiemensUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7)
)
_OenProductMibs_ObjectIdentity = ObjectIdentity
oenProductMibs = _OenProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1)
)
_An_ObjectIdentity = ObjectIdentity
an = _An_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2)
)
_Xld_ObjectIdentity = ObjectIdentity
xld = _Xld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1)
)
_Onu_ObjectIdentity = ObjectIdentity
onu = _Onu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1)
)
_XldOnuSnmVersion_ObjectIdentity = ObjectIdentity
xldOnuSnmVersion = _XldOnuSnmVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 100)
)


class _XldSnmMibVersion_Type(DisplayString):
    """Custom type xldSnmMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_XldSnmMibVersion_Type.__name__ = "DisplayString"
_XldSnmMibVersion_Object = MibScalar
xldSnmMibVersion = _XldSnmMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 100, 1),
    _XldSnmMibVersion_Type()
)
xldSnmMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldSnmMibVersion.setStatus("mandatory")


class _XldSnmAgentVersion_Type(DisplayString):
    """Custom type xldSnmAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_XldSnmAgentVersion_Type.__name__ = "DisplayString"
_XldSnmAgentVersion_Object = MibScalar
xldSnmAgentVersion = _XldSnmAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 100, 2),
    _XldSnmAgentVersion_Type()
)
xldSnmAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldSnmAgentVersion.setStatus("mandatory")
_Olt_ObjectIdentity = ObjectIdentity
olt = _Olt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AN-MIB",
    **{"DisplayString": DisplayString,
       "sni": sni,
       "siemensUnits": siemensUnits,
       "oenProductMibs": oenProductMibs,
       "an": an,
       "xld": xld,
       "onu": onu,
       "xldOnuSnmVersion": xldOnuSnmVersion,
       "xldSnmMibVersion": xldSnmMibVersion,
       "xldSnmAgentVersion": xldSnmAgentVersion,
       "olt": olt}
)
