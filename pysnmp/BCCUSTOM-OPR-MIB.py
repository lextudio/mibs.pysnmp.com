# SNMP MIB module (BCCUSTOM-OPR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BCCUSTOM-OPR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:27 2024
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

(fcSwitch,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "fcSwitch")

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

bcCustomOperation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52)
)
bcCustomOperation.setRevisions(
        ("2011-12-19 10:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwinfospsaveCmd_ObjectIdentity = ObjectIdentity
hwinfospsaveCmd = _HwinfospsaveCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 1)
)
if mibBuilder.loadTexts:
    hwinfospsaveCmd.setStatus("current")


class _HwinfospsaveSet_Type(OctetString):
    """Custom type hwinfospsaveSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwinfospsaveSet_Type.__name__ = "OctetString"
_HwinfospsaveSet_Object = MibScalar
hwinfospsaveSet = _HwinfospsaveSet_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 1, 1),
    _HwinfospsaveSet_Type()
)
hwinfospsaveSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwinfospsaveSet.setStatus("current")


class _HwinfospsaveGet_Type(Integer32):
    """Custom type hwinfospsaveGet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftperror", 1),
          ("progressing", 2),
          ("success", 0),
          ("systemerror", 3))
    )


_HwinfospsaveGet_Type.__name__ = "Integer32"
_HwinfospsaveGet_Object = MibScalar
hwinfospsaveGet = _HwinfospsaveGet_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 1, 2),
    _HwinfospsaveGet_Type()
)
hwinfospsaveGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwinfospsaveGet.setStatus("current")
_HwUpdateFilecmd_ObjectIdentity = ObjectIdentity
hwUpdateFilecmd = _HwUpdateFilecmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 2)
)
if mibBuilder.loadTexts:
    hwUpdateFilecmd.setStatus("current")


class _HwUpdateFile_Type(OctetString):
    """Custom type hwUpdateFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwUpdateFile_Type.__name__ = "OctetString"
_HwUpdateFile_Object = MibScalar
hwUpdateFile = _HwUpdateFile_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 2, 1),
    _HwUpdateFile_Type()
)
hwUpdateFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUpdateFile.setStatus("current")


class _HwUpdateFileInfo_Type(OctetString):
    """Custom type hwUpdateFileInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_HwUpdateFileInfo_Type.__name__ = "OctetString"
_HwUpdateFileInfo_Object = MibScalar
hwUpdateFileInfo = _HwUpdateFileInfo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 2, 2),
    _HwUpdateFileInfo_Type()
)
hwUpdateFileInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUpdateFileInfo.setStatus("current")


class _HwSoftwareVersion_Type(OctetString):
    """Custom type hwSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_HwSoftwareVersion_Type.__name__ = "OctetString"
_HwSoftwareVersion_Object = MibScalar
hwSoftwareVersion = _HwSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 52, 2, 3),
    _HwSoftwareVersion_Type()
)
hwSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSoftwareVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCCUSTOM-OPR-MIB",
    **{"bcCustomOperation": bcCustomOperation,
       "hwinfospsaveCmd": hwinfospsaveCmd,
       "hwinfospsaveSet": hwinfospsaveSet,
       "hwinfospsaveGet": hwinfospsaveGet,
       "hwUpdateFilecmd": hwUpdateFilecmd,
       "hwUpdateFile": hwUpdateFile,
       "hwUpdateFileInfo": hwUpdateFileInfo,
       "hwSoftwareVersion": hwSoftwareVersion}
)
