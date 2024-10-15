# SNMP MIB module (TFTP-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TFTP-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:30 2024
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
 enterprises,
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
    "enterprises",
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

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatTFTPGroup_ObjectIdentity = ObjectIdentity
cdx6500StatTFTPGroup = _Cdx6500StatTFTPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3)
)


class _Cdx6500StatTFTPoperation_Type(Integer32):
    """Custom type cdx6500StatTFTPoperation based on Integer32"""
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
              9,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("configurationDownloadToAlternateBank", 2),
          ("configurationDownloadToCurrentBank", 1),
          ("configurationRestoreFromScript", 7),
          ("configurationRestoreToScript", 8),
          ("configurationUploadFromAlternateBank", 4),
          ("configurationUploadFromCurrentBank", 3),
          ("descriptionfileUpload", 9),
          ("noOperation", 100),
          ("nondefaultvalueUpload", 10),
          ("softwareDownloadToAlternateBank", 6),
          ("softwareDownloadToCurrentBank", 5))
    )


_Cdx6500StatTFTPoperation_Type.__name__ = "Integer32"
_Cdx6500StatTFTPoperation_Object = MibScalar
cdx6500StatTFTPoperation = _Cdx6500StatTFTPoperation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 1),
    _Cdx6500StatTFTPoperation_Type()
)
cdx6500StatTFTPoperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatTFTPoperation.setStatus("mandatory")
_Cdx6500StatTFTPIPaddress_Type = IpAddress
_Cdx6500StatTFTPIPaddress_Object = MibScalar
cdx6500StatTFTPIPaddress = _Cdx6500StatTFTPIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 2),
    _Cdx6500StatTFTPIPaddress_Type()
)
cdx6500StatTFTPIPaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatTFTPIPaddress.setStatus("mandatory")
_Cdx6500StatTFTPfilename_Type = DisplayString
_Cdx6500StatTFTPfilename_Object = MibScalar
cdx6500StatTFTPfilename = _Cdx6500StatTFTPfilename_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 3),
    _Cdx6500StatTFTPfilename_Type()
)
cdx6500StatTFTPfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatTFTPfilename.setStatus("mandatory")
_Cdx6500StatTFTPtimestamp_Type = DisplayString
_Cdx6500StatTFTPtimestamp_Object = MibScalar
cdx6500StatTFTPtimestamp = _Cdx6500StatTFTPtimestamp_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 4),
    _Cdx6500StatTFTPtimestamp_Type()
)
cdx6500StatTFTPtimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatTFTPtimestamp.setStatus("mandatory")
_Cdx6500StatTFTPbytecount_Type = Integer32
_Cdx6500StatTFTPbytecount_Object = MibScalar
cdx6500StatTFTPbytecount = _Cdx6500StatTFTPbytecount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 5),
    _Cdx6500StatTFTPbytecount_Type()
)
cdx6500StatTFTPbytecount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatTFTPbytecount.setStatus("mandatory")
_Cdx6500StatTFTPstatus_Type = DisplayString
_Cdx6500StatTFTPstatus_Object = MibScalar
cdx6500StatTFTPstatus = _Cdx6500StatTFTPstatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 6),
    _Cdx6500StatTFTPstatus_Type()
)
cdx6500StatTFTPstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatTFTPstatus.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)
_Cdx6500ContTFTP_ObjectIdentity = ObjectIdentity
cdx6500ContTFTP = _Cdx6500ContTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2)
)


class _Cdx6500ContTFTPoperation_Type(Integer32):
    """Custom type cdx6500ContTFTPoperation based on Integer32"""
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
              9,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("configurationDownloadToAlternateBank", 2),
          ("configurationDownloadToCurrentBank", 1),
          ("configurationRestoreFromScript", 7),
          ("configurationRestoreToScript", 8),
          ("configurationUploadFromAlternateBank", 4),
          ("configurationUploadFromCurrentBank", 3),
          ("descriptionfileUpload", 9),
          ("noOperation", 100),
          ("nondefaultvalueUpload", 10),
          ("softwareDownloadToAlternateBank", 6),
          ("softwareDownloadToCurrentBank", 5))
    )


_Cdx6500ContTFTPoperation_Type.__name__ = "Integer32"
_Cdx6500ContTFTPoperation_Object = MibScalar
cdx6500ContTFTPoperation = _Cdx6500ContTFTPoperation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2, 1),
    _Cdx6500ContTFTPoperation_Type()
)
cdx6500ContTFTPoperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500ContTFTPoperation.setStatus("mandatory")
_Cdx6500ContTFTPIPaddress_Type = IpAddress
_Cdx6500ContTFTPIPaddress_Object = MibScalar
cdx6500ContTFTPIPaddress = _Cdx6500ContTFTPIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2, 2),
    _Cdx6500ContTFTPIPaddress_Type()
)
cdx6500ContTFTPIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500ContTFTPIPaddress.setStatus("mandatory")
_Cdx6500ContTFTPfilename_Type = DisplayString
_Cdx6500ContTFTPfilename_Object = MibScalar
cdx6500ContTFTPfilename = _Cdx6500ContTFTPfilename_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2, 3),
    _Cdx6500ContTFTPfilename_Type()
)
cdx6500ContTFTPfilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500ContTFTPfilename.setStatus("mandatory")


class _Cdx6500ContTFTPinitiateorder_Type(Integer32):
    """Custom type cdx6500ContTFTPinitiateorder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_Cdx6500ContTFTPinitiateorder_Type.__name__ = "Integer32"
_Cdx6500ContTFTPinitiateorder_Object = MibScalar
cdx6500ContTFTPinitiateorder = _Cdx6500ContTFTPinitiateorder_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2, 4),
    _Cdx6500ContTFTPinitiateorder_Type()
)
cdx6500ContTFTPinitiateorder.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    cdx6500ContTFTPinitiateorder.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TFTP-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatTFTPGroup": cdx6500StatTFTPGroup,
       "cdx6500StatTFTPoperation": cdx6500StatTFTPoperation,
       "cdx6500StatTFTPIPaddress": cdx6500StatTFTPIPaddress,
       "cdx6500StatTFTPfilename": cdx6500StatTFTPfilename,
       "cdx6500StatTFTPtimestamp": cdx6500StatTFTPtimestamp,
       "cdx6500StatTFTPbytecount": cdx6500StatTFTPbytecount,
       "cdx6500StatTFTPstatus": cdx6500StatTFTPstatus,
       "cdx6500Controls": cdx6500Controls,
       "cdx6500ContTFTP": cdx6500ContTFTP,
       "cdx6500ContTFTPoperation": cdx6500ContTFTPoperation,
       "cdx6500ContTFTPIPaddress": cdx6500ContTFTPIPaddress,
       "cdx6500ContTFTPfilename": cdx6500ContTFTPfilename,
       "cdx6500ContTFTPinitiateorder": cdx6500ContTFTPinitiateorder}
)
