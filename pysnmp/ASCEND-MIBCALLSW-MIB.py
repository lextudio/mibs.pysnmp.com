# SNMP MIB module (ASCEND-MIBCALLSW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBCALLSW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:20 2024
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

_MibcallSwitchingProfile_ObjectIdentity = ObjectIdentity
mibcallSwitchingProfile = _MibcallSwitchingProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 65)
)
_MibcallSwitchingProfileTable_Object = MibTable
mibcallSwitchingProfileTable = _MibcallSwitchingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 65, 1)
)
if mibBuilder.loadTexts:
    mibcallSwitchingProfileTable.setStatus("mandatory")
_MibcallSwitchingProfileEntry_Object = MibTableRow
mibcallSwitchingProfileEntry = _MibcallSwitchingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1)
)
mibcallSwitchingProfileEntry.setIndexNames(
    (0, "ASCEND-MIBCALLSW-MIB", "callSwitchingProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibcallSwitchingProfileEntry.setStatus("mandatory")
_CallSwitchingProfile_Index_o_Type = Integer32
_CallSwitchingProfile_Index_o_Object = MibScalar
callSwitchingProfile_Index_o = _CallSwitchingProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1, 1),
    _CallSwitchingProfile_Index_o_Type()
)
callSwitchingProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callSwitchingProfile_Index_o.setStatus("mandatory")


class _CallSwitchingProfile_Enabled_Type(Integer32):
    """Custom type callSwitchingProfile_Enabled based on Integer32"""
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


_CallSwitchingProfile_Enabled_Type.__name__ = "Integer32"
_CallSwitchingProfile_Enabled_Object = MibScalar
callSwitchingProfile_Enabled = _CallSwitchingProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1, 2),
    _CallSwitchingProfile_Enabled_Type()
)
callSwitchingProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callSwitchingProfile_Enabled.setStatus("mandatory")


class _CallSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable_Type(Integer32):
    """Custom type callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable based on Integer32"""
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


_CallSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable_Type.__name__ = "Integer32"
_CallSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable_Object = MibScalar
callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable = _CallSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1, 3),
    _CallSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable_Type()
)
callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable.setStatus("mandatory")


class _CallSwitchingProfile_Action_o_Type(Integer32):
    """Custom type callSwitchingProfile_Action_o based on Integer32"""
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


_CallSwitchingProfile_Action_o_Type.__name__ = "Integer32"
_CallSwitchingProfile_Action_o_Object = MibScalar
callSwitchingProfile_Action_o = _CallSwitchingProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1, 4),
    _CallSwitchingProfile_Action_o_Type()
)
callSwitchingProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callSwitchingProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBCALLSW-MIB",
    **{"DisplayString": DisplayString,
       "mibcallSwitchingProfile": mibcallSwitchingProfile,
       "mibcallSwitchingProfileTable": mibcallSwitchingProfileTable,
       "mibcallSwitchingProfileEntry": mibcallSwitchingProfileEntry,
       "callSwitchingProfile-Index-o": callSwitchingProfile_Index_o,
       "callSwitchingProfile-Enabled": callSwitchingProfile_Enabled,
       "callSwitchingProfile-ComparisonRule-CallRouteEmptyPhoneNumberAcceptable": callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable,
       "callSwitchingProfile-Action-o": callSwitchingProfile_Action_o}
)
