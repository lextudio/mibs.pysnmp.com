# SNMP MIB module (ASCEND-MIBVACM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBVACM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:31 2024
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

_MibvacmSecurityGroupProfile_ObjectIdentity = ObjectIdentity
mibvacmSecurityGroupProfile = _MibvacmSecurityGroupProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 135)
)
_MibvacmSecurityGroupProfileTable_Object = MibTable
mibvacmSecurityGroupProfileTable = _MibvacmSecurityGroupProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 135, 1)
)
if mibBuilder.loadTexts:
    mibvacmSecurityGroupProfileTable.setStatus("mandatory")
_MibvacmSecurityGroupProfileEntry_Object = MibTableRow
mibvacmSecurityGroupProfileEntry = _MibvacmSecurityGroupProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 135, 1, 1)
)
mibvacmSecurityGroupProfileEntry.setIndexNames(
    (0, "ASCEND-MIBVACM-MIB", "vacmSecurityGroupProfile-SecurityProperties-SecurityModel"),
    (0, "ASCEND-MIBVACM-MIB", "vacmSecurityGroupProfile-SecurityProperties-SecurityName"),
)
if mibBuilder.loadTexts:
    mibvacmSecurityGroupProfileEntry.setStatus("mandatory")
_VacmSecurityGroupProfile_SecurityProperties_SecurityModel_Type = Integer32
_VacmSecurityGroupProfile_SecurityProperties_SecurityModel_Object = MibScalar
vacmSecurityGroupProfile_SecurityProperties_SecurityModel = _VacmSecurityGroupProfile_SecurityProperties_SecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 135, 1, 1, 1),
    _VacmSecurityGroupProfile_SecurityProperties_SecurityModel_Type()
)
vacmSecurityGroupProfile_SecurityProperties_SecurityModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vacmSecurityGroupProfile_SecurityProperties_SecurityModel.setStatus("mandatory")
_VacmSecurityGroupProfile_SecurityProperties_SecurityName_Type = OctetString
_VacmSecurityGroupProfile_SecurityProperties_SecurityName_Object = MibScalar
vacmSecurityGroupProfile_SecurityProperties_SecurityName = _VacmSecurityGroupProfile_SecurityProperties_SecurityName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 135, 1, 1, 2),
    _VacmSecurityGroupProfile_SecurityProperties_SecurityName_Type()
)
vacmSecurityGroupProfile_SecurityProperties_SecurityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vacmSecurityGroupProfile_SecurityProperties_SecurityName.setStatus("mandatory")


class _VacmSecurityGroupProfile_Active_Type(Integer32):
    """Custom type vacmSecurityGroupProfile_Active based on Integer32"""
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


_VacmSecurityGroupProfile_Active_Type.__name__ = "Integer32"
_VacmSecurityGroupProfile_Active_Object = MibScalar
vacmSecurityGroupProfile_Active = _VacmSecurityGroupProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 135, 1, 1, 3),
    _VacmSecurityGroupProfile_Active_Type()
)
vacmSecurityGroupProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmSecurityGroupProfile_Active.setStatus("mandatory")
_VacmSecurityGroupProfile_GroupName_Type = OctetString
_VacmSecurityGroupProfile_GroupName_Object = MibScalar
vacmSecurityGroupProfile_GroupName = _VacmSecurityGroupProfile_GroupName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 135, 1, 1, 4),
    _VacmSecurityGroupProfile_GroupName_Type()
)
vacmSecurityGroupProfile_GroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmSecurityGroupProfile_GroupName.setStatus("mandatory")


class _VacmSecurityGroupProfile_Action_o_Type(Integer32):
    """Custom type vacmSecurityGroupProfile_Action_o based on Integer32"""
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


_VacmSecurityGroupProfile_Action_o_Type.__name__ = "Integer32"
_VacmSecurityGroupProfile_Action_o_Object = MibScalar
vacmSecurityGroupProfile_Action_o = _VacmSecurityGroupProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 135, 1, 1, 5),
    _VacmSecurityGroupProfile_Action_o_Type()
)
vacmSecurityGroupProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmSecurityGroupProfile_Action_o.setStatus("mandatory")
_MibvacmAccessProfile_ObjectIdentity = ObjectIdentity
mibvacmAccessProfile = _MibvacmAccessProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 136)
)
_MibvacmAccessProfileTable_Object = MibTable
mibvacmAccessProfileTable = _MibvacmAccessProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 136, 1)
)
if mibBuilder.loadTexts:
    mibvacmAccessProfileTable.setStatus("mandatory")
_MibvacmAccessProfileEntry_Object = MibTableRow
mibvacmAccessProfileEntry = _MibvacmAccessProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1)
)
mibvacmAccessProfileEntry.setIndexNames(
    (0, "ASCEND-MIBVACM-MIB", "vacmAccessProfile-AccessProperties-GroupName"),
    (0, "ASCEND-MIBVACM-MIB", "vacmAccessProfile-AccessProperties-ContextPrefix"),
    (0, "ASCEND-MIBVACM-MIB", "vacmAccessProfile-AccessProperties-SecurityModel"),
    (0, "ASCEND-MIBVACM-MIB", "vacmAccessProfile-AccessProperties-SecurityLevel"),
)
if mibBuilder.loadTexts:
    mibvacmAccessProfileEntry.setStatus("mandatory")
_VacmAccessProfile_AccessProperties_GroupName_Type = OctetString
_VacmAccessProfile_AccessProperties_GroupName_Object = MibScalar
vacmAccessProfile_AccessProperties_GroupName = _VacmAccessProfile_AccessProperties_GroupName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 1),
    _VacmAccessProfile_AccessProperties_GroupName_Type()
)
vacmAccessProfile_AccessProperties_GroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vacmAccessProfile_AccessProperties_GroupName.setStatus("mandatory")
_VacmAccessProfile_AccessProperties_ContextPrefix_Type = OctetString
_VacmAccessProfile_AccessProperties_ContextPrefix_Object = MibScalar
vacmAccessProfile_AccessProperties_ContextPrefix = _VacmAccessProfile_AccessProperties_ContextPrefix_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 2),
    _VacmAccessProfile_AccessProperties_ContextPrefix_Type()
)
vacmAccessProfile_AccessProperties_ContextPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vacmAccessProfile_AccessProperties_ContextPrefix.setStatus("mandatory")
_VacmAccessProfile_AccessProperties_SecurityModel_Type = Integer32
_VacmAccessProfile_AccessProperties_SecurityModel_Object = MibScalar
vacmAccessProfile_AccessProperties_SecurityModel = _VacmAccessProfile_AccessProperties_SecurityModel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 3),
    _VacmAccessProfile_AccessProperties_SecurityModel_Type()
)
vacmAccessProfile_AccessProperties_SecurityModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vacmAccessProfile_AccessProperties_SecurityModel.setStatus("mandatory")
_VacmAccessProfile_AccessProperties_SecurityLevel_Type = Integer32
_VacmAccessProfile_AccessProperties_SecurityLevel_Object = MibScalar
vacmAccessProfile_AccessProperties_SecurityLevel = _VacmAccessProfile_AccessProperties_SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 4),
    _VacmAccessProfile_AccessProperties_SecurityLevel_Type()
)
vacmAccessProfile_AccessProperties_SecurityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vacmAccessProfile_AccessProperties_SecurityLevel.setStatus("mandatory")


class _VacmAccessProfile_Active_Type(Integer32):
    """Custom type vacmAccessProfile_Active based on Integer32"""
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


_VacmAccessProfile_Active_Type.__name__ = "Integer32"
_VacmAccessProfile_Active_Object = MibScalar
vacmAccessProfile_Active = _VacmAccessProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 5),
    _VacmAccessProfile_Active_Type()
)
vacmAccessProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmAccessProfile_Active.setStatus("mandatory")


class _VacmAccessProfile_MatchMethod_Type(Integer32):
    """Custom type vacmAccessProfile_MatchMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exactMatch", 2),
          ("prefixMatch", 3))
    )


_VacmAccessProfile_MatchMethod_Type.__name__ = "Integer32"
_VacmAccessProfile_MatchMethod_Object = MibScalar
vacmAccessProfile_MatchMethod = _VacmAccessProfile_MatchMethod_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 6),
    _VacmAccessProfile_MatchMethod_Type()
)
vacmAccessProfile_MatchMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmAccessProfile_MatchMethod.setStatus("mandatory")
_VacmAccessProfile_ReadViewName_Type = OctetString
_VacmAccessProfile_ReadViewName_Object = MibScalar
vacmAccessProfile_ReadViewName = _VacmAccessProfile_ReadViewName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 7),
    _VacmAccessProfile_ReadViewName_Type()
)
vacmAccessProfile_ReadViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmAccessProfile_ReadViewName.setStatus("mandatory")
_VacmAccessProfile_WriteViewName_Type = OctetString
_VacmAccessProfile_WriteViewName_Object = MibScalar
vacmAccessProfile_WriteViewName = _VacmAccessProfile_WriteViewName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 8),
    _VacmAccessProfile_WriteViewName_Type()
)
vacmAccessProfile_WriteViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmAccessProfile_WriteViewName.setStatus("mandatory")
_VacmAccessProfile_NotifyViewName_Type = OctetString
_VacmAccessProfile_NotifyViewName_Object = MibScalar
vacmAccessProfile_NotifyViewName = _VacmAccessProfile_NotifyViewName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 9),
    _VacmAccessProfile_NotifyViewName_Type()
)
vacmAccessProfile_NotifyViewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmAccessProfile_NotifyViewName.setStatus("mandatory")


class _VacmAccessProfile_Action_o_Type(Integer32):
    """Custom type vacmAccessProfile_Action_o based on Integer32"""
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


_VacmAccessProfile_Action_o_Type.__name__ = "Integer32"
_VacmAccessProfile_Action_o_Object = MibScalar
vacmAccessProfile_Action_o = _VacmAccessProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 136, 1, 1, 10),
    _VacmAccessProfile_Action_o_Type()
)
vacmAccessProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmAccessProfile_Action_o.setStatus("mandatory")
_MibvacmViewTreeProfile_ObjectIdentity = ObjectIdentity
mibvacmViewTreeProfile = _MibvacmViewTreeProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 137)
)
_MibvacmViewTreeProfileTable_Object = MibTable
mibvacmViewTreeProfileTable = _MibvacmViewTreeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 137, 1)
)
if mibBuilder.loadTexts:
    mibvacmViewTreeProfileTable.setStatus("mandatory")
_MibvacmViewTreeProfileEntry_Object = MibTableRow
mibvacmViewTreeProfileEntry = _MibvacmViewTreeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1)
)
mibvacmViewTreeProfileEntry.setIndexNames(
    (0, "ASCEND-MIBVACM-MIB", "vacmViewTreeProfile-TreeProperties-ViewName"),
    (0, "ASCEND-MIBVACM-MIB", "vacmViewTreeProfile-TreeProperties-ViewTreeOid"),
)
if mibBuilder.loadTexts:
    mibvacmViewTreeProfileEntry.setStatus("mandatory")
_VacmViewTreeProfile_TreeProperties_ViewName_Type = OctetString
_VacmViewTreeProfile_TreeProperties_ViewName_Object = MibScalar
vacmViewTreeProfile_TreeProperties_ViewName = _VacmViewTreeProfile_TreeProperties_ViewName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1, 1),
    _VacmViewTreeProfile_TreeProperties_ViewName_Type()
)
vacmViewTreeProfile_TreeProperties_ViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vacmViewTreeProfile_TreeProperties_ViewName.setStatus("mandatory")
_VacmViewTreeProfile_TreeProperties_ViewTreeOid_Type = DisplayString
_VacmViewTreeProfile_TreeProperties_ViewTreeOid_Object = MibScalar
vacmViewTreeProfile_TreeProperties_ViewTreeOid = _VacmViewTreeProfile_TreeProperties_ViewTreeOid_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1, 2),
    _VacmViewTreeProfile_TreeProperties_ViewTreeOid_Type()
)
vacmViewTreeProfile_TreeProperties_ViewTreeOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vacmViewTreeProfile_TreeProperties_ViewTreeOid.setStatus("mandatory")


class _VacmViewTreeProfile_Active_Type(Integer32):
    """Custom type vacmViewTreeProfile_Active based on Integer32"""
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


_VacmViewTreeProfile_Active_Type.__name__ = "Integer32"
_VacmViewTreeProfile_Active_Object = MibScalar
vacmViewTreeProfile_Active = _VacmViewTreeProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1, 3),
    _VacmViewTreeProfile_Active_Type()
)
vacmViewTreeProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmViewTreeProfile_Active.setStatus("mandatory")
_VacmViewTreeProfile_TreeOidMask_Type = DisplayString
_VacmViewTreeProfile_TreeOidMask_Object = MibScalar
vacmViewTreeProfile_TreeOidMask = _VacmViewTreeProfile_TreeOidMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1, 4),
    _VacmViewTreeProfile_TreeOidMask_Type()
)
vacmViewTreeProfile_TreeOidMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmViewTreeProfile_TreeOidMask.setStatus("mandatory")


class _VacmViewTreeProfile_TreeType_Type(Integer32):
    """Custom type vacmViewTreeProfile_TreeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("excluded", 3),
          ("included", 2))
    )


_VacmViewTreeProfile_TreeType_Type.__name__ = "Integer32"
_VacmViewTreeProfile_TreeType_Object = MibScalar
vacmViewTreeProfile_TreeType = _VacmViewTreeProfile_TreeType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1, 5),
    _VacmViewTreeProfile_TreeType_Type()
)
vacmViewTreeProfile_TreeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmViewTreeProfile_TreeType.setStatus("mandatory")


class _VacmViewTreeProfile_Action_o_Type(Integer32):
    """Custom type vacmViewTreeProfile_Action_o based on Integer32"""
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


_VacmViewTreeProfile_Action_o_Type.__name__ = "Integer32"
_VacmViewTreeProfile_Action_o_Object = MibScalar
vacmViewTreeProfile_Action_o = _VacmViewTreeProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 137, 1, 1, 6),
    _VacmViewTreeProfile_Action_o_Type()
)
vacmViewTreeProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vacmViewTreeProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBVACM-MIB",
    **{"DisplayString": DisplayString,
       "mibvacmSecurityGroupProfile": mibvacmSecurityGroupProfile,
       "mibvacmSecurityGroupProfileTable": mibvacmSecurityGroupProfileTable,
       "mibvacmSecurityGroupProfileEntry": mibvacmSecurityGroupProfileEntry,
       "vacmSecurityGroupProfile-SecurityProperties-SecurityModel": vacmSecurityGroupProfile_SecurityProperties_SecurityModel,
       "vacmSecurityGroupProfile-SecurityProperties-SecurityName": vacmSecurityGroupProfile_SecurityProperties_SecurityName,
       "vacmSecurityGroupProfile-Active": vacmSecurityGroupProfile_Active,
       "vacmSecurityGroupProfile-GroupName": vacmSecurityGroupProfile_GroupName,
       "vacmSecurityGroupProfile-Action-o": vacmSecurityGroupProfile_Action_o,
       "mibvacmAccessProfile": mibvacmAccessProfile,
       "mibvacmAccessProfileTable": mibvacmAccessProfileTable,
       "mibvacmAccessProfileEntry": mibvacmAccessProfileEntry,
       "vacmAccessProfile-AccessProperties-GroupName": vacmAccessProfile_AccessProperties_GroupName,
       "vacmAccessProfile-AccessProperties-ContextPrefix": vacmAccessProfile_AccessProperties_ContextPrefix,
       "vacmAccessProfile-AccessProperties-SecurityModel": vacmAccessProfile_AccessProperties_SecurityModel,
       "vacmAccessProfile-AccessProperties-SecurityLevel": vacmAccessProfile_AccessProperties_SecurityLevel,
       "vacmAccessProfile-Active": vacmAccessProfile_Active,
       "vacmAccessProfile-MatchMethod": vacmAccessProfile_MatchMethod,
       "vacmAccessProfile-ReadViewName": vacmAccessProfile_ReadViewName,
       "vacmAccessProfile-WriteViewName": vacmAccessProfile_WriteViewName,
       "vacmAccessProfile-NotifyViewName": vacmAccessProfile_NotifyViewName,
       "vacmAccessProfile-Action-o": vacmAccessProfile_Action_o,
       "mibvacmViewTreeProfile": mibvacmViewTreeProfile,
       "mibvacmViewTreeProfileTable": mibvacmViewTreeProfileTable,
       "mibvacmViewTreeProfileEntry": mibvacmViewTreeProfileEntry,
       "vacmViewTreeProfile-TreeProperties-ViewName": vacmViewTreeProfile_TreeProperties_ViewName,
       "vacmViewTreeProfile-TreeProperties-ViewTreeOid": vacmViewTreeProfile_TreeProperties_ViewTreeOid,
       "vacmViewTreeProfile-Active": vacmViewTreeProfile_Active,
       "vacmViewTreeProfile-TreeOidMask": vacmViewTreeProfile_TreeOidMask,
       "vacmViewTreeProfile-TreeType": vacmViewTreeProfile_TreeType,
       "vacmViewTreeProfile-Action-o": vacmViewTreeProfile_Action_o}
)
