# SNMP MIB module (ASCEND-MIBDEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBDEST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:27 2024
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

_MibdestProfile_ObjectIdentity = ObjectIdentity
mibdestProfile = _MibdestProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 73)
)
_MibdestProfileTable_Object = MibTable
mibdestProfileTable = _MibdestProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 73, 1)
)
if mibBuilder.loadTexts:
    mibdestProfileTable.setStatus("mandatory")
_MibdestProfileEntry_Object = MibTableRow
mibdestProfileEntry = _MibdestProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 73, 1, 1)
)
mibdestProfileEntry.setIndexNames(
    (0, "ASCEND-MIBDEST-MIB", "destProfile-PlanNumber"),
)
if mibBuilder.loadTexts:
    mibdestProfileEntry.setStatus("mandatory")
_DestProfile_PlanNumber_Type = Integer32
_DestProfile_PlanNumber_Object = MibScalar
destProfile_PlanNumber = _DestProfile_PlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 73, 1, 1, 1),
    _DestProfile_PlanNumber_Type()
)
destProfile_PlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destProfile_PlanNumber.setStatus("mandatory")
_DestProfile_Name_Type = DisplayString
_DestProfile_Name_Object = MibScalar
destProfile_Name = _DestProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 73, 1, 1, 2),
    _DestProfile_Name_Type()
)
destProfile_Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destProfile_Name.setStatus("mandatory")


class _DestProfile_NumberOption_Type(Integer32):
    """Custom type destProfile_NumberOption based on Integer32"""
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
        *(("destSelAnyAvail", 3),
          ("destSelFirstActive", 2),
          ("destSelFirstAvail", 1),
          ("numberOfDestSel", 4))
    )


_DestProfile_NumberOption_Type.__name__ = "Integer32"
_DestProfile_NumberOption_Object = MibScalar
destProfile_NumberOption = _DestProfile_NumberOption_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 73, 1, 1, 3),
    _DestProfile_NumberOption_Type()
)
destProfile_NumberOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destProfile_NumberOption.setStatus("mandatory")


class _DestProfile_Action_o_Type(Integer32):
    """Custom type destProfile_Action_o based on Integer32"""
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


_DestProfile_Action_o_Type.__name__ = "Integer32"
_DestProfile_Action_o_Object = MibScalar
destProfile_Action_o = _DestProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 73, 1, 1, 4),
    _DestProfile_Action_o_Type()
)
destProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destProfile_Action_o.setStatus("mandatory")
_MibdestProfile_DestNumberTable_Object = MibTable
mibdestProfile_DestNumberTable = _MibdestProfile_DestNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 73, 2)
)
if mibBuilder.loadTexts:
    mibdestProfile_DestNumberTable.setStatus("mandatory")
_MibdestProfile_DestNumberEntry_Object = MibTableRow
mibdestProfile_DestNumberEntry = _MibdestProfile_DestNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 73, 2, 1)
)
mibdestProfile_DestNumberEntry.setIndexNames(
    (0, "ASCEND-MIBDEST-MIB", "destProfile-DestNumber-PlanNumber"),
    (0, "ASCEND-MIBDEST-MIB", "destProfile-DestNumber-Index-o"),
)
if mibBuilder.loadTexts:
    mibdestProfile_DestNumberEntry.setStatus("mandatory")
_DestProfile_DestNumber_PlanNumber_Type = Integer32
_DestProfile_DestNumber_PlanNumber_Object = MibScalar
destProfile_DestNumber_PlanNumber = _DestProfile_DestNumber_PlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 73, 2, 1, 1),
    _DestProfile_DestNumber_PlanNumber_Type()
)
destProfile_DestNumber_PlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destProfile_DestNumber_PlanNumber.setStatus("mandatory")
_DestProfile_DestNumber_Index_o_Type = Integer32
_DestProfile_DestNumber_Index_o_Object = MibScalar
destProfile_DestNumber_Index_o = _DestProfile_DestNumber_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 73, 2, 1, 2),
    _DestProfile_DestNumber_Index_o_Type()
)
destProfile_DestNumber_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destProfile_DestNumber_Index_o.setStatus("mandatory")
_DestProfile_DestNumber_PhoneNumber_Type = DisplayString
_DestProfile_DestNumber_PhoneNumber_Object = MibScalar
destProfile_DestNumber_PhoneNumber = _DestProfile_DestNumber_PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 73, 2, 1, 3),
    _DestProfile_DestNumber_PhoneNumber_Type()
)
destProfile_DestNumber_PhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destProfile_DestNumber_PhoneNumber.setStatus("mandatory")
_DestProfile_DestNumber_CallByCallId_Type = Integer32
_DestProfile_DestNumber_CallByCallId_Object = MibScalar
destProfile_DestNumber_CallByCallId = _DestProfile_DestNumber_CallByCallId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 73, 2, 1, 4),
    _DestProfile_DestNumber_CallByCallId_Type()
)
destProfile_DestNumber_CallByCallId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destProfile_DestNumber_CallByCallId.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBDEST-MIB",
    **{"DisplayString": DisplayString,
       "mibdestProfile": mibdestProfile,
       "mibdestProfileTable": mibdestProfileTable,
       "mibdestProfileEntry": mibdestProfileEntry,
       "destProfile-PlanNumber": destProfile_PlanNumber,
       "destProfile-Name": destProfile_Name,
       "destProfile-NumberOption": destProfile_NumberOption,
       "destProfile-Action-o": destProfile_Action_o,
       "mibdestProfile-DestNumberTable": mibdestProfile_DestNumberTable,
       "mibdestProfile-DestNumberEntry": mibdestProfile_DestNumberEntry,
       "destProfile-DestNumber-PlanNumber": destProfile_DestNumber_PlanNumber,
       "destProfile-DestNumber-Index-o": destProfile_DestNumber_Index_o,
       "destProfile-DestNumber-PhoneNumber": destProfile_DestNumber_PhoneNumber,
       "destProfile-DestNumber-CallByCallId": destProfile_DestNumber_CallByCallId}
)
