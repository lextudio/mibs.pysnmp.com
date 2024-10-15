# SNMP MIB module (ASCEND-MIBPERDNIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBPERDNIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:02 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibperDnisProfile_ObjectIdentity = ObjectIdentity
mibperDnisProfile = _MibperDnisProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 100)
)
_MibperDnisProfileTable_Object = MibTable
mibperDnisProfileTable = _MibperDnisProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 100, 1)
)
if mibBuilder.loadTexts:
    mibperDnisProfileTable.setStatus("mandatory")
_MibperDnisProfileEntry_Object = MibTableRow
mibperDnisProfileEntry = _MibperDnisProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 100, 1, 1)
)
mibperDnisProfileEntry.setIndexNames(
    (0, "ASCEND-MIBPERDNIS-MIB", "perDnisProfile-DialedNumber"),
)
if mibBuilder.loadTexts:
    mibperDnisProfileEntry.setStatus("mandatory")
_PerDnisProfile_DialedNumber_Type = DisplayString
_PerDnisProfile_DialedNumber_Object = MibScalar
perDnisProfile_DialedNumber = _PerDnisProfile_DialedNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 100, 1, 1, 1),
    _PerDnisProfile_DialedNumber_Type()
)
perDnisProfile_DialedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perDnisProfile_DialedNumber.setStatus("mandatory")


class _PerDnisProfile_CallType_Type(Integer32):
    """Custom type perDnisProfile_CallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("digital", 1),
          ("voice", 2))
    )


_PerDnisProfile_CallType_Type.__name__ = "Integer32"
_PerDnisProfile_CallType_Object = MibScalar
perDnisProfile_CallType = _PerDnisProfile_CallType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 100, 1, 1, 2),
    _PerDnisProfile_CallType_Type()
)
perDnisProfile_CallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perDnisProfile_CallType.setStatus("mandatory")


class _PerDnisProfile_Action_o_Type(Integer32):
    """Custom type perDnisProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_PerDnisProfile_Action_o_Type.__name__ = "Integer32"
_PerDnisProfile_Action_o_Object = MibScalar
perDnisProfile_Action_o = _PerDnisProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 100, 1, 1, 3),
    _PerDnisProfile_Action_o_Type()
)
perDnisProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perDnisProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBPERDNIS-MIB",
    **{"DisplayString": DisplayString,
       "mibperDnisProfile": mibperDnisProfile,
       "mibperDnisProfileTable": mibperDnisProfileTable,
       "mibperDnisProfileEntry": mibperDnisProfileEntry,
       "perDnisProfile-DialedNumber": perDnisProfile_DialedNumber,
       "perDnisProfile-CallType": perDnisProfile_CallType,
       "perDnisProfile-Action-o": perDnisProfile_Action_o}
)
