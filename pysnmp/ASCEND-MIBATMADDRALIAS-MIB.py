# SNMP MIB module (ASCEND-MIBATMADDRALIAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATMADDRALIAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:06 2024
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

_MibatmAddrAliasProfile_ObjectIdentity = ObjectIdentity
mibatmAddrAliasProfile = _MibatmAddrAliasProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 37)
)
_MibatmAddrAliasProfileTable_Object = MibTable
mibatmAddrAliasProfileTable = _MibatmAddrAliasProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 37, 1)
)
if mibBuilder.loadTexts:
    mibatmAddrAliasProfileTable.setStatus("mandatory")
_MibatmAddrAliasProfileEntry_Object = MibTableRow
mibatmAddrAliasProfileEntry = _MibatmAddrAliasProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1)
)
mibatmAddrAliasProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATMADDRALIAS-MIB", "atmAddrAliasProfile-AliasName"),
)
if mibBuilder.loadTexts:
    mibatmAddrAliasProfileEntry.setStatus("mandatory")
_AtmAddrAliasProfile_AliasName_Type = DisplayString
_AtmAddrAliasProfile_AliasName_Object = MibScalar
atmAddrAliasProfile_AliasName = _AtmAddrAliasProfile_AliasName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1, 1),
    _AtmAddrAliasProfile_AliasName_Type()
)
atmAddrAliasProfile_AliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAddrAliasProfile_AliasName.setStatus("mandatory")
_AtmAddrAliasProfile_Address_Type = DisplayString
_AtmAddrAliasProfile_Address_Object = MibScalar
atmAddrAliasProfile_Address = _AtmAddrAliasProfile_Address_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1, 2),
    _AtmAddrAliasProfile_Address_Type()
)
atmAddrAliasProfile_Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAddrAliasProfile_Address.setStatus("mandatory")
_AtmAddrAliasProfile_Length_Type = Integer32
_AtmAddrAliasProfile_Length_Object = MibScalar
atmAddrAliasProfile_Length = _AtmAddrAliasProfile_Length_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1, 3),
    _AtmAddrAliasProfile_Length_Type()
)
atmAddrAliasProfile_Length.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAddrAliasProfile_Length.setStatus("mandatory")


class _AtmAddrAliasProfile_Action_o_Type(Integer32):
    """Custom type atmAddrAliasProfile_Action_o based on Integer32"""
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


_AtmAddrAliasProfile_Action_o_Type.__name__ = "Integer32"
_AtmAddrAliasProfile_Action_o_Object = MibScalar
atmAddrAliasProfile_Action_o = _AtmAddrAliasProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1, 4),
    _AtmAddrAliasProfile_Action_o_Type()
)
atmAddrAliasProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmAddrAliasProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATMADDRALIAS-MIB",
    **{"DisplayString": DisplayString,
       "mibatmAddrAliasProfile": mibatmAddrAliasProfile,
       "mibatmAddrAliasProfileTable": mibatmAddrAliasProfileTable,
       "mibatmAddrAliasProfileEntry": mibatmAddrAliasProfileEntry,
       "atmAddrAliasProfile-AliasName": atmAddrAliasProfile_AliasName,
       "atmAddrAliasProfile-Address": atmAddrAliasProfile_Address,
       "atmAddrAliasProfile-Length": atmAddrAliasProfile_Length,
       "atmAddrAliasProfile-Action-o": atmAddrAliasProfile_Action_o}
)
