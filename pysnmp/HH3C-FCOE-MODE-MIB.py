# SNMP MIB module (HH3C-FCOE-MODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-FCOE-MODE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:23 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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


# MODULE-IDENTITY

hh3cFcoeMode = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 135)
)
hh3cFcoeMode.setRevisions(
        ("2013-03-08 11:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cFcoeModeMibObjects_ObjectIdentity = ObjectIdentity
hh3cFcoeModeMibObjects = _Hh3cFcoeModeMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 135, 1)
)
_Hh3cFcoeModeCfgMode_Type = Integer32
_Hh3cFcoeModeCfgMode_Object = MibScalar
hh3cFcoeModeCfgMode = _Hh3cFcoeModeCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 135, 1, 1),
    _Hh3cFcoeModeCfgMode_Type()
)
hh3cFcoeModeCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFcoeModeCfgMode.setStatus("current")


class _Hh3cFcoeModeCfgLastResult_Type(Integer32):
    """Custom type hh3cFcoeModeCfgLastResult based on Integer32"""
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
        *(("needReset", 3),
          ("noLicence", 2),
          ("success", 1),
          ("unknownFault", 4))
    )


_Hh3cFcoeModeCfgLastResult_Type.__name__ = "Integer32"
_Hh3cFcoeModeCfgLastResult_Object = MibScalar
hh3cFcoeModeCfgLastResult = _Hh3cFcoeModeCfgLastResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 135, 1, 2),
    _Hh3cFcoeModeCfgLastResult_Type()
)
hh3cFcoeModeCfgLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFcoeModeCfgLastResult.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FCOE-MODE-MIB",
    **{"hh3cFcoeMode": hh3cFcoeMode,
       "hh3cFcoeModeMibObjects": hh3cFcoeModeMibObjects,
       "hh3cFcoeModeCfgMode": hh3cFcoeModeCfgMode,
       "hh3cFcoeModeCfgLastResult": hh3cFcoeModeCfgLastResult}
)
