# SNMP MIB module (ASCEND-MIBATMPREFIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATMPREFIX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:11 2024
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

_MibatmPrefixProfile_ObjectIdentity = ObjectIdentity
mibatmPrefixProfile = _MibatmPrefixProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 22)
)
_MibatmPrefixProfileTable_Object = MibTable
mibatmPrefixProfileTable = _MibatmPrefixProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 22, 1)
)
if mibBuilder.loadTexts:
    mibatmPrefixProfileTable.setStatus("mandatory")
_MibatmPrefixProfileEntry_Object = MibTableRow
mibatmPrefixProfileEntry = _MibatmPrefixProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1)
)
mibatmPrefixProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATMPREFIX-MIB", "atmPrefixProfile-PrefixName"),
)
if mibBuilder.loadTexts:
    mibatmPrefixProfileEntry.setStatus("mandatory")
_AtmPrefixProfile_PrefixName_Type = DisplayString
_AtmPrefixProfile_PrefixName_Object = MibScalar
atmPrefixProfile_PrefixName = _AtmPrefixProfile_PrefixName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 1),
    _AtmPrefixProfile_PrefixName_Type()
)
atmPrefixProfile_PrefixName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPrefixProfile_PrefixName.setStatus("mandatory")


class _AtmPrefixProfile_UseShortAddress_Type(Integer32):
    """Custom type atmPrefixProfile_UseShortAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtmPrefixProfile_UseShortAddress_Type.__name__ = "Integer32"
_AtmPrefixProfile_UseShortAddress_Object = MibScalar
atmPrefixProfile_UseShortAddress = _AtmPrefixProfile_UseShortAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 2),
    _AtmPrefixProfile_UseShortAddress_Type()
)
atmPrefixProfile_UseShortAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPrefixProfile_UseShortAddress.setStatus("mandatory")
_AtmPrefixProfile_PnniNodePrefix_Length_Type = Integer32
_AtmPrefixProfile_PnniNodePrefix_Length_Object = MibScalar
atmPrefixProfile_PnniNodePrefix_Length = _AtmPrefixProfile_PnniNodePrefix_Length_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 3),
    _AtmPrefixProfile_PnniNodePrefix_Length_Type()
)
atmPrefixProfile_PnniNodePrefix_Length.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPrefixProfile_PnniNodePrefix_Length.setStatus("mandatory")
_AtmPrefixProfile_PnniNodePrefix_Address_Type = DisplayString
_AtmPrefixProfile_PnniNodePrefix_Address_Object = MibScalar
atmPrefixProfile_PnniNodePrefix_Address = _AtmPrefixProfile_PnniNodePrefix_Address_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 4),
    _AtmPrefixProfile_PnniNodePrefix_Address_Type()
)
atmPrefixProfile_PnniNodePrefix_Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPrefixProfile_PnniNodePrefix_Address.setStatus("mandatory")
_AtmPrefixProfile_SpvcAddressPrefix_Length_Type = Integer32
_AtmPrefixProfile_SpvcAddressPrefix_Length_Object = MibScalar
atmPrefixProfile_SpvcAddressPrefix_Length = _AtmPrefixProfile_SpvcAddressPrefix_Length_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 5),
    _AtmPrefixProfile_SpvcAddressPrefix_Length_Type()
)
atmPrefixProfile_SpvcAddressPrefix_Length.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPrefixProfile_SpvcAddressPrefix_Length.setStatus("mandatory")
_AtmPrefixProfile_SpvcAddressPrefix_Address_Type = DisplayString
_AtmPrefixProfile_SpvcAddressPrefix_Address_Object = MibScalar
atmPrefixProfile_SpvcAddressPrefix_Address = _AtmPrefixProfile_SpvcAddressPrefix_Address_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 6),
    _AtmPrefixProfile_SpvcAddressPrefix_Address_Type()
)
atmPrefixProfile_SpvcAddressPrefix_Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPrefixProfile_SpvcAddressPrefix_Address.setStatus("mandatory")
_AtmPrefixProfile_SvcAddressPrefix_Length_Type = Integer32
_AtmPrefixProfile_SvcAddressPrefix_Length_Object = MibScalar
atmPrefixProfile_SvcAddressPrefix_Length = _AtmPrefixProfile_SvcAddressPrefix_Length_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 7),
    _AtmPrefixProfile_SvcAddressPrefix_Length_Type()
)
atmPrefixProfile_SvcAddressPrefix_Length.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPrefixProfile_SvcAddressPrefix_Length.setStatus("mandatory")
_AtmPrefixProfile_SvcAddressPrefix_Address_Type = DisplayString
_AtmPrefixProfile_SvcAddressPrefix_Address_Object = MibScalar
atmPrefixProfile_SvcAddressPrefix_Address = _AtmPrefixProfile_SvcAddressPrefix_Address_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 8),
    _AtmPrefixProfile_SvcAddressPrefix_Address_Type()
)
atmPrefixProfile_SvcAddressPrefix_Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPrefixProfile_SvcAddressPrefix_Address.setStatus("mandatory")


class _AtmPrefixProfile_Action_o_Type(Integer32):
    """Custom type atmPrefixProfile_Action_o based on Integer32"""
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


_AtmPrefixProfile_Action_o_Type.__name__ = "Integer32"
_AtmPrefixProfile_Action_o_Object = MibScalar
atmPrefixProfile_Action_o = _AtmPrefixProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 9),
    _AtmPrefixProfile_Action_o_Type()
)
atmPrefixProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPrefixProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATMPREFIX-MIB",
    **{"DisplayString": DisplayString,
       "mibatmPrefixProfile": mibatmPrefixProfile,
       "mibatmPrefixProfileTable": mibatmPrefixProfileTable,
       "mibatmPrefixProfileEntry": mibatmPrefixProfileEntry,
       "atmPrefixProfile-PrefixName": atmPrefixProfile_PrefixName,
       "atmPrefixProfile-UseShortAddress": atmPrefixProfile_UseShortAddress,
       "atmPrefixProfile-PnniNodePrefix-Length": atmPrefixProfile_PnniNodePrefix_Length,
       "atmPrefixProfile-PnniNodePrefix-Address": atmPrefixProfile_PnniNodePrefix_Address,
       "atmPrefixProfile-SpvcAddressPrefix-Length": atmPrefixProfile_SpvcAddressPrefix_Length,
       "atmPrefixProfile-SpvcAddressPrefix-Address": atmPrefixProfile_SpvcAddressPrefix_Address,
       "atmPrefixProfile-SvcAddressPrefix-Length": atmPrefixProfile_SvcAddressPrefix_Length,
       "atmPrefixProfile-SvcAddressPrefix-Address": atmPrefixProfile_SvcAddressPrefix_Address,
       "atmPrefixProfile-Action-o": atmPrefixProfile_Action_o}
)
