# SNMP MIB module (ASCEND-MIBNUMPLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBNUMPLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:56 2024
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

_MibnumberPlanProfile_ObjectIdentity = ObjectIdentity
mibnumberPlanProfile = _MibnumberPlanProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 96)
)
_MibnumberPlanProfileTable_Object = MibTable
mibnumberPlanProfileTable = _MibnumberPlanProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 96, 1)
)
if mibBuilder.loadTexts:
    mibnumberPlanProfileTable.setStatus("mandatory")
_MibnumberPlanProfileEntry_Object = MibTableRow
mibnumberPlanProfileEntry = _MibnumberPlanProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 96, 1, 1)
)
mibnumberPlanProfileEntry.setIndexNames(
    (0, "ASCEND-MIBNUMPLAN-MIB", "numberPlanProfile-Name"),
)
if mibBuilder.loadTexts:
    mibnumberPlanProfileEntry.setStatus("mandatory")
_NumberPlanProfile_Name_Type = DisplayString
_NumberPlanProfile_Name_Object = MibScalar
numberPlanProfile_Name = _NumberPlanProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 96, 1, 1, 1),
    _NumberPlanProfile_Name_Type()
)
numberPlanProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberPlanProfile_Name.setStatus("mandatory")


class _NumberPlanProfile_Active_Type(Integer32):
    """Custom type numberPlanProfile_Active based on Integer32"""
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


_NumberPlanProfile_Active_Type.__name__ = "Integer32"
_NumberPlanProfile_Active_Object = MibScalar
numberPlanProfile_Active = _NumberPlanProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 96, 1, 1, 2),
    _NumberPlanProfile_Active_Type()
)
numberPlanProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberPlanProfile_Active.setStatus("mandatory")
_NumberPlanProfile_DialPrefix_Type = DisplayString
_NumberPlanProfile_DialPrefix_Object = MibScalar
numberPlanProfile_DialPrefix = _NumberPlanProfile_DialPrefix_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 96, 1, 1, 3),
    _NumberPlanProfile_DialPrefix_Type()
)
numberPlanProfile_DialPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberPlanProfile_DialPrefix.setStatus("mandatory")
_NumberPlanProfile_NumDigits_Type = Integer32
_NumberPlanProfile_NumDigits_Object = MibScalar
numberPlanProfile_NumDigits = _NumberPlanProfile_NumDigits_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 96, 1, 1, 4),
    _NumberPlanProfile_NumDigits_Type()
)
numberPlanProfile_NumDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberPlanProfile_NumDigits.setStatus("mandatory")


class _NumberPlanProfile_Action_o_Type(Integer32):
    """Custom type numberPlanProfile_Action_o based on Integer32"""
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


_NumberPlanProfile_Action_o_Type.__name__ = "Integer32"
_NumberPlanProfile_Action_o_Object = MibScalar
numberPlanProfile_Action_o = _NumberPlanProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 96, 1, 1, 5),
    _NumberPlanProfile_Action_o_Type()
)
numberPlanProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberPlanProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBNUMPLAN-MIB",
    **{"DisplayString": DisplayString,
       "mibnumberPlanProfile": mibnumberPlanProfile,
       "mibnumberPlanProfileTable": mibnumberPlanProfileTable,
       "mibnumberPlanProfileEntry": mibnumberPlanProfileEntry,
       "numberPlanProfile-Name": numberPlanProfile_Name,
       "numberPlanProfile-Active": numberPlanProfile_Active,
       "numberPlanProfile-DialPrefix": numberPlanProfile_DialPrefix,
       "numberPlanProfile-NumDigits": numberPlanProfile_NumDigits,
       "numberPlanProfile-Action-o": numberPlanProfile_Action_o}
)
