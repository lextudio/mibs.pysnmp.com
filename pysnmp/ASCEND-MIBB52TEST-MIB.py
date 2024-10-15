# SNMP MIB module (ASCEND-MIBB52TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBB52TEST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:14 2024
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

_Mibb52TestProfile_ObjectIdentity = ObjectIdentity
mibb52TestProfile = _Mibb52TestProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 56)
)
_Mibb52TestProfileTable_Object = MibTable
mibb52TestProfileTable = _Mibb52TestProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 56, 1)
)
if mibBuilder.loadTexts:
    mibb52TestProfileTable.setStatus("mandatory")
_Mibb52TestProfileEntry_Object = MibTableRow
mibb52TestProfileEntry = _Mibb52TestProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1)
)
mibb52TestProfileEntry.setIndexNames(
    (0, "ASCEND-MIBB52TEST-MIB", "b52TestProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibb52TestProfileEntry.setStatus("mandatory")
_B52TestProfile_Index_o_Type = Integer32
_B52TestProfile_Index_o_Object = MibScalar
b52TestProfile_Index_o = _B52TestProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 1),
    _B52TestProfile_Index_o_Type()
)
b52TestProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    b52TestProfile_Index_o.setStatus("mandatory")


class _B52TestProfile_TftpBootType_Type(Integer32):
    """Custom type b52TestProfile_TftpBootType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tftpBootFirst", 2),
          ("tftpBootSecond", 3))
    )


_B52TestProfile_TftpBootType_Type.__name__ = "Integer32"
_B52TestProfile_TftpBootType_Object = MibScalar
b52TestProfile_TftpBootType = _B52TestProfile_TftpBootType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 2),
    _B52TestProfile_TftpBootType_Type()
)
b52TestProfile_TftpBootType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    b52TestProfile_TftpBootType.setStatus("mandatory")
_B52TestProfile_TftpBootHostName_Type = DisplayString
_B52TestProfile_TftpBootHostName_Object = MibScalar
b52TestProfile_TftpBootHostName = _B52TestProfile_TftpBootHostName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 3),
    _B52TestProfile_TftpBootHostName_Type()
)
b52TestProfile_TftpBootHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    b52TestProfile_TftpBootHostName.setStatus("mandatory")
_B52TestProfile_TftpBootBaseName_Type = DisplayString
_B52TestProfile_TftpBootBaseName_Object = MibScalar
b52TestProfile_TftpBootBaseName = _B52TestProfile_TftpBootBaseName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 4),
    _B52TestProfile_TftpBootBaseName_Type()
)
b52TestProfile_TftpBootBaseName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    b52TestProfile_TftpBootBaseName.setStatus("mandatory")


class _B52TestProfile_Action_o_Type(Integer32):
    """Custom type b52TestProfile_Action_o based on Integer32"""
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


_B52TestProfile_Action_o_Type.__name__ = "Integer32"
_B52TestProfile_Action_o_Object = MibScalar
b52TestProfile_Action_o = _B52TestProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 56, 1, 1, 5),
    _B52TestProfile_Action_o_Type()
)
b52TestProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    b52TestProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBB52TEST-MIB",
    **{"DisplayString": DisplayString,
       "mibb52TestProfile": mibb52TestProfile,
       "mibb52TestProfileTable": mibb52TestProfileTable,
       "mibb52TestProfileEntry": mibb52TestProfileEntry,
       "b52TestProfile-Index-o": b52TestProfile_Index_o,
       "b52TestProfile-TftpBootType": b52TestProfile_TftpBootType,
       "b52TestProfile-TftpBootHostName": b52TestProfile_TftpBootHostName,
       "b52TestProfile-TftpBootBaseName": b52TestProfile_TftpBootBaseName,
       "b52TestProfile-Action-o": b52TestProfile_Action_o}
)
