# SNMP MIB module (ASCEND-MIBSCRTY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSCRTY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:09 2024
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

_MibsecurityProfile_ObjectIdentity = ObjectIdentity
mibsecurityProfile = _MibsecurityProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 107)
)
_MibsecurityProfileTable_Object = MibTable
mibsecurityProfileTable = _MibsecurityProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1)
)
if mibBuilder.loadTexts:
    mibsecurityProfileTable.setStatus("mandatory")
_MibsecurityProfileEntry_Object = MibTableRow
mibsecurityProfileEntry = _MibsecurityProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1)
)
mibsecurityProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSCRTY-MIB", "securityProfile-Name"),
)
if mibBuilder.loadTexts:
    mibsecurityProfileEntry.setStatus("mandatory")
_SecurityProfile_Name_Type = DisplayString
_SecurityProfile_Name_Object = MibScalar
securityProfile_Name = _SecurityProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 1),
    _SecurityProfile_Name_Type()
)
securityProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityProfile_Name.setStatus("mandatory")
_SecurityProfile_Password_Type = DisplayString
_SecurityProfile_Password_Object = MibScalar
securityProfile_Password = _SecurityProfile_Password_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 2),
    _SecurityProfile_Password_Type()
)
securityProfile_Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_Password.setStatus("mandatory")


class _SecurityProfile_Operations_Type(Integer32):
    """Custom type securityProfile_Operations based on Integer32"""
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


_SecurityProfile_Operations_Type.__name__ = "Integer32"
_SecurityProfile_Operations_Object = MibScalar
securityProfile_Operations = _SecurityProfile_Operations_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 3),
    _SecurityProfile_Operations_Type()
)
securityProfile_Operations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_Operations.setStatus("mandatory")


class _SecurityProfile_EditSecurity_Type(Integer32):
    """Custom type securityProfile_EditSecurity based on Integer32"""
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


_SecurityProfile_EditSecurity_Type.__name__ = "Integer32"
_SecurityProfile_EditSecurity_Object = MibScalar
securityProfile_EditSecurity = _SecurityProfile_EditSecurity_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 4),
    _SecurityProfile_EditSecurity_Type()
)
securityProfile_EditSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_EditSecurity.setStatus("mandatory")


class _SecurityProfile_EditSystem_Type(Integer32):
    """Custom type securityProfile_EditSystem based on Integer32"""
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


_SecurityProfile_EditSystem_Type.__name__ = "Integer32"
_SecurityProfile_EditSystem_Object = MibScalar
securityProfile_EditSystem = _SecurityProfile_EditSystem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 5),
    _SecurityProfile_EditSystem_Type()
)
securityProfile_EditSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_EditSystem.setStatus("mandatory")


class _SecurityProfile_EditLine_Type(Integer32):
    """Custom type securityProfile_EditLine based on Integer32"""
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


_SecurityProfile_EditLine_Type.__name__ = "Integer32"
_SecurityProfile_EditLine_Object = MibScalar
securityProfile_EditLine = _SecurityProfile_EditLine_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 6),
    _SecurityProfile_EditLine_Type()
)
securityProfile_EditLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_EditLine.setStatus("mandatory")


class _SecurityProfile_EditOwnPort_Type(Integer32):
    """Custom type securityProfile_EditOwnPort based on Integer32"""
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


_SecurityProfile_EditOwnPort_Type.__name__ = "Integer32"
_SecurityProfile_EditOwnPort_Object = MibScalar
securityProfile_EditOwnPort = _SecurityProfile_EditOwnPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 7),
    _SecurityProfile_EditOwnPort_Type()
)
securityProfile_EditOwnPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_EditOwnPort.setStatus("mandatory")


class _SecurityProfile_EditAllPort_Type(Integer32):
    """Custom type securityProfile_EditAllPort based on Integer32"""
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


_SecurityProfile_EditAllPort_Type.__name__ = "Integer32"
_SecurityProfile_EditAllPort_Object = MibScalar
securityProfile_EditAllPort = _SecurityProfile_EditAllPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 8),
    _SecurityProfile_EditAllPort_Type()
)
securityProfile_EditAllPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_EditAllPort.setStatus("mandatory")


class _SecurityProfile_EditCurCall_Type(Integer32):
    """Custom type securityProfile_EditCurCall based on Integer32"""
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


_SecurityProfile_EditCurCall_Type.__name__ = "Integer32"
_SecurityProfile_EditCurCall_Object = MibScalar
securityProfile_EditCurCall = _SecurityProfile_EditCurCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 9),
    _SecurityProfile_EditCurCall_Type()
)
securityProfile_EditCurCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_EditCurCall.setStatus("mandatory")


class _SecurityProfile_EditOwnCall_Type(Integer32):
    """Custom type securityProfile_EditOwnCall based on Integer32"""
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


_SecurityProfile_EditOwnCall_Type.__name__ = "Integer32"
_SecurityProfile_EditOwnCall_Object = MibScalar
securityProfile_EditOwnCall = _SecurityProfile_EditOwnCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 10),
    _SecurityProfile_EditOwnCall_Type()
)
securityProfile_EditOwnCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_EditOwnCall.setStatus("mandatory")


class _SecurityProfile_EditComCall_Type(Integer32):
    """Custom type securityProfile_EditComCall based on Integer32"""
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


_SecurityProfile_EditComCall_Type.__name__ = "Integer32"
_SecurityProfile_EditComCall_Object = MibScalar
securityProfile_EditComCall = _SecurityProfile_EditComCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 11),
    _SecurityProfile_EditComCall_Type()
)
securityProfile_EditComCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_EditComCall.setStatus("mandatory")


class _SecurityProfile_EditAllCall_Type(Integer32):
    """Custom type securityProfile_EditAllCall based on Integer32"""
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


_SecurityProfile_EditAllCall_Type.__name__ = "Integer32"
_SecurityProfile_EditAllCall_Object = MibScalar
securityProfile_EditAllCall = _SecurityProfile_EditAllCall_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 12),
    _SecurityProfile_EditAllCall_Type()
)
securityProfile_EditAllCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_EditAllCall.setStatus("mandatory")


class _SecurityProfile_SysDiag_Type(Integer32):
    """Custom type securityProfile_SysDiag based on Integer32"""
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


_SecurityProfile_SysDiag_Type.__name__ = "Integer32"
_SecurityProfile_SysDiag_Object = MibScalar
securityProfile_SysDiag = _SecurityProfile_SysDiag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 13),
    _SecurityProfile_SysDiag_Type()
)
securityProfile_SysDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_SysDiag.setStatus("mandatory")


class _SecurityProfile_OwnPortDiag_Type(Integer32):
    """Custom type securityProfile_OwnPortDiag based on Integer32"""
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


_SecurityProfile_OwnPortDiag_Type.__name__ = "Integer32"
_SecurityProfile_OwnPortDiag_Object = MibScalar
securityProfile_OwnPortDiag = _SecurityProfile_OwnPortDiag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 14),
    _SecurityProfile_OwnPortDiag_Type()
)
securityProfile_OwnPortDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_OwnPortDiag.setStatus("mandatory")


class _SecurityProfile_AllPortDiag_Type(Integer32):
    """Custom type securityProfile_AllPortDiag based on Integer32"""
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


_SecurityProfile_AllPortDiag_Type.__name__ = "Integer32"
_SecurityProfile_AllPortDiag_Object = MibScalar
securityProfile_AllPortDiag = _SecurityProfile_AllPortDiag_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 15),
    _SecurityProfile_AllPortDiag_Type()
)
securityProfile_AllPortDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_AllPortDiag.setStatus("mandatory")


class _SecurityProfile_Download_Type(Integer32):
    """Custom type securityProfile_Download based on Integer32"""
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


_SecurityProfile_Download_Type.__name__ = "Integer32"
_SecurityProfile_Download_Object = MibScalar
securityProfile_Download = _SecurityProfile_Download_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 16),
    _SecurityProfile_Download_Type()
)
securityProfile_Download.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_Download.setStatus("mandatory")


class _SecurityProfile_Upload_Type(Integer32):
    """Custom type securityProfile_Upload based on Integer32"""
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


_SecurityProfile_Upload_Type.__name__ = "Integer32"
_SecurityProfile_Upload_Object = MibScalar
securityProfile_Upload = _SecurityProfile_Upload_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 17),
    _SecurityProfile_Upload_Type()
)
securityProfile_Upload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_Upload.setStatus("mandatory")


class _SecurityProfile_FieldService_Type(Integer32):
    """Custom type securityProfile_FieldService based on Integer32"""
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


_SecurityProfile_FieldService_Type.__name__ = "Integer32"
_SecurityProfile_FieldService_Object = MibScalar
securityProfile_FieldService = _SecurityProfile_FieldService_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 18),
    _SecurityProfile_FieldService_Type()
)
securityProfile_FieldService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_FieldService.setStatus("mandatory")


class _SecurityProfile_UseTacacsPlus_Type(Integer32):
    """Custom type securityProfile_UseTacacsPlus based on Integer32"""
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


_SecurityProfile_UseTacacsPlus_Type.__name__ = "Integer32"
_SecurityProfile_UseTacacsPlus_Object = MibScalar
securityProfile_UseTacacsPlus = _SecurityProfile_UseTacacsPlus_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 19),
    _SecurityProfile_UseTacacsPlus_Type()
)
securityProfile_UseTacacsPlus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_UseTacacsPlus.setStatus("mandatory")


class _SecurityProfile_Action_o_Type(Integer32):
    """Custom type securityProfile_Action_o based on Integer32"""
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


_SecurityProfile_Action_o_Type.__name__ = "Integer32"
_SecurityProfile_Action_o_Object = MibScalar
securityProfile_Action_o = _SecurityProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 20),
    _SecurityProfile_Action_o_Type()
)
securityProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSCRTY-MIB",
    **{"DisplayString": DisplayString,
       "mibsecurityProfile": mibsecurityProfile,
       "mibsecurityProfileTable": mibsecurityProfileTable,
       "mibsecurityProfileEntry": mibsecurityProfileEntry,
       "securityProfile-Name": securityProfile_Name,
       "securityProfile-Password": securityProfile_Password,
       "securityProfile-Operations": securityProfile_Operations,
       "securityProfile-EditSecurity": securityProfile_EditSecurity,
       "securityProfile-EditSystem": securityProfile_EditSystem,
       "securityProfile-EditLine": securityProfile_EditLine,
       "securityProfile-EditOwnPort": securityProfile_EditOwnPort,
       "securityProfile-EditAllPort": securityProfile_EditAllPort,
       "securityProfile-EditCurCall": securityProfile_EditCurCall,
       "securityProfile-EditOwnCall": securityProfile_EditOwnCall,
       "securityProfile-EditComCall": securityProfile_EditComCall,
       "securityProfile-EditAllCall": securityProfile_EditAllCall,
       "securityProfile-SysDiag": securityProfile_SysDiag,
       "securityProfile-OwnPortDiag": securityProfile_OwnPortDiag,
       "securityProfile-AllPortDiag": securityProfile_AllPortDiag,
       "securityProfile-Download": securityProfile_Download,
       "securityProfile-Upload": securityProfile_Upload,
       "securityProfile-FieldService": securityProfile_FieldService,
       "securityProfile-UseTacacsPlus": securityProfile_UseTacacsPlus,
       "securityProfile-Action-o": securityProfile_Action_o}
)
