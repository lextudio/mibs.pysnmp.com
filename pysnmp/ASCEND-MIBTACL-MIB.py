# SNMP MIB module (ASCEND-MIBTACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBTACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:25 2024
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

_MibtaclProfile_ObjectIdentity = ObjectIdentity
mibtaclProfile = _MibtaclProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 128)
)
_MibtaclProfileTable_Object = MibTable
mibtaclProfileTable = _MibtaclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 128, 1)
)
if mibBuilder.loadTexts:
    mibtaclProfileTable.setStatus("mandatory")
_MibtaclProfileEntry_Object = MibTableRow
mibtaclProfileEntry = _MibtaclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 128, 1, 1)
)
mibtaclProfileEntry.setIndexNames(
    (0, "ASCEND-MIBTACL-MIB", "taclProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibtaclProfileEntry.setStatus("mandatory")
_TaclProfile_Index_o_Type = Integer32
_TaclProfile_Index_o_Object = MibScalar
taclProfile_Index_o = _TaclProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 128, 1, 1, 1),
    _TaclProfile_Index_o_Type()
)
taclProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taclProfile_Index_o.setStatus("mandatory")


class _TaclProfile_EnablePermit_Type(Integer32):
    """Custom type taclProfile_EnablePermit based on Integer32"""
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


_TaclProfile_EnablePermit_Type.__name__ = "Integer32"
_TaclProfile_EnablePermit_Object = MibScalar
taclProfile_EnablePermit = _TaclProfile_EnablePermit_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 128, 1, 1, 2),
    _TaclProfile_EnablePermit_Type()
)
taclProfile_EnablePermit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taclProfile_EnablePermit.setStatus("mandatory")


class _TaclProfile_Action_o_Type(Integer32):
    """Custom type taclProfile_Action_o based on Integer32"""
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


_TaclProfile_Action_o_Type.__name__ = "Integer32"
_TaclProfile_Action_o_Object = MibScalar
taclProfile_Action_o = _TaclProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 128, 1, 1, 3),
    _TaclProfile_Action_o_Type()
)
taclProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taclProfile_Action_o.setStatus("mandatory")
_MibtaclProfile_PermitListTable_Object = MibTable
mibtaclProfile_PermitListTable = _MibtaclProfile_PermitListTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 128, 2)
)
if mibBuilder.loadTexts:
    mibtaclProfile_PermitListTable.setStatus("mandatory")
_MibtaclProfile_PermitListEntry_Object = MibTableRow
mibtaclProfile_PermitListEntry = _MibtaclProfile_PermitListEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1)
)
mibtaclProfile_PermitListEntry.setIndexNames(
    (0, "ASCEND-MIBTACL-MIB", "taclProfile-PermitList-Index-o"),
    (0, "ASCEND-MIBTACL-MIB", "taclProfile-PermitList-Index1-o"),
)
if mibBuilder.loadTexts:
    mibtaclProfile_PermitListEntry.setStatus("mandatory")
_TaclProfile_PermitList_Index_o_Type = Integer32
_TaclProfile_PermitList_Index_o_Object = MibScalar
taclProfile_PermitList_Index_o = _TaclProfile_PermitList_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 1),
    _TaclProfile_PermitList_Index_o_Type()
)
taclProfile_PermitList_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taclProfile_PermitList_Index_o.setStatus("mandatory")
_TaclProfile_PermitList_Index1_o_Type = Integer32
_TaclProfile_PermitList_Index1_o_Object = MibScalar
taclProfile_PermitList_Index1_o = _TaclProfile_PermitList_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 2),
    _TaclProfile_PermitList_Index1_o_Type()
)
taclProfile_PermitList_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taclProfile_PermitList_Index1_o.setStatus("mandatory")


class _TaclProfile_PermitList_ValidEntry_Type(Integer32):
    """Custom type taclProfile_PermitList_ValidEntry based on Integer32"""
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


_TaclProfile_PermitList_ValidEntry_Type.__name__ = "Integer32"
_TaclProfile_PermitList_ValidEntry_Object = MibScalar
taclProfile_PermitList_ValidEntry = _TaclProfile_PermitList_ValidEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 3),
    _TaclProfile_PermitList_ValidEntry_Type()
)
taclProfile_PermitList_ValidEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taclProfile_PermitList_ValidEntry.setStatus("mandatory")
_TaclProfile_PermitList_SourceAddress_Type = IpAddress
_TaclProfile_PermitList_SourceAddress_Object = MibScalar
taclProfile_PermitList_SourceAddress = _TaclProfile_PermitList_SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 4),
    _TaclProfile_PermitList_SourceAddress_Type()
)
taclProfile_PermitList_SourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taclProfile_PermitList_SourceAddress.setStatus("mandatory")
_TaclProfile_PermitList_SourceAddressMask_Type = IpAddress
_TaclProfile_PermitList_SourceAddressMask_Object = MibScalar
taclProfile_PermitList_SourceAddressMask = _TaclProfile_PermitList_SourceAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 128, 2, 1, 5),
    _TaclProfile_PermitList_SourceAddressMask_Type()
)
taclProfile_PermitList_SourceAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taclProfile_PermitList_SourceAddressMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBTACL-MIB",
    **{"DisplayString": DisplayString,
       "mibtaclProfile": mibtaclProfile,
       "mibtaclProfileTable": mibtaclProfileTable,
       "mibtaclProfileEntry": mibtaclProfileEntry,
       "taclProfile-Index-o": taclProfile_Index_o,
       "taclProfile-EnablePermit": taclProfile_EnablePermit,
       "taclProfile-Action-o": taclProfile_Action_o,
       "mibtaclProfile-PermitListTable": mibtaclProfile_PermitListTable,
       "mibtaclProfile-PermitListEntry": mibtaclProfile_PermitListEntry,
       "taclProfile-PermitList-Index-o": taclProfile_PermitList_Index_o,
       "taclProfile-PermitList-Index1-o": taclProfile_PermitList_Index1_o,
       "taclProfile-PermitList-ValidEntry": taclProfile_PermitList_ValidEntry,
       "taclProfile-PermitList-SourceAddress": taclProfile_PermitList_SourceAddress,
       "taclProfile-PermitList-SourceAddressMask": taclProfile_PermitList_SourceAddressMask}
)
