# SNMP MIB module (XEDIA-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:40 2024
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

xediaRegistrations = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LongDisplayString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )



# MIB Managed Objects in the order of their OIDs

_Xedia_ObjectIdentity = ObjectIdentity
xedia = _Xedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838)
)
if mibBuilder.loadTexts:
    xedia.setStatus("current")
_XediaMibs_ObjectIdentity = ObjectIdentity
xediaMibs = _XediaMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3)
)
if mibBuilder.loadTexts:
    xediaMibs.setStatus("current")
_XediaClasses_ObjectIdentity = ObjectIdentity
xediaClasses = _XediaClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 4)
)
if mibBuilder.loadTexts:
    xediaClasses.setStatus("current")
_XediaProducts_ObjectIdentity = ObjectIdentity
xediaProducts = _XediaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 5)
)
if mibBuilder.loadTexts:
    xediaProducts.setStatus("current")
_XediaAccessView_ObjectIdentity = ObjectIdentity
xediaAccessView = _XediaAccessView_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 6)
)
if mibBuilder.loadTexts:
    xediaAccessView.setStatus("current")
_XediaQvpnBuilder_ObjectIdentity = ObjectIdentity
xediaQvpnBuilder = _XediaQvpnBuilder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 6, 1)
)
if mibBuilder.loadTexts:
    xediaQvpnBuilder.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-REG",
    **{"LongDisplayString": LongDisplayString,
       "xedia": xedia,
       "xediaRegistrations": xediaRegistrations,
       "xediaMibs": xediaMibs,
       "xediaClasses": xediaClasses,
       "xediaProducts": xediaProducts,
       "xediaAccessView": xediaAccessView,
       "xediaQvpnBuilder": xediaQvpnBuilder}
)
