# SNMP MIB module (ASCEND-MIBUSER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBUSER-MIB
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

_MibuserProfile_ObjectIdentity = ObjectIdentity
mibuserProfile = _MibuserProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 134)
)
_MibuserProfileTable_Object = MibTable
mibuserProfileTable = _MibuserProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1)
)
if mibBuilder.loadTexts:
    mibuserProfileTable.setStatus("mandatory")
_MibuserProfileEntry_Object = MibTableRow
mibuserProfileEntry = _MibuserProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1)
)
mibuserProfileEntry.setIndexNames(
    (0, "ASCEND-MIBUSER-MIB", "userProfile-Name"),
)
if mibBuilder.loadTexts:
    mibuserProfileEntry.setStatus("mandatory")
_UserProfile_Name_Type = DisplayString
_UserProfile_Name_Object = MibScalar
userProfile_Name = _UserProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 1),
    _UserProfile_Name_Type()
)
userProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userProfile_Name.setStatus("mandatory")
_UserProfile_Password_Type = DisplayString
_UserProfile_Password_Object = MibScalar
userProfile_Password = _UserProfile_Password_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 2),
    _UserProfile_Password_Type()
)
userProfile_Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_Password.setStatus("mandatory")


class _UserProfile_ActiveEnabled_Type(Integer32):
    """Custom type userProfile_ActiveEnabled based on Integer32"""
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


_UserProfile_ActiveEnabled_Type.__name__ = "Integer32"
_UserProfile_ActiveEnabled_Object = MibScalar
userProfile_ActiveEnabled = _UserProfile_ActiveEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 3),
    _UserProfile_ActiveEnabled_Type()
)
userProfile_ActiveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_ActiveEnabled.setStatus("mandatory")


class _UserProfile_AllowTermserv_Type(Integer32):
    """Custom type userProfile_AllowTermserv based on Integer32"""
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


_UserProfile_AllowTermserv_Type.__name__ = "Integer32"
_UserProfile_AllowTermserv_Object = MibScalar
userProfile_AllowTermserv = _UserProfile_AllowTermserv_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 4),
    _UserProfile_AllowTermserv_Type()
)
userProfile_AllowTermserv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_AllowTermserv.setStatus("mandatory")


class _UserProfile_AllowSystem_Type(Integer32):
    """Custom type userProfile_AllowSystem based on Integer32"""
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


_UserProfile_AllowSystem_Type.__name__ = "Integer32"
_UserProfile_AllowSystem_Object = MibScalar
userProfile_AllowSystem = _UserProfile_AllowSystem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 5),
    _UserProfile_AllowSystem_Type()
)
userProfile_AllowSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_AllowSystem.setStatus("mandatory")


class _UserProfile_AllowDiagnostic_Type(Integer32):
    """Custom type userProfile_AllowDiagnostic based on Integer32"""
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


_UserProfile_AllowDiagnostic_Type.__name__ = "Integer32"
_UserProfile_AllowDiagnostic_Object = MibScalar
userProfile_AllowDiagnostic = _UserProfile_AllowDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 6),
    _UserProfile_AllowDiagnostic_Type()
)
userProfile_AllowDiagnostic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_AllowDiagnostic.setStatus("mandatory")


class _UserProfile_AllowUpdate_Type(Integer32):
    """Custom type userProfile_AllowUpdate based on Integer32"""
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


_UserProfile_AllowUpdate_Type.__name__ = "Integer32"
_UserProfile_AllowUpdate_Object = MibScalar
userProfile_AllowUpdate = _UserProfile_AllowUpdate_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 7),
    _UserProfile_AllowUpdate_Type()
)
userProfile_AllowUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_AllowUpdate.setStatus("mandatory")


class _UserProfile_AllowPassword_Type(Integer32):
    """Custom type userProfile_AllowPassword based on Integer32"""
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


_UserProfile_AllowPassword_Type.__name__ = "Integer32"
_UserProfile_AllowPassword_Object = MibScalar
userProfile_AllowPassword = _UserProfile_AllowPassword_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 8),
    _UserProfile_AllowPassword_Type()
)
userProfile_AllowPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_AllowPassword.setStatus("mandatory")


class _UserProfile_AllowCode_Type(Integer32):
    """Custom type userProfile_AllowCode based on Integer32"""
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


_UserProfile_AllowCode_Type.__name__ = "Integer32"
_UserProfile_AllowCode_Object = MibScalar
userProfile_AllowCode = _UserProfile_AllowCode_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 9),
    _UserProfile_AllowCode_Type()
)
userProfile_AllowCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_AllowCode.setStatus("mandatory")
_UserProfile_IdleLogout_Type = Integer32
_UserProfile_IdleLogout_Object = MibScalar
userProfile_IdleLogout = _UserProfile_IdleLogout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 10),
    _UserProfile_IdleLogout_Type()
)
userProfile_IdleLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_IdleLogout.setStatus("mandatory")
_UserProfile_Prompt_Type = DisplayString
_UserProfile_Prompt_Object = MibScalar
userProfile_Prompt = _UserProfile_Prompt_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 11),
    _UserProfile_Prompt_Type()
)
userProfile_Prompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_Prompt.setStatus("mandatory")


class _UserProfile_DefaultStatus_Type(Integer32):
    """Custom type userProfile_DefaultStatus based on Integer32"""
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


_UserProfile_DefaultStatus_Type.__name__ = "Integer32"
_UserProfile_DefaultStatus_Object = MibScalar
userProfile_DefaultStatus = _UserProfile_DefaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 12),
    _UserProfile_DefaultStatus_Type()
)
userProfile_DefaultStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_DefaultStatus.setStatus("mandatory")


class _UserProfile_TopStatus_Type(Integer32):
    """Custom type userProfile_TopStatus based on Integer32"""
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
        *(("atmvccStatus", 4),
          ("generalInfo", 1),
          ("lineStatus", 3),
          ("logWindow", 2))
    )


_UserProfile_TopStatus_Type.__name__ = "Integer32"
_UserProfile_TopStatus_Object = MibScalar
userProfile_TopStatus = _UserProfile_TopStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 13),
    _UserProfile_TopStatus_Type()
)
userProfile_TopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_TopStatus.setStatus("mandatory")


class _UserProfile_BottomStatus_Type(Integer32):
    """Custom type userProfile_BottomStatus based on Integer32"""
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
        *(("atmvccStatus", 4),
          ("generalInfo", 1),
          ("lineStatus", 3),
          ("logWindow", 2))
    )


_UserProfile_BottomStatus_Type.__name__ = "Integer32"
_UserProfile_BottomStatus_Object = MibScalar
userProfile_BottomStatus = _UserProfile_BottomStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 14),
    _UserProfile_BottomStatus_Type()
)
userProfile_BottomStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_BottomStatus.setStatus("mandatory")


class _UserProfile_LeftStatus_Type(Integer32):
    """Custom type userProfile_LeftStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("callstatsList", 3),
          ("connectionList", 2),
          ("sessionList", 1))
    )


_UserProfile_LeftStatus_Type.__name__ = "Integer32"
_UserProfile_LeftStatus_Object = MibScalar
userProfile_LeftStatus = _UserProfile_LeftStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 15),
    _UserProfile_LeftStatus_Type()
)
userProfile_LeftStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_LeftStatus.setStatus("mandatory")
_UserProfile_ScreenWidth_Type = Integer32
_UserProfile_ScreenWidth_Object = MibScalar
userProfile_ScreenWidth = _UserProfile_ScreenWidth_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 16),
    _UserProfile_ScreenWidth_Type()
)
userProfile_ScreenWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_ScreenWidth.setStatus("mandatory")
_UserProfile_ScreenLength_Type = Integer32
_UserProfile_ScreenLength_Object = MibScalar
userProfile_ScreenLength = _UserProfile_ScreenLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 17),
    _UserProfile_ScreenLength_Type()
)
userProfile_ScreenLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_ScreenLength.setStatus("mandatory")
_UserProfile_StatusLength_Type = Integer32
_UserProfile_StatusLength_Object = MibScalar
userProfile_StatusLength = _UserProfile_StatusLength_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 18),
    _UserProfile_StatusLength_Type()
)
userProfile_StatusLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_StatusLength.setStatus("mandatory")


class _UserProfile_UseScrollRegions_Type(Integer32):
    """Custom type userProfile_UseScrollRegions based on Integer32"""
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


_UserProfile_UseScrollRegions_Type.__name__ = "Integer32"
_UserProfile_UseScrollRegions_Object = MibScalar
userProfile_UseScrollRegions = _UserProfile_UseScrollRegions_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 19),
    _UserProfile_UseScrollRegions_Type()
)
userProfile_UseScrollRegions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_UseScrollRegions.setStatus("mandatory")


class _UserProfile_LogDisplayLevel_Type(Integer32):
    """Custom type userProfile_LogDisplayLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("alert", 3),
          ("critical", 4),
          ("debug", 9),
          ("emergency", 2),
          ("error", 5),
          ("info", 8),
          ("none", 1),
          ("notice", 7),
          ("warning", 6))
    )


_UserProfile_LogDisplayLevel_Type.__name__ = "Integer32"
_UserProfile_LogDisplayLevel_Object = MibScalar
userProfile_LogDisplayLevel = _UserProfile_LogDisplayLevel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 20),
    _UserProfile_LogDisplayLevel_Type()
)
userProfile_LogDisplayLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_LogDisplayLevel.setStatus("mandatory")


class _UserProfile_Action_o_Type(Integer32):
    """Custom type userProfile_Action_o based on Integer32"""
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


_UserProfile_Action_o_Type.__name__ = "Integer32"
_UserProfile_Action_o_Object = MibScalar
userProfile_Action_o = _UserProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 134, 1, 1, 21),
    _UserProfile_Action_o_Type()
)
userProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBUSER-MIB",
    **{"DisplayString": DisplayString,
       "mibuserProfile": mibuserProfile,
       "mibuserProfileTable": mibuserProfileTable,
       "mibuserProfileEntry": mibuserProfileEntry,
       "userProfile-Name": userProfile_Name,
       "userProfile-Password": userProfile_Password,
       "userProfile-ActiveEnabled": userProfile_ActiveEnabled,
       "userProfile-AllowTermserv": userProfile_AllowTermserv,
       "userProfile-AllowSystem": userProfile_AllowSystem,
       "userProfile-AllowDiagnostic": userProfile_AllowDiagnostic,
       "userProfile-AllowUpdate": userProfile_AllowUpdate,
       "userProfile-AllowPassword": userProfile_AllowPassword,
       "userProfile-AllowCode": userProfile_AllowCode,
       "userProfile-IdleLogout": userProfile_IdleLogout,
       "userProfile-Prompt": userProfile_Prompt,
       "userProfile-DefaultStatus": userProfile_DefaultStatus,
       "userProfile-TopStatus": userProfile_TopStatus,
       "userProfile-BottomStatus": userProfile_BottomStatus,
       "userProfile-LeftStatus": userProfile_LeftStatus,
       "userProfile-ScreenWidth": userProfile_ScreenWidth,
       "userProfile-ScreenLength": userProfile_ScreenLength,
       "userProfile-StatusLength": userProfile_StatusLength,
       "userProfile-UseScrollRegions": userProfile_UseScrollRegions,
       "userProfile-LogDisplayLevel": userProfile_LogDisplayLevel,
       "userProfile-Action-o": userProfile_Action_o}
)
