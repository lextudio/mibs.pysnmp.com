# SNMP MIB module (ASCEND-MIBSHASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSHASH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:10 2024
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

_MibsHashProfile_ObjectIdentity = ObjectIdentity
mibsHashProfile = _MibsHashProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 108)
)
_MibsHashProfileTable_Object = MibTable
mibsHashProfileTable = _MibsHashProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 108, 1)
)
if mibBuilder.loadTexts:
    mibsHashProfileTable.setStatus("mandatory")
_MibsHashProfileEntry_Object = MibTableRow
mibsHashProfileEntry = _MibsHashProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 108, 1, 1)
)
mibsHashProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSHASH-MIB", "sHashProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibsHashProfileEntry.setStatus("mandatory")
_SHashProfile_Index_o_Type = Integer32
_SHashProfile_Index_o_Object = MibScalar
sHashProfile_Index_o = _SHashProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 108, 1, 1, 1),
    _SHashProfile_Index_o_Type()
)
sHashProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sHashProfile_Index_o.setStatus("mandatory")
_SHashProfile_Ipsec_Type = DisplayString
_SHashProfile_Ipsec_Object = MibScalar
sHashProfile_Ipsec = _SHashProfile_Ipsec_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 108, 1, 1, 2),
    _SHashProfile_Ipsec_Type()
)
sHashProfile_Ipsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sHashProfile_Ipsec.setStatus("mandatory")


class _SHashProfile_Action_o_Type(Integer32):
    """Custom type sHashProfile_Action_o based on Integer32"""
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


_SHashProfile_Action_o_Type.__name__ = "Integer32"
_SHashProfile_Action_o_Object = MibScalar
sHashProfile_Action_o = _SHashProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 108, 1, 1, 3),
    _SHashProfile_Action_o_Type()
)
sHashProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sHashProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSHASH-MIB",
    **{"DisplayString": DisplayString,
       "mibsHashProfile": mibsHashProfile,
       "mibsHashProfileTable": mibsHashProfileTable,
       "mibsHashProfileEntry": mibsHashProfileEntry,
       "sHashProfile-Index-o": sHashProfile_Index_o,
       "sHashProfile-Ipsec": sHashProfile_Ipsec,
       "sHashProfile-Action-o": sHashProfile_Action_o}
)
