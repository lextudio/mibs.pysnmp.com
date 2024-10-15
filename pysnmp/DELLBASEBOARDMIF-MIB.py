# SNMP MIB module (DELLBASEBOARDMIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELLBASEBOARDMIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:07 2024
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

(DmiDate,) = mibBuilder.importSymbols(
    "DMTF-DMI-MIB",
    "DmiDate")

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
 NotificationType,
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
    "NotificationType",
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



class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiOctetstring(OctetString):
    """Custom type DmiOctetstring based on OctetString"""




class DmiDisplaystring(DisplayString):
    """Custom type DmiDisplaystring based on DisplayString"""




class DmiComponentIndex(Integer32):
    """Custom type DmiComponentIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674)
)
_Server_ObjectIdentity = ObjectIdentity
server = _Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890)
)
_Baseboard_ObjectIdentity = ObjectIdentity
baseboard = _Baseboard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1)
)
_DmtfGroups_ObjectIdentity = ObjectIdentity
dmtfGroups = _DmtfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1)
)
_TComponentid_Object = MibTable
tComponentid = _TComponentid_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tComponentid.setStatus("mandatory")
_EComponentid_Object = MibTableRow
eComponentid = _EComponentid_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 1, 1)
)
eComponentid.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eComponentid.setStatus("mandatory")
_A1Manufacturer_Type = DmiDisplaystring
_A1Manufacturer_Object = MibTableColumn
a1Manufacturer = _A1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 1, 1, 1),
    _A1Manufacturer_Type()
)
a1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Manufacturer.setStatus("mandatory")
_A1Product_Type = DmiDisplaystring
_A1Product_Object = MibTableColumn
a1Product = _A1Product_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 1, 1, 2),
    _A1Product_Type()
)
a1Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Product.setStatus("mandatory")
_A1Version_Type = DmiDisplaystring
_A1Version_Object = MibTableColumn
a1Version = _A1Version_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 1, 1, 3),
    _A1Version_Type()
)
a1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Version.setStatus("mandatory")
_A1SerialNumber_Type = DmiDisplaystring
_A1SerialNumber_Object = MibTableColumn
a1SerialNumber = _A1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 1, 1, 4),
    _A1SerialNumber_Type()
)
a1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1SerialNumber.setStatus("mandatory")
_A1Installation_Type = DmiDate
_A1Installation_Object = MibTableColumn
a1Installation = _A1Installation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 1, 1, 5),
    _A1Installation_Type()
)
a1Installation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Installation.setStatus("mandatory")


class _A1Verify_Type(Integer32):
    """Custom type a1Verify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("vAnErrorOccurredCheckStatusCode", 0),
          ("vReserved", 3),
          ("vTheVerifyIsNotSupported", 2),
          ("vThisComponentDoesNotExist", 1),
          ("vThisComponentExistsAndIsFunctioningCorr", 7),
          ("vThisComponentExistsAndIsNotFunctioningC", 6),
          ("vThisComponentExistsButTheFunctionality1", 5),
          ("vThisComponentExistsButTheFunctionalityI", 4))
    )


_A1Verify_Type.__name__ = "Integer32"
_A1Verify_Object = MibTableColumn
a1Verify = _A1Verify_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 1, 1, 6),
    _A1Verify_Type()
)
a1Verify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a1Verify.setStatus("mandatory")
_TTemperature_Object = MibTable
tTemperature = _TTemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tTemperature.setStatus("mandatory")
_ETemperature_Object = MibTableRow
eTemperature = _ETemperature_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 2, 1)
)
eTemperature.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a2Tempparentindex"),
    (0, "DELLBASEBOARDMIF-MIB", "a2Tempindex"),
)
if mibBuilder.loadTexts:
    eTemperature.setStatus("mandatory")
_A2Tempparentindex_Type = DmiInteger
_A2Tempparentindex_Object = MibTableColumn
a2Tempparentindex = _A2Tempparentindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 2, 1, 1),
    _A2Tempparentindex_Type()
)
a2Tempparentindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Tempparentindex.setStatus("mandatory")
_A2Tempindex_Type = DmiInteger
_A2Tempindex_Object = MibTableColumn
a2Tempindex = _A2Tempindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 2, 1, 2),
    _A2Tempindex_Type()
)
a2Tempindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Tempindex.setStatus("mandatory")


class _A2Temptype_Type(Integer32):
    """Custom type a2Temptype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("vBackplane", 6),
          ("vEsm", 5),
          ("vHarrierBackplane", 7),
          ("vOther", 1),
          ("vTmc", 3),
          ("vTvm", 4),
          ("vUnknown", 2))
    )


_A2Temptype_Type.__name__ = "Integer32"
_A2Temptype_Object = MibTableColumn
a2Temptype = _A2Temptype_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 2, 1, 3),
    _A2Temptype_Type()
)
a2Temptype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Temptype.setStatus("mandatory")


class _A2Tempstatus_Type(Integer32):
    """Custom type a2Tempstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A2Tempstatus_Type.__name__ = "Integer32"
_A2Tempstatus_Object = MibTableColumn
a2Tempstatus = _A2Tempstatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 2, 1, 4),
    _A2Tempstatus_Type()
)
a2Tempstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Tempstatus.setStatus("mandatory")
_A2Tempreading_Type = DmiInteger
_A2Tempreading_Object = MibTableColumn
a2Tempreading = _A2Tempreading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 2, 1, 5),
    _A2Tempreading_Type()
)
a2Tempreading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Tempreading.setStatus("mandatory")
_A2Tempminwarn_Type = DmiDisplaystring
_A2Tempminwarn_Object = MibTableColumn
a2Tempminwarn = _A2Tempminwarn_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 2, 1, 6),
    _A2Tempminwarn_Type()
)
a2Tempminwarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2Tempminwarn.setStatus("mandatory")
_A2Tempmaxwarn_Type = DmiDisplaystring
_A2Tempmaxwarn_Object = MibTableColumn
a2Tempmaxwarn = _A2Tempmaxwarn_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 2, 1, 7),
    _A2Tempmaxwarn_Type()
)
a2Tempmaxwarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a2Tempmaxwarn.setStatus("mandatory")
_A2Tempminfail_Type = DmiInteger
_A2Tempminfail_Object = MibTableColumn
a2Tempminfail = _A2Tempminfail_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 2, 1, 8),
    _A2Tempminfail_Type()
)
a2Tempminfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Tempminfail.setStatus("mandatory")
_A2Tempmaxfail_Type = DmiInteger
_A2Tempmaxfail_Object = MibTableColumn
a2Tempmaxfail = _A2Tempmaxfail_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 2, 1, 9),
    _A2Tempmaxfail_Type()
)
a2Tempmaxfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Tempmaxfail.setStatus("mandatory")
_A2Templocation_Type = DmiDisplaystring
_A2Templocation_Object = MibTableColumn
a2Templocation = _A2Templocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 2, 1, 10),
    _A2Templocation_Type()
)
a2Templocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a2Templocation.setStatus("mandatory")
_TFan_Object = MibTable
tFan = _TFan_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tFan.setStatus("mandatory")
_EFan_Object = MibTableRow
eFan = _EFan_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 3, 1)
)
eFan.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a3Fansparentindex"),
    (0, "DELLBASEBOARDMIF-MIB", "a3Fansindex"),
)
if mibBuilder.loadTexts:
    eFan.setStatus("mandatory")
_A3Fansparentindex_Type = DmiInteger
_A3Fansparentindex_Object = MibTableColumn
a3Fansparentindex = _A3Fansparentindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 3, 1, 1),
    _A3Fansparentindex_Type()
)
a3Fansparentindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Fansparentindex.setStatus("mandatory")
_A3Fansindex_Type = DmiInteger
_A3Fansindex_Object = MibTableColumn
a3Fansindex = _A3Fansindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 3, 1, 2),
    _A3Fansindex_Type()
)
a3Fansindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Fansindex.setStatus("mandatory")


class _A3Fanstype_Type(Integer32):
    """Custom type a3Fanstype based on Integer32"""
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
        *(("vBoolean", 3),
          ("vOther", 1),
          ("vRpm", 4),
          ("vUnknown", 2))
    )


_A3Fanstype_Type.__name__ = "Integer32"
_A3Fanstype_Object = MibTableColumn
a3Fanstype = _A3Fanstype_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 3, 1, 3),
    _A3Fanstype_Type()
)
a3Fanstype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Fanstype.setStatus("mandatory")


class _A3Fansstatus_Type(Integer32):
    """Custom type a3Fansstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A3Fansstatus_Type.__name__ = "Integer32"
_A3Fansstatus_Object = MibTableColumn
a3Fansstatus = _A3Fansstatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 3, 1, 4),
    _A3Fansstatus_Type()
)
a3Fansstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Fansstatus.setStatus("mandatory")
_A3Fansreading_Type = DmiInteger
_A3Fansreading_Object = MibTableColumn
a3Fansreading = _A3Fansreading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 3, 1, 5),
    _A3Fansreading_Type()
)
a3Fansreading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Fansreading.setStatus("mandatory")
_A3Fanswarningmin_Type = DmiDisplaystring
_A3Fanswarningmin_Object = MibTableColumn
a3Fanswarningmin = _A3Fanswarningmin_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 3, 1, 6),
    _A3Fanswarningmin_Type()
)
a3Fanswarningmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3Fanswarningmin.setStatus("mandatory")
_A3Fansmaxwarn_Type = DmiDisplaystring
_A3Fansmaxwarn_Object = MibTableColumn
a3Fansmaxwarn = _A3Fansmaxwarn_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 3, 1, 7),
    _A3Fansmaxwarn_Type()
)
a3Fansmaxwarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3Fansmaxwarn.setStatus("mandatory")
_A3Fansminfail_Type = DmiInteger
_A3Fansminfail_Object = MibTableColumn
a3Fansminfail = _A3Fansminfail_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 3, 1, 8),
    _A3Fansminfail_Type()
)
a3Fansminfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Fansminfail.setStatus("mandatory")
_A3Fansmaxfail_Type = DmiInteger
_A3Fansmaxfail_Object = MibTableColumn
a3Fansmaxfail = _A3Fansmaxfail_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 3, 1, 9),
    _A3Fansmaxfail_Type()
)
a3Fansmaxfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Fansmaxfail.setStatus("mandatory")
_A3Fanslocation_Type = DmiDisplaystring
_A3Fanslocation_Object = MibTableColumn
a3Fanslocation = _A3Fanslocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 3, 1, 10),
    _A3Fanslocation_Type()
)
a3Fanslocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3Fanslocation.setStatus("mandatory")
_TVoltage_Object = MibTable
tVoltage = _TVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tVoltage.setStatus("mandatory")
_EVoltage_Object = MibTableRow
eVoltage = _EVoltage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 4, 1)
)
eVoltage.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a4Voltparentindex"),
    (0, "DELLBASEBOARDMIF-MIB", "a4Voltindex"),
)
if mibBuilder.loadTexts:
    eVoltage.setStatus("mandatory")
_A4Voltparentindex_Type = DmiInteger
_A4Voltparentindex_Object = MibTableColumn
a4Voltparentindex = _A4Voltparentindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 4, 1, 1),
    _A4Voltparentindex_Type()
)
a4Voltparentindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Voltparentindex.setStatus("mandatory")
_A4Voltindex_Type = DmiInteger
_A4Voltindex_Object = MibTableColumn
a4Voltindex = _A4Voltindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 4, 1, 2),
    _A4Voltindex_Type()
)
a4Voltindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Voltindex.setStatus("mandatory")


class _A4Volttype_Type(Integer32):
    """Custom type a4Volttype based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("v-12v", 7),
          ("v-3-3v", 3),
          ("v-5v", 5),
          ("v12v", 8),
          ("v15v", 9),
          ("v3-3v", 4),
          ("v5v", 6),
          ("vCore", 10),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A4Volttype_Type.__name__ = "Integer32"
_A4Volttype_Object = MibTableColumn
a4Volttype = _A4Volttype_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 4, 1, 3),
    _A4Volttype_Type()
)
a4Volttype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Volttype.setStatus("mandatory")


class _A4Voltstatus_Type(Integer32):
    """Custom type a4Voltstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A4Voltstatus_Type.__name__ = "Integer32"
_A4Voltstatus_Object = MibTableColumn
a4Voltstatus = _A4Voltstatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 4, 1, 4),
    _A4Voltstatus_Type()
)
a4Voltstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Voltstatus.setStatus("mandatory")
_A4Voltreading_Type = DmiInteger
_A4Voltreading_Object = MibTableColumn
a4Voltreading = _A4Voltreading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 4, 1, 5),
    _A4Voltreading_Type()
)
a4Voltreading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Voltreading.setStatus("mandatory")
_A4Voltminwarn_Type = DmiDisplaystring
_A4Voltminwarn_Object = MibTableColumn
a4Voltminwarn = _A4Voltminwarn_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 4, 1, 6),
    _A4Voltminwarn_Type()
)
a4Voltminwarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4Voltminwarn.setStatus("mandatory")
_A4Voltmaxwarn_Type = DmiDisplaystring
_A4Voltmaxwarn_Object = MibTableColumn
a4Voltmaxwarn = _A4Voltmaxwarn_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 4, 1, 7),
    _A4Voltmaxwarn_Type()
)
a4Voltmaxwarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a4Voltmaxwarn.setStatus("mandatory")
_A4Voltminfail_Type = DmiInteger
_A4Voltminfail_Object = MibTableColumn
a4Voltminfail = _A4Voltminfail_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 4, 1, 8),
    _A4Voltminfail_Type()
)
a4Voltminfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Voltminfail.setStatus("mandatory")
_A4Voltmaxfail_Type = DmiInteger
_A4Voltmaxfail_Object = MibTableColumn
a4Voltmaxfail = _A4Voltmaxfail_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 4, 1, 9),
    _A4Voltmaxfail_Type()
)
a4Voltmaxfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Voltmaxfail.setStatus("mandatory")
_A4Voltlocation_Type = DmiDisplaystring
_A4Voltlocation_Object = MibTableColumn
a4Voltlocation = _A4Voltlocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 4, 1, 10),
    _A4Voltlocation_Type()
)
a4Voltlocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a4Voltlocation.setStatus("mandatory")
_TCurrent_Object = MibTable
tCurrent = _TCurrent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tCurrent.setStatus("mandatory")
_ECurrent_Object = MibTableRow
eCurrent = _ECurrent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 5, 1)
)
eCurrent.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a5Ampparentindex"),
    (0, "DELLBASEBOARDMIF-MIB", "a5Ampindex"),
)
if mibBuilder.loadTexts:
    eCurrent.setStatus("mandatory")
_A5Ampparentindex_Type = DmiInteger
_A5Ampparentindex_Object = MibTableColumn
a5Ampparentindex = _A5Ampparentindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 5, 1, 1),
    _A5Ampparentindex_Type()
)
a5Ampparentindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Ampparentindex.setStatus("mandatory")
_A5Ampindex_Type = DmiInteger
_A5Ampindex_Object = MibTableColumn
a5Ampindex = _A5Ampindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 5, 1, 2),
    _A5Ampindex_Type()
)
a5Ampindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Ampindex.setStatus("mandatory")


class _A5Amptype_Type(Integer32):
    """Custom type a5Amptype based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("v-12v", 7),
          ("v-3-3v", 3),
          ("v-5v", 5),
          ("v12v", 8),
          ("v3-3v", 4),
          ("v5v", 6),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A5Amptype_Type.__name__ = "Integer32"
_A5Amptype_Object = MibTableColumn
a5Amptype = _A5Amptype_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 5, 1, 3),
    _A5Amptype_Type()
)
a5Amptype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Amptype.setStatus("mandatory")


class _A5Ampstatus_Type(Integer32):
    """Custom type a5Ampstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A5Ampstatus_Type.__name__ = "Integer32"
_A5Ampstatus_Object = MibTableColumn
a5Ampstatus = _A5Ampstatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 5, 1, 4),
    _A5Ampstatus_Type()
)
a5Ampstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Ampstatus.setStatus("mandatory")
_A5Ampreading_Type = DmiInteger
_A5Ampreading_Object = MibTableColumn
a5Ampreading = _A5Ampreading_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 5, 1, 5),
    _A5Ampreading_Type()
)
a5Ampreading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Ampreading.setStatus("mandatory")
_A5Ampminwarn_Type = DmiDisplaystring
_A5Ampminwarn_Object = MibTableColumn
a5Ampminwarn = _A5Ampminwarn_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 5, 1, 6),
    _A5Ampminwarn_Type()
)
a5Ampminwarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a5Ampminwarn.setStatus("mandatory")
_A5Ampmaxwarn_Type = DmiDisplaystring
_A5Ampmaxwarn_Object = MibTableColumn
a5Ampmaxwarn = _A5Ampmaxwarn_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 5, 1, 7),
    _A5Ampmaxwarn_Type()
)
a5Ampmaxwarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a5Ampmaxwarn.setStatus("mandatory")
_A5Ampminfail_Type = DmiInteger
_A5Ampminfail_Object = MibTableColumn
a5Ampminfail = _A5Ampminfail_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 5, 1, 8),
    _A5Ampminfail_Type()
)
a5Ampminfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Ampminfail.setStatus("mandatory")
_A5Ampmaxfail_Type = DmiInteger
_A5Ampmaxfail_Object = MibTableColumn
a5Ampmaxfail = _A5Ampmaxfail_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 5, 1, 9),
    _A5Ampmaxfail_Type()
)
a5Ampmaxfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Ampmaxfail.setStatus("mandatory")
_A5Amplocation_Type = DmiDisplaystring
_A5Amplocation_Object = MibTableColumn
a5Amplocation = _A5Amplocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 5, 1, 10),
    _A5Amplocation_Type()
)
a5Amplocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a5Amplocation.setStatus("mandatory")
_TPowerSupply_Object = MibTable
tPowerSupply = _TPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tPowerSupply.setStatus("mandatory")
_EPowerSupply_Object = MibTableRow
ePowerSupply = _EPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 6, 1)
)
ePowerSupply.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a6Pwrsupplyparentindex"),
    (0, "DELLBASEBOARDMIF-MIB", "a6Pwrsupplyindex"),
)
if mibBuilder.loadTexts:
    ePowerSupply.setStatus("mandatory")
_A6Pwrsupplyparentindex_Type = DmiInteger
_A6Pwrsupplyparentindex_Object = MibTableColumn
a6Pwrsupplyparentindex = _A6Pwrsupplyparentindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 6, 1, 1),
    _A6Pwrsupplyparentindex_Type()
)
a6Pwrsupplyparentindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6Pwrsupplyparentindex.setStatus("mandatory")
_A6Pwrsupplyindex_Type = DmiInteger
_A6Pwrsupplyindex_Object = MibTableColumn
a6Pwrsupplyindex = _A6Pwrsupplyindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 6, 1, 2),
    _A6Pwrsupplyindex_Type()
)
a6Pwrsupplyindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6Pwrsupplyindex.setStatus("mandatory")


class _A6Pwrsupplytype_Type(Integer32):
    """Custom type a6Pwrsupplytype based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("v230w", 4),
          ("v275w", 8),
          ("v320w", 7),
          ("v500w", 5),
          ("v700w", 6),
          ("vOther", 1),
          ("vPspb", 3),
          ("vUnknown", 2))
    )


_A6Pwrsupplytype_Type.__name__ = "Integer32"
_A6Pwrsupplytype_Object = MibTableColumn
a6Pwrsupplytype = _A6Pwrsupplytype_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 6, 1, 3),
    _A6Pwrsupplytype_Type()
)
a6Pwrsupplytype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6Pwrsupplytype.setStatus("mandatory")


class _A6Pwrsupplystatus_Type(Integer32):
    """Custom type a6Pwrsupplystatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A6Pwrsupplystatus_Type.__name__ = "Integer32"
_A6Pwrsupplystatus_Object = MibTableColumn
a6Pwrsupplystatus = _A6Pwrsupplystatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 6, 1, 4),
    _A6Pwrsupplystatus_Type()
)
a6Pwrsupplystatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6Pwrsupplystatus.setStatus("mandatory")
_A6Pwrsupplyonline_Type = DmiDisplaystring
_A6Pwrsupplyonline_Object = MibTableColumn
a6Pwrsupplyonline = _A6Pwrsupplyonline_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 6, 1, 5),
    _A6Pwrsupplyonline_Type()
)
a6Pwrsupplyonline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a6Pwrsupplyonline.setStatus("mandatory")
_A6Pwrlocation_Type = DmiDisplaystring
_A6Pwrlocation_Object = MibTableColumn
a6Pwrlocation = _A6Pwrlocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 6, 1, 6),
    _A6Pwrlocation_Type()
)
a6Pwrlocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a6Pwrlocation.setStatus("mandatory")
_TGlobalPowerUnit_Object = MibTable
tGlobalPowerUnit = _TGlobalPowerUnit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tGlobalPowerUnit.setStatus("mandatory")
_EGlobalPowerUnit_Object = MibTableRow
eGlobalPowerUnit = _EGlobalPowerUnit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 7, 1)
)
eGlobalPowerUnit.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a7Pwrunitindex"),
)
if mibBuilder.loadTexts:
    eGlobalPowerUnit.setStatus("mandatory")


class _A7Pwrunitstatus_Type(Integer32):
    """Custom type a7Pwrunitstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("vDegradedRedundancy", 6),
          ("vFullyRedundant", 5),
          ("vNotApplicableUnitNotRedundant", 3),
          ("vOffline", 4),
          ("vOther", 1),
          ("vRedundancyLost", 7),
          ("vUnknown", 2))
    )


_A7Pwrunitstatus_Type.__name__ = "Integer32"
_A7Pwrunitstatus_Object = MibTableColumn
a7Pwrunitstatus = _A7Pwrunitstatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 7, 1, 1),
    _A7Pwrunitstatus_Type()
)
a7Pwrunitstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7Pwrunitstatus.setStatus("mandatory")
_A7Pwrunitgloballevel_Type = DmiInteger
_A7Pwrunitgloballevel_Object = MibTableColumn
a7Pwrunitgloballevel = _A7Pwrunitgloballevel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 7, 1, 2),
    _A7Pwrunitgloballevel_Type()
)
a7Pwrunitgloballevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7Pwrunitgloballevel.setStatus("mandatory")
_A7Pwrunitglobalmaxwarn_Type = DmiDisplaystring
_A7Pwrunitglobalmaxwarn_Object = MibTableColumn
a7Pwrunitglobalmaxwarn = _A7Pwrunitglobalmaxwarn_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 7, 1, 3),
    _A7Pwrunitglobalmaxwarn_Type()
)
a7Pwrunitglobalmaxwarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a7Pwrunitglobalmaxwarn.setStatus("mandatory")
_A7Pwrunitlevel33v_Type = DmiInteger
_A7Pwrunitlevel33v_Object = MibTableColumn
a7Pwrunitlevel33v = _A7Pwrunitlevel33v_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 7, 1, 4),
    _A7Pwrunitlevel33v_Type()
)
a7Pwrunitlevel33v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7Pwrunitlevel33v.setStatus("mandatory")
_A7Pwrunitmaxwarn33v_Type = DmiDisplaystring
_A7Pwrunitmaxwarn33v_Object = MibTableColumn
a7Pwrunitmaxwarn33v = _A7Pwrunitmaxwarn33v_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 7, 1, 5),
    _A7Pwrunitmaxwarn33v_Type()
)
a7Pwrunitmaxwarn33v.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a7Pwrunitmaxwarn33v.setStatus("mandatory")
_A7Pwrunitlevel5v_Type = DmiInteger
_A7Pwrunitlevel5v_Object = MibTableColumn
a7Pwrunitlevel5v = _A7Pwrunitlevel5v_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 7, 1, 6),
    _A7Pwrunitlevel5v_Type()
)
a7Pwrunitlevel5v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7Pwrunitlevel5v.setStatus("mandatory")
_A7Pwrunitmaxwarn5v_Type = DmiDisplaystring
_A7Pwrunitmaxwarn5v_Object = MibTableColumn
a7Pwrunitmaxwarn5v = _A7Pwrunitmaxwarn5v_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 7, 1, 7),
    _A7Pwrunitmaxwarn5v_Type()
)
a7Pwrunitmaxwarn5v.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a7Pwrunitmaxwarn5v.setStatus("mandatory")
_A7Pwrunitlevel12v_Type = DmiInteger
_A7Pwrunitlevel12v_Object = MibTableColumn
a7Pwrunitlevel12v = _A7Pwrunitlevel12v_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 7, 1, 8),
    _A7Pwrunitlevel12v_Type()
)
a7Pwrunitlevel12v.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7Pwrunitlevel12v.setStatus("mandatory")
_A7Pwrunitmaxwarn12v_Type = DmiDisplaystring
_A7Pwrunitmaxwarn12v_Object = MibTableColumn
a7Pwrunitmaxwarn12v = _A7Pwrunitmaxwarn12v_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 7, 1, 9),
    _A7Pwrunitmaxwarn12v_Type()
)
a7Pwrunitmaxwarn12v.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a7Pwrunitmaxwarn12v.setStatus("mandatory")
_A7Pwrunituid_Type = DmiDisplaystring
_A7Pwrunituid_Object = MibTableColumn
a7Pwrunituid = _A7Pwrunituid_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 7, 1, 10),
    _A7Pwrunituid_Type()
)
a7Pwrunituid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7Pwrunituid.setStatus("mandatory")
_A7Pwrunitindex_Type = DmiInteger
_A7Pwrunitindex_Object = MibTableColumn
a7Pwrunitindex = _A7Pwrunitindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 7, 1, 11),
    _A7Pwrunitindex_Type()
)
a7Pwrunitindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a7Pwrunitindex.setStatus("mandatory")
_TChassisExtension_Object = MibTable
tChassisExtension = _TChassisExtension_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8)
)
if mibBuilder.loadTexts:
    tChassisExtension.setStatus("mandatory")
_EChassisExtension_Object = MibTableRow
eChassisExtension = _EChassisExtension_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1)
)
eChassisExtension.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a8Chassindex"),
)
if mibBuilder.loadTexts:
    eChassisExtension.setStatus("mandatory")
_A8Chassindex_Type = DmiInteger
_A8Chassindex_Object = MibTableColumn
a8Chassindex = _A8Chassindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 1),
    _A8Chassindex_Type()
)
a8Chassindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chassindex.setStatus("mandatory")


class _A8Chassglobstatus_Type(Integer32):
    """Custom type a8Chassglobstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A8Chassglobstatus_Type.__name__ = "Integer32"
_A8Chassglobstatus_Object = MibTableColumn
a8Chassglobstatus = _A8Chassglobstatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 2),
    _A8Chassglobstatus_Type()
)
a8Chassglobstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chassglobstatus.setStatus("mandatory")


class _A8Chasstempstatus_Type(Integer32):
    """Custom type a8Chasstempstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A8Chasstempstatus_Type.__name__ = "Integer32"
_A8Chasstempstatus_Object = MibTableColumn
a8Chasstempstatus = _A8Chasstempstatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 3),
    _A8Chasstempstatus_Type()
)
a8Chasstempstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chasstempstatus.setStatus("mandatory")
_A8Chasstempprobes_Type = DmiOctetstring
_A8Chasstempprobes_Object = MibTableColumn
a8Chasstempprobes = _A8Chasstempprobes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 4),
    _A8Chasstempprobes_Type()
)
a8Chasstempprobes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chasstempprobes.setStatus("mandatory")


class _A8Chassfansstatus_Type(Integer32):
    """Custom type a8Chassfansstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A8Chassfansstatus_Type.__name__ = "Integer32"
_A8Chassfansstatus_Object = MibTableColumn
a8Chassfansstatus = _A8Chassfansstatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 5),
    _A8Chassfansstatus_Type()
)
a8Chassfansstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chassfansstatus.setStatus("mandatory")
_A8Chassfansprobes_Type = DmiOctetstring
_A8Chassfansprobes_Object = MibTableColumn
a8Chassfansprobes = _A8Chassfansprobes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 6),
    _A8Chassfansprobes_Type()
)
a8Chassfansprobes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chassfansprobes.setStatus("mandatory")


class _A8Chassvoltstatus_Type(Integer32):
    """Custom type a8Chassvoltstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A8Chassvoltstatus_Type.__name__ = "Integer32"
_A8Chassvoltstatus_Object = MibTableColumn
a8Chassvoltstatus = _A8Chassvoltstatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 7),
    _A8Chassvoltstatus_Type()
)
a8Chassvoltstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chassvoltstatus.setStatus("mandatory")
_A8Chassvoltprobes_Type = DmiOctetstring
_A8Chassvoltprobes_Object = MibTableColumn
a8Chassvoltprobes = _A8Chassvoltprobes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 8),
    _A8Chassvoltprobes_Type()
)
a8Chassvoltprobes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chassvoltprobes.setStatus("mandatory")


class _A8Chassampstatus_Type(Integer32):
    """Custom type a8Chassampstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A8Chassampstatus_Type.__name__ = "Integer32"
_A8Chassampstatus_Object = MibTableColumn
a8Chassampstatus = _A8Chassampstatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 9),
    _A8Chassampstatus_Type()
)
a8Chassampstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chassampstatus.setStatus("mandatory")
_A8Chassampprobes_Type = DmiOctetstring
_A8Chassampprobes_Object = MibTableColumn
a8Chassampprobes = _A8Chassampprobes_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 10),
    _A8Chassampprobes_Type()
)
a8Chassampprobes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chassampprobes.setStatus("mandatory")


class _A8Chasspsstatus_Type(Integer32):
    """Custom type a8Chasspsstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A8Chasspsstatus_Type.__name__ = "Integer32"
_A8Chasspsstatus_Object = MibTableColumn
a8Chasspsstatus = _A8Chasspsstatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 11),
    _A8Chasspsstatus_Type()
)
a8Chasspsstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chasspsstatus.setStatus("mandatory")
_A8Chasspwrsupplies_Type = DmiOctetstring
_A8Chasspwrsupplies_Object = MibTableColumn
a8Chasspwrsupplies = _A8Chasspwrsupplies_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 12),
    _A8Chasspwrsupplies_Type()
)
a8Chasspwrsupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chasspwrsupplies.setStatus("mandatory")
_A8Chassservicetag_Type = DmiDisplaystring
_A8Chassservicetag_Object = MibTableColumn
a8Chassservicetag = _A8Chassservicetag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 13),
    _A8Chassservicetag_Type()
)
a8Chassservicetag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chassservicetag.setStatus("mandatory")
_A8Chassuid_Type = DmiDisplaystring
_A8Chassuid_Object = MibTableColumn
a8Chassuid = _A8Chassuid_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 14),
    _A8Chassuid_Type()
)
a8Chassuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chassuid.setStatus("mandatory")
_A8Chassbackplaneuid_Type = DmiDisplaystring
_A8Chassbackplaneuid_Object = MibTableColumn
a8Chassbackplaneuid = _A8Chassbackplaneuid_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 15),
    _A8Chassbackplaneuid_Type()
)
a8Chassbackplaneuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a8Chassbackplaneuid.setStatus("mandatory")
_A8Chassidentify_Type = DmiDisplaystring
_A8Chassidentify_Object = MibTableColumn
a8Chassidentify = _A8Chassidentify_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 16),
    _A8Chassidentify_Type()
)
a8Chassidentify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a8Chassidentify.setStatus("mandatory")
_A8Chassfancontrol_Type = DmiDisplaystring
_A8Chassfancontrol_Object = MibTableColumn
a8Chassfancontrol = _A8Chassfancontrol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 17),
    _A8Chassfancontrol_Type()
)
a8Chassfancontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a8Chassfancontrol.setStatus("mandatory")
_A8Chassledconfig_Type = DmiDisplaystring
_A8Chassledconfig_Object = MibTableColumn
a8Chassledconfig = _A8Chassledconfig_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 18),
    _A8Chassledconfig_Type()
)
a8Chassledconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a8Chassledconfig.setStatus("mandatory")
_A8Chassfaultclear_Type = DmiDisplaystring
_A8Chassfaultclear_Object = MibTableColumn
a8Chassfaultclear = _A8Chassfaultclear_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 8, 1, 19),
    _A8Chassfaultclear_Type()
)
a8Chassfaultclear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a8Chassfaultclear.setStatus("mandatory")
_TPhysicalContainerGlobalTable_Object = MibTable
tPhysicalContainerGlobalTable = _TPhysicalContainerGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9)
)
if mibBuilder.loadTexts:
    tPhysicalContainerGlobalTable.setStatus("mandatory")
_EPhysicalContainerGlobalTable_Object = MibTableRow
ePhysicalContainerGlobalTable = _EPhysicalContainerGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9, 1)
)
ePhysicalContainerGlobalTable.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a9ContainerIndex"),
)
if mibBuilder.loadTexts:
    ePhysicalContainerGlobalTable.setStatus("mandatory")


class _A9ContainerOrChassisType_Type(Integer32):
    """Custom type a9ContainerOrChassisType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("vAllInOne", 13),
          ("vBusExpansionChassis", 20),
          ("vDesktop", 3),
          ("vDockingStation", 12),
          ("vExpansionChassis", 18),
          ("vHandheld", 11),
          ("vLaptop", 9),
          ("vLowProfileDesktop", 4),
          ("vLunchBox", 16),
          ("vMainSystemChassis", 17),
          ("vMiniTower", 6),
          ("vNotebook", 10),
          ("vOther", 1),
          ("vPeripheralChassis", 21),
          ("vPizzaBox", 5),
          ("vPortable", 8),
          ("vRackMountChassis", 23),
          ("vRaidChassis", 22),
          ("vSpace-saving", 15),
          ("vSubNotebook", 14),
          ("vSubchassis", 19),
          ("vTower", 7),
          ("vUnknown", 2))
    )


_A9ContainerOrChassisType_Type.__name__ = "Integer32"
_A9ContainerOrChassisType_Object = MibTableColumn
a9ContainerOrChassisType = _A9ContainerOrChassisType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9, 1, 1),
    _A9ContainerOrChassisType_Type()
)
a9ContainerOrChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ContainerOrChassisType.setStatus("mandatory")
_A9ContainerAssetTag_Type = DmiDisplaystring
_A9ContainerAssetTag_Object = MibTableColumn
a9ContainerAssetTag = _A9ContainerAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9, 1, 2),
    _A9ContainerAssetTag_Type()
)
a9ContainerAssetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a9ContainerAssetTag.setStatus("mandatory")


class _A9ChassisLockPresent_Type(Integer32):
    """Custom type a9ChassisLockPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1),
          ("vUnknown", 2))
    )


_A9ChassisLockPresent_Type.__name__ = "Integer32"
_A9ChassisLockPresent_Object = MibTableColumn
a9ChassisLockPresent = _A9ChassisLockPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9, 1, 3),
    _A9ChassisLockPresent_Type()
)
a9ChassisLockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ChassisLockPresent.setStatus("mandatory")


class _A9ContainerChassisBootupState_Type(Integer32):
    """Custom type a9ContainerChassisBootupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A9ContainerChassisBootupState_Type.__name__ = "Integer32"
_A9ContainerChassisBootupState_Object = MibTableColumn
a9ContainerChassisBootupState = _A9ContainerChassisBootupState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9, 1, 4),
    _A9ContainerChassisBootupState_Type()
)
a9ContainerChassisBootupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ContainerChassisBootupState.setStatus("mandatory")


class _A9PowerState_Type(Integer32):
    """Custom type a9PowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A9PowerState_Type.__name__ = "Integer32"
_A9PowerState_Object = MibTableColumn
a9PowerState = _A9PowerState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9, 1, 5),
    _A9PowerState_Type()
)
a9PowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9PowerState.setStatus("mandatory")


class _A9ThermalState_Type(Integer32):
    """Custom type a9ThermalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A9ThermalState_Type.__name__ = "Integer32"
_A9ThermalState_Object = MibTableColumn
a9ThermalState = _A9ThermalState_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9, 1, 6),
    _A9ThermalState_Type()
)
a9ThermalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ThermalState.setStatus("mandatory")
_A9FruGroupIndex_Type = DmiInteger
_A9FruGroupIndex_Object = MibTableColumn
a9FruGroupIndex = _A9FruGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9, 1, 7),
    _A9FruGroupIndex_Type()
)
a9FruGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9FruGroupIndex.setStatus("mandatory")
_A9OperationalGroupIndex_Type = DmiInteger
_A9OperationalGroupIndex_Object = MibTableColumn
a9OperationalGroupIndex = _A9OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9, 1, 8),
    _A9OperationalGroupIndex_Type()
)
a9OperationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9OperationalGroupIndex.setStatus("mandatory")
_A9ContainerIndex_Type = DmiInteger
_A9ContainerIndex_Object = MibTableColumn
a9ContainerIndex = _A9ContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9, 1, 9),
    _A9ContainerIndex_Type()
)
a9ContainerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ContainerIndex.setStatus("mandatory")
_A9ContainerName_Type = DmiDisplaystring
_A9ContainerName_Object = MibTableColumn
a9ContainerName = _A9ContainerName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9, 1, 10),
    _A9ContainerName_Type()
)
a9ContainerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a9ContainerName.setStatus("mandatory")
_A9ContainerLocation_Type = DmiDisplaystring
_A9ContainerLocation_Object = MibTableColumn
a9ContainerLocation = _A9ContainerLocation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9, 1, 11),
    _A9ContainerLocation_Type()
)
a9ContainerLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a9ContainerLocation.setStatus("mandatory")


class _A9ContainerSecurityStatus_Type(Integer32):
    """Custom type a9ContainerSecurityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("vContainerSecurityBreachAttempted", 4),
          ("vContainerSecurityBreached", 5),
          ("vNoSecurityBreachDetected", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A9ContainerSecurityStatus_Type.__name__ = "Integer32"
_A9ContainerSecurityStatus_Object = MibTableColumn
a9ContainerSecurityStatus = _A9ContainerSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9, 1, 12),
    _A9ContainerSecurityStatus_Type()
)
a9ContainerSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9ContainerSecurityStatus.setStatus("mandatory")
_TSystemControl_Object = MibTable
tSystemControl = _TSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 10)
)
if mibBuilder.loadTexts:
    tSystemControl.setStatus("mandatory")
_ESystemControl_Object = MibTableRow
eSystemControl = _ESystemControl_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 10, 1)
)
eSystemControl.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eSystemControl.setStatus("mandatory")
_A10AutomaticCapabilities_Type = DmiInteger
_A10AutomaticCapabilities_Object = MibTableColumn
a10AutomaticCapabilities = _A10AutomaticCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 10, 1, 1),
    _A10AutomaticCapabilities_Type()
)
a10AutomaticCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10AutomaticCapabilities.setStatus("mandatory")
_A10AutomaticSettings_Type = DmiDisplaystring
_A10AutomaticSettings_Object = MibTableColumn
a10AutomaticSettings = _A10AutomaticSettings_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 10, 1, 2),
    _A10AutomaticSettings_Type()
)
a10AutomaticSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10AutomaticSettings.setStatus("mandatory")
_A10NotificationNumber_Type = DmiDisplaystring
_A10NotificationNumber_Object = MibTableColumn
a10NotificationNumber = _A10NotificationNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 10, 1, 3),
    _A10NotificationNumber_Type()
)
a10NotificationNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10NotificationNumber.setStatus("mandatory")
_A10ManualCapabilities_Type = DmiInteger
_A10ManualCapabilities_Object = MibTableColumn
a10ManualCapabilities = _A10ManualCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 10, 1, 4),
    _A10ManualCapabilities_Type()
)
a10ManualCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a10ManualCapabilities.setStatus("mandatory")
_A10ManualControl_Type = DmiDisplaystring
_A10ManualControl_Object = MibTableColumn
a10ManualControl = _A10ManualControl_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 10, 1, 5),
    _A10ManualControl_Type()
)
a10ManualControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a10ManualControl.setStatus("mandatory")
_TEsmEventLog_Object = MibTable
tEsmEventLog = _TEsmEventLog_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 11)
)
if mibBuilder.loadTexts:
    tEsmEventLog.setStatus("mandatory")
_EEsmEventLog_Object = MibTableRow
eEsmEventLog = _EEsmEventLog_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 11, 1)
)
eEsmEventLog.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a11Esmlogindex"),
)
if mibBuilder.loadTexts:
    eEsmEventLog.setStatus("mandatory")
_A11Esmlogindex_Type = DmiInteger
_A11Esmlogindex_Object = MibTableColumn
a11Esmlogindex = _A11Esmlogindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 11, 1, 1),
    _A11Esmlogindex_Type()
)
a11Esmlogindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a11Esmlogindex.setStatus("mandatory")
_A11Esmlogdata_Type = DmiDisplaystring
_A11Esmlogdata_Object = MibTableColumn
a11Esmlogdata = _A11Esmlogdata_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 11, 1, 2),
    _A11Esmlogdata_Type()
)
a11Esmlogdata.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a11Esmlogdata.setStatus("mandatory")
_TPostEventLog_Object = MibTable
tPostEventLog = _TPostEventLog_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 12)
)
if mibBuilder.loadTexts:
    tPostEventLog.setStatus("mandatory")
_EPostEventLog_Object = MibTableRow
ePostEventLog = _EPostEventLog_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 12, 1)
)
ePostEventLog.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a12Postlogindex"),
)
if mibBuilder.loadTexts:
    ePostEventLog.setStatus("mandatory")
_A12Postlogindex_Type = DmiInteger
_A12Postlogindex_Object = MibTableColumn
a12Postlogindex = _A12Postlogindex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 12, 1, 1),
    _A12Postlogindex_Type()
)
a12Postlogindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12Postlogindex.setStatus("mandatory")
_A12Postlogdata_Type = DmiOctetstring
_A12Postlogdata_Object = MibTableColumn
a12Postlogdata = _A12Postlogdata_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 12, 1, 2),
    _A12Postlogdata_Type()
)
a12Postlogdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a12Postlogdata.setStatus("mandatory")
_TUserSecurityGroup_Object = MibTable
tUserSecurityGroup = _TUserSecurityGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 13)
)
if mibBuilder.loadTexts:
    tUserSecurityGroup.setStatus("mandatory")
_EUserSecurityGroup_Object = MibTableRow
eUserSecurityGroup = _EUserSecurityGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 13, 1)
)
eUserSecurityGroup.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a13UserIndex"),
)
if mibBuilder.loadTexts:
    eUserSecurityGroup.setStatus("mandatory")
_A13UserIndex_Type = DmiInteger
_A13UserIndex_Object = MibTableColumn
a13UserIndex = _A13UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 13, 1, 1),
    _A13UserIndex_Type()
)
a13UserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13UserIndex.setStatus("mandatory")
_A13UserName_Type = DmiDisplaystring
_A13UserName_Object = MibTableColumn
a13UserName = _A13UserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 13, 1, 2),
    _A13UserName_Type()
)
a13UserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a13UserName.setStatus("mandatory")
_A13UserControl_Type = DmiDisplaystring
_A13UserControl_Object = MibTableColumn
a13UserControl = _A13UserControl_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 13, 1, 3),
    _A13UserControl_Type()
)
a13UserControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a13UserControl.setStatus("mandatory")
_TDialupControl_Object = MibTable
tDialupControl = _TDialupControl_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 14)
)
if mibBuilder.loadTexts:
    tDialupControl.setStatus("mandatory")
_EDialupControl_Object = MibTableRow
eDialupControl = _EDialupControl_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 14, 1)
)
eDialupControl.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eDialupControl.setStatus("mandatory")


class _A14DialupCapability_Type(Integer32):
    """Custom type a14DialupCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A14DialupCapability_Type.__name__ = "Integer32"
_A14DialupCapability_Object = MibTableColumn
a14DialupCapability = _A14DialupCapability_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 14, 1, 1),
    _A14DialupCapability_Type()
)
a14DialupCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a14DialupCapability.setStatus("mandatory")
_A14CallbackNumber_Type = DmiDisplaystring
_A14CallbackNumber_Object = MibTableColumn
a14CallbackNumber = _A14CallbackNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 14, 1, 2),
    _A14CallbackNumber_Type()
)
a14CallbackNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a14CallbackNumber.setStatus("mandatory")
_TFirmwareInformation_Object = MibTable
tFirmwareInformation = _TFirmwareInformation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 15)
)
if mibBuilder.loadTexts:
    tFirmwareInformation.setStatus("mandatory")
_EFirmwareInformation_Object = MibTableRow
eFirmwareInformation = _EFirmwareInformation_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 15, 1)
)
eFirmwareInformation.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a15FirmwareChassisIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a15FirmwareIndex"),
)
if mibBuilder.loadTexts:
    eFirmwareInformation.setStatus("mandatory")
_A15FirmwareChassisIndex_Type = DmiInteger
_A15FirmwareChassisIndex_Object = MibTableColumn
a15FirmwareChassisIndex = _A15FirmwareChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 15, 1, 1),
    _A15FirmwareChassisIndex_Type()
)
a15FirmwareChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a15FirmwareChassisIndex.setStatus("mandatory")
_A15FirmwareIndex_Type = DmiInteger
_A15FirmwareIndex_Object = MibTableColumn
a15FirmwareIndex = _A15FirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 15, 1, 2),
    _A15FirmwareIndex_Type()
)
a15FirmwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a15FirmwareIndex.setStatus("mandatory")


class _A15FirmwareType_Type(Integer32):
    """Custom type a15FirmwareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vBackplane", 6),
          ("vBios", 3),
          ("vEsm", 4),
          ("vOther", 1),
          ("vPspb", 5),
          ("vUnknown", 2))
    )


_A15FirmwareType_Type.__name__ = "Integer32"
_A15FirmwareType_Object = MibTableColumn
a15FirmwareType = _A15FirmwareType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 15, 1, 3),
    _A15FirmwareType_Type()
)
a15FirmwareType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a15FirmwareType.setStatus("mandatory")
_A15FirmwareVersion_Type = DmiDisplaystring
_A15FirmwareVersion_Object = MibTableColumn
a15FirmwareVersion = _A15FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 15, 1, 4),
    _A15FirmwareVersion_Type()
)
a15FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a15FirmwareVersion.setStatus("mandatory")


class _A15FirmwareStatus_Type(Integer32):
    """Custom type a15FirmwareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 5),
          ("vNon-critical", 4),
          ("vNon-recoverable", 6),
          ("vOk", 3),
          ("vOther", 1),
          ("vUnknown", 2))
    )


_A15FirmwareStatus_Type.__name__ = "Integer32"
_A15FirmwareStatus_Object = MibTableColumn
a15FirmwareStatus = _A15FirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 15, 1, 5),
    _A15FirmwareStatus_Type()
)
a15FirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a15FirmwareStatus.setStatus("mandatory")
_TMiftomib_Object = MibTable
tMiftomib = _TMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 99)
)
if mibBuilder.loadTexts:
    tMiftomib.setStatus("mandatory")
_EMiftomib_Object = MibTableRow
eMiftomib = _EMiftomib_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 99, 1)
)
eMiftomib.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eMiftomib.setStatus("mandatory")
_A99DellBaseboardMib_Type = DmiDisplaystring
_A99DellBaseboardMib_Object = MibTableColumn
a99DellBaseboardMib = _A99DellBaseboardMib_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 99, 1, 1),
    _A99DellBaseboardMib_Type()
)
a99DellBaseboardMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99DellBaseboardMib.setStatus("mandatory")
_A99MibOid_Type = DmiDisplaystring
_A99MibOid_Object = MibTableColumn
a99MibOid = _A99MibOid_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 99, 1, 2),
    _A99MibOid_Type()
)
a99MibOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99MibOid.setStatus("mandatory")
_A99DisableTraps_Type = DmiInteger
_A99DisableTraps_Object = MibTableColumn
a99DisableTraps = _A99DisableTraps_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 99, 1, 3),
    _A99DisableTraps_Type()
)
a99DisableTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a99DisableTraps.setStatus("mandatory")
_TTemperatureProbeAlerts_Object = MibTable
tTemperatureProbeAlerts = _TTemperatureProbeAlerts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102)
)
if mibBuilder.loadTexts:
    tTemperatureProbeAlerts.setStatus("mandatory")
_ETemperatureProbeAlerts_Object = MibTableRow
eTemperatureProbeAlerts = _ETemperatureProbeAlerts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102, 1)
)
eTemperatureProbeAlerts.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a102AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eTemperatureProbeAlerts.setStatus("mandatory")


class _A102EventType_Type(Integer32):
    """Custom type a102EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vCoolingDeviceStatusChange", 1)
    )


_A102EventType_Type.__name__ = "Integer32"
_A102EventType_Object = MibTableColumn
a102EventType = _A102EventType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102, 1, 1),
    _A102EventType_Type()
)
a102EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a102EventType.setStatus("mandatory")


class _A102EventSeverity_Type(Integer32):
    """Custom type a102EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A102EventSeverity_Type.__name__ = "Integer32"
_A102EventSeverity_Object = MibTableColumn
a102EventSeverity = _A102EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102, 1, 2),
    _A102EventSeverity_Type()
)
a102EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a102EventSeverity.setStatus("mandatory")


class _A102IsEventStateBased_Type(Integer32):
    """Custom type a102IsEventStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A102IsEventStateBased_Type.__name__ = "Integer32"
_A102IsEventStateBased_Object = MibTableColumn
a102IsEventStateBased = _A102IsEventStateBased_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102, 1, 3),
    _A102IsEventStateBased_Type()
)
a102IsEventStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a102IsEventStateBased.setStatus("mandatory")
_A102EventStateKey_Type = DmiInteger
_A102EventStateKey_Object = MibTableColumn
a102EventStateKey = _A102EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102, 1, 4),
    _A102EventStateKey_Type()
)
a102EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a102EventStateKey.setStatus("mandatory")
_A102AssociatedGroup_Type = DmiDisplaystring
_A102AssociatedGroup_Object = MibTableColumn
a102AssociatedGroup = _A102AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102, 1, 5),
    _A102AssociatedGroup_Type()
)
a102AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a102AssociatedGroup.setStatus("mandatory")
_A102EventSystem_Type = DmiInteger
_A102EventSystem_Object = MibTableColumn
a102EventSystem = _A102EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102, 1, 6),
    _A102EventSystem_Type()
)
a102EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a102EventSystem.setStatus("mandatory")
_A102EventSubsystem_Type = DmiInteger
_A102EventSubsystem_Object = MibTableColumn
a102EventSubsystem = _A102EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102, 1, 7),
    _A102EventSubsystem_Type()
)
a102EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a102EventSubsystem.setStatus("mandatory")


class _A102EventSolution_Type(Integer32):
    """Custom type a102EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A102EventSolution_Type.__name__ = "Integer32"
_A102EventSolution_Object = MibTableColumn
a102EventSolution = _A102EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102, 1, 8),
    _A102EventSolution_Type()
)
a102EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a102EventSolution.setStatus("mandatory")


class _A102InstanceDataPresent_Type(Integer32):
    """Custom type a102InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A102InstanceDataPresent_Type.__name__ = "Integer32"
_A102InstanceDataPresent_Object = MibTableColumn
a102InstanceDataPresent = _A102InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102, 1, 9),
    _A102InstanceDataPresent_Type()
)
a102InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a102InstanceDataPresent.setStatus("mandatory")
_A102VendorSpecificMessage_Type = DmiDisplaystring
_A102VendorSpecificMessage_Object = MibTableColumn
a102VendorSpecificMessage = _A102VendorSpecificMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102, 1, 10),
    _A102VendorSpecificMessage_Type()
)
a102VendorSpecificMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a102VendorSpecificMessage.setStatus("mandatory")
_A102VendorSpecificData_Type = DmiOctetstring
_A102VendorSpecificData_Object = MibTableColumn
a102VendorSpecificData = _A102VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102, 1, 11),
    _A102VendorSpecificData_Type()
)
a102VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a102VendorSpecificData.setStatus("mandatory")
_A102VendorTrapNumber_Type = DmiInteger
_A102VendorTrapNumber_Object = MibTableColumn
a102VendorTrapNumber = _A102VendorTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 102, 1, 12),
    _A102VendorTrapNumber_Type()
)
a102VendorTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a102VendorTrapNumber.setStatus("mandatory")
_TFanSensorAlerts_Object = MibTable
tFanSensorAlerts = _TFanSensorAlerts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103)
)
if mibBuilder.loadTexts:
    tFanSensorAlerts.setStatus("mandatory")
_EFanSensorAlerts_Object = MibTableRow
eFanSensorAlerts = _EFanSensorAlerts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103, 1)
)
eFanSensorAlerts.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a103AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eFanSensorAlerts.setStatus("mandatory")


class _A103EventType_Type(Integer32):
    """Custom type a103EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vCoolingDeviceStatusChange", 1)
    )


_A103EventType_Type.__name__ = "Integer32"
_A103EventType_Object = MibTableColumn
a103EventType = _A103EventType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103, 1, 1),
    _A103EventType_Type()
)
a103EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103EventType.setStatus("mandatory")


class _A103EventSeverity_Type(Integer32):
    """Custom type a103EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A103EventSeverity_Type.__name__ = "Integer32"
_A103EventSeverity_Object = MibTableColumn
a103EventSeverity = _A103EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103, 1, 2),
    _A103EventSeverity_Type()
)
a103EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103EventSeverity.setStatus("mandatory")


class _A103IsEventStateBased_Type(Integer32):
    """Custom type a103IsEventStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A103IsEventStateBased_Type.__name__ = "Integer32"
_A103IsEventStateBased_Object = MibTableColumn
a103IsEventStateBased = _A103IsEventStateBased_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103, 1, 3),
    _A103IsEventStateBased_Type()
)
a103IsEventStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103IsEventStateBased.setStatus("mandatory")
_A103EventStateKey_Type = DmiInteger
_A103EventStateKey_Object = MibTableColumn
a103EventStateKey = _A103EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103, 1, 4),
    _A103EventStateKey_Type()
)
a103EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103EventStateKey.setStatus("mandatory")
_A103AssociatedGroup_Type = DmiDisplaystring
_A103AssociatedGroup_Object = MibTableColumn
a103AssociatedGroup = _A103AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103, 1, 5),
    _A103AssociatedGroup_Type()
)
a103AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103AssociatedGroup.setStatus("mandatory")
_A103EventSystem_Type = DmiInteger
_A103EventSystem_Object = MibTableColumn
a103EventSystem = _A103EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103, 1, 6),
    _A103EventSystem_Type()
)
a103EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103EventSystem.setStatus("mandatory")
_A103EventSubsystem_Type = DmiInteger
_A103EventSubsystem_Object = MibTableColumn
a103EventSubsystem = _A103EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103, 1, 7),
    _A103EventSubsystem_Type()
)
a103EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103EventSubsystem.setStatus("mandatory")


class _A103EventSolution_Type(Integer32):
    """Custom type a103EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A103EventSolution_Type.__name__ = "Integer32"
_A103EventSolution_Object = MibTableColumn
a103EventSolution = _A103EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103, 1, 8),
    _A103EventSolution_Type()
)
a103EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103EventSolution.setStatus("mandatory")


class _A103InstanceDataPresent_Type(Integer32):
    """Custom type a103InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A103InstanceDataPresent_Type.__name__ = "Integer32"
_A103InstanceDataPresent_Object = MibTableColumn
a103InstanceDataPresent = _A103InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103, 1, 9),
    _A103InstanceDataPresent_Type()
)
a103InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103InstanceDataPresent.setStatus("mandatory")
_A103VendorSpecificMessage_Type = DmiDisplaystring
_A103VendorSpecificMessage_Object = MibTableColumn
a103VendorSpecificMessage = _A103VendorSpecificMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103, 1, 10),
    _A103VendorSpecificMessage_Type()
)
a103VendorSpecificMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103VendorSpecificMessage.setStatus("mandatory")
_A103VendorSpecificData_Type = DmiOctetstring
_A103VendorSpecificData_Object = MibTableColumn
a103VendorSpecificData = _A103VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103, 1, 11),
    _A103VendorSpecificData_Type()
)
a103VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103VendorSpecificData.setStatus("mandatory")
_A103VendorTrapNumber_Type = DmiInteger
_A103VendorTrapNumber_Object = MibTableColumn
a103VendorTrapNumber = _A103VendorTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 103, 1, 12),
    _A103VendorTrapNumber_Type()
)
a103VendorTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a103VendorTrapNumber.setStatus("mandatory")
_TVoltageProbeAlerts_Object = MibTable
tVoltageProbeAlerts = _TVoltageProbeAlerts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104)
)
if mibBuilder.loadTexts:
    tVoltageProbeAlerts.setStatus("mandatory")
_EVoltageProbeAlerts_Object = MibTableRow
eVoltageProbeAlerts = _EVoltageProbeAlerts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104, 1)
)
eVoltageProbeAlerts.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a104AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eVoltageProbeAlerts.setStatus("mandatory")


class _A104EventType_Type(Integer32):
    """Custom type a104EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vPowerSupplyStatusChange", 1)
    )


_A104EventType_Type.__name__ = "Integer32"
_A104EventType_Object = MibTableColumn
a104EventType = _A104EventType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104, 1, 1),
    _A104EventType_Type()
)
a104EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventType.setStatus("mandatory")


class _A104EventSeverity_Type(Integer32):
    """Custom type a104EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A104EventSeverity_Type.__name__ = "Integer32"
_A104EventSeverity_Object = MibTableColumn
a104EventSeverity = _A104EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104, 1, 2),
    _A104EventSeverity_Type()
)
a104EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventSeverity.setStatus("mandatory")


class _A104IsEventStateBased_Type(Integer32):
    """Custom type a104IsEventStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A104IsEventStateBased_Type.__name__ = "Integer32"
_A104IsEventStateBased_Object = MibTableColumn
a104IsEventStateBased = _A104IsEventStateBased_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104, 1, 3),
    _A104IsEventStateBased_Type()
)
a104IsEventStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104IsEventStateBased.setStatus("mandatory")
_A104EventStateKey_Type = DmiInteger
_A104EventStateKey_Object = MibTableColumn
a104EventStateKey = _A104EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104, 1, 4),
    _A104EventStateKey_Type()
)
a104EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventStateKey.setStatus("mandatory")
_A104AssociatedGroup_Type = DmiDisplaystring
_A104AssociatedGroup_Object = MibTableColumn
a104AssociatedGroup = _A104AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104, 1, 5),
    _A104AssociatedGroup_Type()
)
a104AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104AssociatedGroup.setStatus("mandatory")
_A104EventSystem_Type = DmiInteger
_A104EventSystem_Object = MibTableColumn
a104EventSystem = _A104EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104, 1, 6),
    _A104EventSystem_Type()
)
a104EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventSystem.setStatus("mandatory")
_A104EventSubsystem_Type = DmiInteger
_A104EventSubsystem_Object = MibTableColumn
a104EventSubsystem = _A104EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104, 1, 7),
    _A104EventSubsystem_Type()
)
a104EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventSubsystem.setStatus("mandatory")


class _A104EventSolution_Type(Integer32):
    """Custom type a104EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A104EventSolution_Type.__name__ = "Integer32"
_A104EventSolution_Object = MibTableColumn
a104EventSolution = _A104EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104, 1, 8),
    _A104EventSolution_Type()
)
a104EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104EventSolution.setStatus("mandatory")


class _A104InstanceDataPresent_Type(Integer32):
    """Custom type a104InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A104InstanceDataPresent_Type.__name__ = "Integer32"
_A104InstanceDataPresent_Object = MibTableColumn
a104InstanceDataPresent = _A104InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104, 1, 9),
    _A104InstanceDataPresent_Type()
)
a104InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104InstanceDataPresent.setStatus("mandatory")
_A104VendorSpecificMessage_Type = DmiDisplaystring
_A104VendorSpecificMessage_Object = MibTableColumn
a104VendorSpecificMessage = _A104VendorSpecificMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104, 1, 10),
    _A104VendorSpecificMessage_Type()
)
a104VendorSpecificMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104VendorSpecificMessage.setStatus("mandatory")
_A104VendorSpecificData_Type = DmiOctetstring
_A104VendorSpecificData_Object = MibTableColumn
a104VendorSpecificData = _A104VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104, 1, 11),
    _A104VendorSpecificData_Type()
)
a104VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104VendorSpecificData.setStatus("mandatory")
_A104VendorTrapNumber_Type = DmiInteger
_A104VendorTrapNumber_Object = MibTableColumn
a104VendorTrapNumber = _A104VendorTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 104, 1, 12),
    _A104VendorTrapNumber_Type()
)
a104VendorTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a104VendorTrapNumber.setStatus("mandatory")
_TCurrentProbeAlerts_Object = MibTable
tCurrentProbeAlerts = _TCurrentProbeAlerts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105)
)
if mibBuilder.loadTexts:
    tCurrentProbeAlerts.setStatus("mandatory")
_ECurrentProbeAlerts_Object = MibTableRow
eCurrentProbeAlerts = _ECurrentProbeAlerts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105, 1)
)
eCurrentProbeAlerts.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a105AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eCurrentProbeAlerts.setStatus("mandatory")


class _A105EventType_Type(Integer32):
    """Custom type a105EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vPowerSupplyStatusChange", 1)
    )


_A105EventType_Type.__name__ = "Integer32"
_A105EventType_Object = MibTableColumn
a105EventType = _A105EventType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105, 1, 1),
    _A105EventType_Type()
)
a105EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a105EventType.setStatus("mandatory")


class _A105EventSeverity_Type(Integer32):
    """Custom type a105EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A105EventSeverity_Type.__name__ = "Integer32"
_A105EventSeverity_Object = MibTableColumn
a105EventSeverity = _A105EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105, 1, 2),
    _A105EventSeverity_Type()
)
a105EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a105EventSeverity.setStatus("mandatory")


class _A105IsEventStateBased_Type(Integer32):
    """Custom type a105IsEventStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A105IsEventStateBased_Type.__name__ = "Integer32"
_A105IsEventStateBased_Object = MibTableColumn
a105IsEventStateBased = _A105IsEventStateBased_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105, 1, 3),
    _A105IsEventStateBased_Type()
)
a105IsEventStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a105IsEventStateBased.setStatus("mandatory")
_A105EventStateKey_Type = DmiInteger
_A105EventStateKey_Object = MibTableColumn
a105EventStateKey = _A105EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105, 1, 4),
    _A105EventStateKey_Type()
)
a105EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a105EventStateKey.setStatus("mandatory")
_A105AssociatedGroup_Type = DmiDisplaystring
_A105AssociatedGroup_Object = MibTableColumn
a105AssociatedGroup = _A105AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105, 1, 5),
    _A105AssociatedGroup_Type()
)
a105AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a105AssociatedGroup.setStatus("mandatory")
_A105EventSystem_Type = DmiInteger
_A105EventSystem_Object = MibTableColumn
a105EventSystem = _A105EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105, 1, 6),
    _A105EventSystem_Type()
)
a105EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a105EventSystem.setStatus("mandatory")
_A105EventSubsystem_Type = DmiInteger
_A105EventSubsystem_Object = MibTableColumn
a105EventSubsystem = _A105EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105, 1, 7),
    _A105EventSubsystem_Type()
)
a105EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a105EventSubsystem.setStatus("mandatory")


class _A105EventSolution_Type(Integer32):
    """Custom type a105EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A105EventSolution_Type.__name__ = "Integer32"
_A105EventSolution_Object = MibTableColumn
a105EventSolution = _A105EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105, 1, 8),
    _A105EventSolution_Type()
)
a105EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a105EventSolution.setStatus("mandatory")


class _A105InstanceDataPresent_Type(Integer32):
    """Custom type a105InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A105InstanceDataPresent_Type.__name__ = "Integer32"
_A105InstanceDataPresent_Object = MibTableColumn
a105InstanceDataPresent = _A105InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105, 1, 9),
    _A105InstanceDataPresent_Type()
)
a105InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a105InstanceDataPresent.setStatus("mandatory")
_A105VendorSpecificMessage_Type = DmiDisplaystring
_A105VendorSpecificMessage_Object = MibTableColumn
a105VendorSpecificMessage = _A105VendorSpecificMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105, 1, 10),
    _A105VendorSpecificMessage_Type()
)
a105VendorSpecificMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a105VendorSpecificMessage.setStatus("mandatory")
_A105VendorSpecificData_Type = DmiOctetstring
_A105VendorSpecificData_Object = MibTableColumn
a105VendorSpecificData = _A105VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105, 1, 11),
    _A105VendorSpecificData_Type()
)
a105VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a105VendorSpecificData.setStatus("mandatory")
_A105VendorTrapNumber_Type = DmiInteger
_A105VendorTrapNumber_Object = MibTableColumn
a105VendorTrapNumber = _A105VendorTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 105, 1, 12),
    _A105VendorTrapNumber_Type()
)
a105VendorTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a105VendorTrapNumber.setStatus("mandatory")
_TPowerUnitAlerts_Object = MibTable
tPowerUnitAlerts = _TPowerUnitAlerts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107)
)
if mibBuilder.loadTexts:
    tPowerUnitAlerts.setStatus("mandatory")
_EPowerUnitAlerts_Object = MibTableRow
ePowerUnitAlerts = _EPowerUnitAlerts_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107, 1)
)
ePowerUnitAlerts.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a107AssociatedGroup"),
)
if mibBuilder.loadTexts:
    ePowerUnitAlerts.setStatus("mandatory")


class _A107EventType_Type(Integer32):
    """Custom type a107EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vPowerSupplyRedundancyChange", 1),
          ("vPowerSupplyStatusChange", 2))
    )


_A107EventType_Type.__name__ = "Integer32"
_A107EventType_Object = MibTableColumn
a107EventType = _A107EventType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107, 1, 1),
    _A107EventType_Type()
)
a107EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a107EventType.setStatus("mandatory")


class _A107EventSeverity_Type(Integer32):
    """Custom type a107EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A107EventSeverity_Type.__name__ = "Integer32"
_A107EventSeverity_Object = MibTableColumn
a107EventSeverity = _A107EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107, 1, 2),
    _A107EventSeverity_Type()
)
a107EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a107EventSeverity.setStatus("mandatory")


class _A107IsEventStateBased_Type(Integer32):
    """Custom type a107IsEventStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A107IsEventStateBased_Type.__name__ = "Integer32"
_A107IsEventStateBased_Object = MibTableColumn
a107IsEventStateBased = _A107IsEventStateBased_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107, 1, 3),
    _A107IsEventStateBased_Type()
)
a107IsEventStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a107IsEventStateBased.setStatus("mandatory")
_A107EventStateKey_Type = DmiInteger
_A107EventStateKey_Object = MibTableColumn
a107EventStateKey = _A107EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107, 1, 4),
    _A107EventStateKey_Type()
)
a107EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a107EventStateKey.setStatus("mandatory")
_A107AssociatedGroup_Type = DmiDisplaystring
_A107AssociatedGroup_Object = MibTableColumn
a107AssociatedGroup = _A107AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107, 1, 5),
    _A107AssociatedGroup_Type()
)
a107AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a107AssociatedGroup.setStatus("mandatory")
_A107EventSystem_Type = DmiInteger
_A107EventSystem_Object = MibTableColumn
a107EventSystem = _A107EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107, 1, 6),
    _A107EventSystem_Type()
)
a107EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a107EventSystem.setStatus("mandatory")
_A107EventSubsystem_Type = DmiInteger
_A107EventSubsystem_Object = MibTableColumn
a107EventSubsystem = _A107EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107, 1, 7),
    _A107EventSubsystem_Type()
)
a107EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a107EventSubsystem.setStatus("mandatory")


class _A107EventSolution_Type(Integer32):
    """Custom type a107EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A107EventSolution_Type.__name__ = "Integer32"
_A107EventSolution_Object = MibTableColumn
a107EventSolution = _A107EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107, 1, 8),
    _A107EventSolution_Type()
)
a107EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a107EventSolution.setStatus("mandatory")


class _A107InstanceDataPresent_Type(Integer32):
    """Custom type a107InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A107InstanceDataPresent_Type.__name__ = "Integer32"
_A107InstanceDataPresent_Object = MibTableColumn
a107InstanceDataPresent = _A107InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107, 1, 9),
    _A107InstanceDataPresent_Type()
)
a107InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a107InstanceDataPresent.setStatus("mandatory")
_A107VendorSpecificMessage_Type = DmiDisplaystring
_A107VendorSpecificMessage_Object = MibTableColumn
a107VendorSpecificMessage = _A107VendorSpecificMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107, 1, 10),
    _A107VendorSpecificMessage_Type()
)
a107VendorSpecificMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a107VendorSpecificMessage.setStatus("mandatory")
_A107VendorSpecificData_Type = DmiOctetstring
_A107VendorSpecificData_Object = MibTableColumn
a107VendorSpecificData = _A107VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107, 1, 11),
    _A107VendorSpecificData_Type()
)
a107VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a107VendorSpecificData.setStatus("mandatory")
_A107VendorTrapNumber_Type = DmiInteger
_A107VendorTrapNumber_Object = MibTableColumn
a107VendorTrapNumber = _A107VendorTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 107, 1, 12),
    _A107VendorTrapNumber_Type()
)
a107VendorTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a107VendorTrapNumber.setStatus("mandatory")
_TChassisEventGeneration_Object = MibTable
tChassisEventGeneration = _TChassisEventGeneration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108)
)
if mibBuilder.loadTexts:
    tChassisEventGeneration.setStatus("mandatory")
_EChassisEventGeneration_Object = MibTableRow
eChassisEventGeneration = _EChassisEventGeneration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108, 1)
)
eChassisEventGeneration.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a108AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eChassisEventGeneration.setStatus("mandatory")


class _A108EventType_Type(Integer32):
    """Custom type a108EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vMemoryEccError", 1)
    )


_A108EventType_Type.__name__ = "Integer32"
_A108EventType_Object = MibTableColumn
a108EventType = _A108EventType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108, 1, 1),
    _A108EventType_Type()
)
a108EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108EventType.setStatus("mandatory")


class _A108EventSeverity_Type(Integer32):
    """Custom type a108EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A108EventSeverity_Type.__name__ = "Integer32"
_A108EventSeverity_Object = MibTableColumn
a108EventSeverity = _A108EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108, 1, 2),
    _A108EventSeverity_Type()
)
a108EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108EventSeverity.setStatus("mandatory")


class _A108IsEventStateBased_Type(Integer32):
    """Custom type a108IsEventStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A108IsEventStateBased_Type.__name__ = "Integer32"
_A108IsEventStateBased_Object = MibTableColumn
a108IsEventStateBased = _A108IsEventStateBased_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108, 1, 3),
    _A108IsEventStateBased_Type()
)
a108IsEventStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108IsEventStateBased.setStatus("mandatory")
_A108EventStateKey_Type = DmiInteger
_A108EventStateKey_Object = MibTableColumn
a108EventStateKey = _A108EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108, 1, 4),
    _A108EventStateKey_Type()
)
a108EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108EventStateKey.setStatus("mandatory")
_A108AssociatedGroup_Type = DmiDisplaystring
_A108AssociatedGroup_Object = MibTableColumn
a108AssociatedGroup = _A108AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108, 1, 5),
    _A108AssociatedGroup_Type()
)
a108AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108AssociatedGroup.setStatus("mandatory")
_A108EventSystem_Type = DmiInteger
_A108EventSystem_Object = MibTableColumn
a108EventSystem = _A108EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108, 1, 6),
    _A108EventSystem_Type()
)
a108EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108EventSystem.setStatus("mandatory")
_A108EventSubsystem_Type = DmiInteger
_A108EventSubsystem_Object = MibTableColumn
a108EventSubsystem = _A108EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108, 1, 7),
    _A108EventSubsystem_Type()
)
a108EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108EventSubsystem.setStatus("mandatory")


class _A108EventSolution_Type(Integer32):
    """Custom type a108EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A108EventSolution_Type.__name__ = "Integer32"
_A108EventSolution_Object = MibTableColumn
a108EventSolution = _A108EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108, 1, 8),
    _A108EventSolution_Type()
)
a108EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108EventSolution.setStatus("mandatory")


class _A108InstanceDataPresent_Type(Integer32):
    """Custom type a108InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A108InstanceDataPresent_Type.__name__ = "Integer32"
_A108InstanceDataPresent_Object = MibTableColumn
a108InstanceDataPresent = _A108InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108, 1, 9),
    _A108InstanceDataPresent_Type()
)
a108InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108InstanceDataPresent.setStatus("mandatory")
_A108VendorSpecificMessage_Type = DmiDisplaystring
_A108VendorSpecificMessage_Object = MibTableColumn
a108VendorSpecificMessage = _A108VendorSpecificMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108, 1, 10),
    _A108VendorSpecificMessage_Type()
)
a108VendorSpecificMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108VendorSpecificMessage.setStatus("mandatory")
_A108VendorSpecificData_Type = DmiOctetstring
_A108VendorSpecificData_Object = MibTableColumn
a108VendorSpecificData = _A108VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108, 1, 11),
    _A108VendorSpecificData_Type()
)
a108VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108VendorSpecificData.setStatus("mandatory")
_A108VendorTrapNumber_Type = DmiInteger
_A108VendorTrapNumber_Object = MibTableColumn
a108VendorTrapNumber = _A108VendorTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 108, 1, 12),
    _A108VendorTrapNumber_Type()
)
a108VendorTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a108VendorTrapNumber.setStatus("mandatory")
_TContainerEventGeneration_Object = MibTable
tContainerEventGeneration = _TContainerEventGeneration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109)
)
if mibBuilder.loadTexts:
    tContainerEventGeneration.setStatus("mandatory")
_EContainerEventGeneration_Object = MibTableRow
eContainerEventGeneration = _EContainerEventGeneration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109, 1)
)
eContainerEventGeneration.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a109AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eContainerEventGeneration.setStatus("mandatory")


class _A109EventType_Type(Integer32):
    """Custom type a109EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("vConfigurationError", 7),
          ("vContainerSecurityBreach", 6),
          ("vCoolingDeviceStatusChange", 3),
          ("vLogicalDeviceStatusChange", 5),
          ("vPhysicalDeviceStatusChange", 4),
          ("vPowerSupplyStatusChange", 2),
          ("vSecuritySettingsChange", 1))
    )


_A109EventType_Type.__name__ = "Integer32"
_A109EventType_Object = MibTableColumn
a109EventType = _A109EventType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109, 1, 1),
    _A109EventType_Type()
)
a109EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a109EventType.setStatus("mandatory")


class _A109EventSeverity_Type(Integer32):
    """Custom type a109EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A109EventSeverity_Type.__name__ = "Integer32"
_A109EventSeverity_Object = MibTableColumn
a109EventSeverity = _A109EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109, 1, 2),
    _A109EventSeverity_Type()
)
a109EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a109EventSeverity.setStatus("mandatory")


class _A109IsEventStateBased_Type(Integer32):
    """Custom type a109IsEventStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A109IsEventStateBased_Type.__name__ = "Integer32"
_A109IsEventStateBased_Object = MibTableColumn
a109IsEventStateBased = _A109IsEventStateBased_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109, 1, 3),
    _A109IsEventStateBased_Type()
)
a109IsEventStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a109IsEventStateBased.setStatus("mandatory")
_A109EventStateKey_Type = DmiInteger
_A109EventStateKey_Object = MibTableColumn
a109EventStateKey = _A109EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109, 1, 4),
    _A109EventStateKey_Type()
)
a109EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a109EventStateKey.setStatus("mandatory")
_A109AssociatedGroup_Type = DmiDisplaystring
_A109AssociatedGroup_Object = MibTableColumn
a109AssociatedGroup = _A109AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109, 1, 5),
    _A109AssociatedGroup_Type()
)
a109AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a109AssociatedGroup.setStatus("mandatory")
_A109EventSystem_Type = DmiInteger
_A109EventSystem_Object = MibTableColumn
a109EventSystem = _A109EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109, 1, 6),
    _A109EventSystem_Type()
)
a109EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a109EventSystem.setStatus("mandatory")
_A109EventSubsystem_Type = DmiInteger
_A109EventSubsystem_Object = MibTableColumn
a109EventSubsystem = _A109EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109, 1, 7),
    _A109EventSubsystem_Type()
)
a109EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a109EventSubsystem.setStatus("mandatory")


class _A109EventSolution_Type(Integer32):
    """Custom type a109EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A109EventSolution_Type.__name__ = "Integer32"
_A109EventSolution_Object = MibTableColumn
a109EventSolution = _A109EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109, 1, 8),
    _A109EventSolution_Type()
)
a109EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a109EventSolution.setStatus("mandatory")


class _A109InstanceDataPresent_Type(Integer32):
    """Custom type a109InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A109InstanceDataPresent_Type.__name__ = "Integer32"
_A109InstanceDataPresent_Object = MibTableColumn
a109InstanceDataPresent = _A109InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109, 1, 9),
    _A109InstanceDataPresent_Type()
)
a109InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a109InstanceDataPresent.setStatus("mandatory")
_A109VendorSpecificMessage_Type = DmiDisplaystring
_A109VendorSpecificMessage_Object = MibTableColumn
a109VendorSpecificMessage = _A109VendorSpecificMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109, 1, 10),
    _A109VendorSpecificMessage_Type()
)
a109VendorSpecificMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a109VendorSpecificMessage.setStatus("mandatory")
_A109VendorSpecificData_Type = DmiOctetstring
_A109VendorSpecificData_Object = MibTableColumn
a109VendorSpecificData = _A109VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109, 1, 11),
    _A109VendorSpecificData_Type()
)
a109VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a109VendorSpecificData.setStatus("mandatory")
_A109VendorTrapNumber_Type = DmiInteger
_A109VendorTrapNumber_Object = MibTableColumn
a109VendorTrapNumber = _A109VendorTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 109, 1, 12),
    _A109VendorTrapNumber_Type()
)
a109VendorTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a109VendorTrapNumber.setStatus("mandatory")
_TResetEventGeneration_Object = MibTable
tResetEventGeneration = _TResetEventGeneration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110)
)
if mibBuilder.loadTexts:
    tResetEventGeneration.setStatus("mandatory")
_EResetEventGeneration_Object = MibTableRow
eResetEventGeneration = _EResetEventGeneration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110, 1)
)
eResetEventGeneration.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
    (0, "DELLBASEBOARDMIF-MIB", "a110AssociatedGroup"),
)
if mibBuilder.loadTexts:
    eResetEventGeneration.setStatus("mandatory")


class _A110EventType_Type(Integer32):
    """Custom type a110EventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vSystemUp", 1)
    )


_A110EventType_Type.__name__ = "Integer32"
_A110EventType_Object = MibTableColumn
a110EventType = _A110EventType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110, 1, 1),
    _A110EventType_Type()
)
a110EventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a110EventType.setStatus("mandatory")


class _A110EventSeverity_Type(Integer32):
    """Custom type a110EventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("vCritical", 10),
          ("vInformation", 2),
          ("vMonitor", 1),
          ("vNon-critical", 8),
          ("vNon-recoverable", 12),
          ("vOk", 4))
    )


_A110EventSeverity_Type.__name__ = "Integer32"
_A110EventSeverity_Object = MibTableColumn
a110EventSeverity = _A110EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110, 1, 2),
    _A110EventSeverity_Type()
)
a110EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a110EventSeverity.setStatus("mandatory")


class _A110IsEventStateBased_Type(Integer32):
    """Custom type a110IsEventStateBased based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A110IsEventStateBased_Type.__name__ = "Integer32"
_A110IsEventStateBased_Object = MibTableColumn
a110IsEventStateBased = _A110IsEventStateBased_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110, 1, 3),
    _A110IsEventStateBased_Type()
)
a110IsEventStateBased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a110IsEventStateBased.setStatus("mandatory")
_A110EventStateKey_Type = DmiInteger
_A110EventStateKey_Object = MibTableColumn
a110EventStateKey = _A110EventStateKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110, 1, 4),
    _A110EventStateKey_Type()
)
a110EventStateKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a110EventStateKey.setStatus("mandatory")
_A110AssociatedGroup_Type = DmiDisplaystring
_A110AssociatedGroup_Object = MibTableColumn
a110AssociatedGroup = _A110AssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110, 1, 5),
    _A110AssociatedGroup_Type()
)
a110AssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a110AssociatedGroup.setStatus("mandatory")
_A110EventSystem_Type = DmiInteger
_A110EventSystem_Object = MibTableColumn
a110EventSystem = _A110EventSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110, 1, 6),
    _A110EventSystem_Type()
)
a110EventSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a110EventSystem.setStatus("mandatory")
_A110EventSubsystem_Type = DmiInteger
_A110EventSubsystem_Object = MibTableColumn
a110EventSubsystem = _A110EventSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110, 1, 7),
    _A110EventSubsystem_Type()
)
a110EventSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a110EventSubsystem.setStatus("mandatory")


class _A110EventSolution_Type(Integer32):
    """Custom type a110EventSolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vOther", 1),
          ("vUnknown", 2))
    )


_A110EventSolution_Type.__name__ = "Integer32"
_A110EventSolution_Object = MibTableColumn
a110EventSolution = _A110EventSolution_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110, 1, 8),
    _A110EventSolution_Type()
)
a110EventSolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a110EventSolution.setStatus("mandatory")


class _A110InstanceDataPresent_Type(Integer32):
    """Custom type a110InstanceDataPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vFalse", 0),
          ("vTrue", 1))
    )


_A110InstanceDataPresent_Type.__name__ = "Integer32"
_A110InstanceDataPresent_Object = MibTableColumn
a110InstanceDataPresent = _A110InstanceDataPresent_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110, 1, 9),
    _A110InstanceDataPresent_Type()
)
a110InstanceDataPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a110InstanceDataPresent.setStatus("mandatory")
_A110VendorSpecificMessage_Type = DmiDisplaystring
_A110VendorSpecificMessage_Object = MibTableColumn
a110VendorSpecificMessage = _A110VendorSpecificMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110, 1, 10),
    _A110VendorSpecificMessage_Type()
)
a110VendorSpecificMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a110VendorSpecificMessage.setStatus("mandatory")
_A110VendorSpecificData_Type = DmiOctetstring
_A110VendorSpecificData_Object = MibTableColumn
a110VendorSpecificData = _A110VendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110, 1, 11),
    _A110VendorSpecificData_Type()
)
a110VendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a110VendorSpecificData.setStatus("mandatory")
_A110VendorTrapNumber_Type = DmiInteger
_A110VendorTrapNumber_Object = MibTableColumn
a110VendorTrapNumber = _A110VendorTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 110, 1, 12),
    _A110VendorTrapNumber_Type()
)
a110VendorTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a110VendorTrapNumber.setStatus("mandatory")
_TTrapGroup_Object = MibTable
tTrapGroup = _TTrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9999)
)
if mibBuilder.loadTexts:
    tTrapGroup.setStatus("mandatory")
_ETrapGroup_Object = MibTableRow
eTrapGroup = _ETrapGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9999, 1)
)
eTrapGroup.setIndexNames(
    (0, "DELLBASEBOARDMIF-MIB", "DmiComponentIndex"),
)
if mibBuilder.loadTexts:
    eTrapGroup.setStatus("mandatory")
_A9999AlertSystem_Type = OctetString
_A9999AlertSystem_Object = MibTableColumn
a9999AlertSystem = _A9999AlertSystem_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9999, 1, 1),
    _A9999AlertSystem_Type()
)
a9999AlertSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999AlertSystem.setStatus("mandatory")
_A9999AlertGroup_Type = OctetString
_A9999AlertGroup_Object = MibTableColumn
a9999AlertGroup = _A9999AlertGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9999, 1, 2),
    _A9999AlertGroup_Type()
)
a9999AlertGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999AlertGroup.setStatus("mandatory")
_A9999AlertMessage_Type = OctetString
_A9999AlertMessage_Object = MibTableColumn
a9999AlertMessage = _A9999AlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9999, 1, 3),
    _A9999AlertMessage_Type()
)
a9999AlertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999AlertMessage.setStatus("mandatory")
_A9999AlertSeverity_Type = DmiInteger
_A9999AlertSeverity_Object = MibTableColumn
a9999AlertSeverity = _A9999AlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9999, 1, 4),
    _A9999AlertSeverity_Type()
)
a9999AlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999AlertSeverity.setStatus("mandatory")
_A9999AlertData_Type = OctetString
_A9999AlertData_Object = MibTableColumn
a9999AlertData = _A9999AlertData_Object(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 1, 9999, 1, 5),
    _A9999AlertData_Type()
)
a9999AlertData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a9999AlertData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dmtfAlert260 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 260)
)
dmtfAlert260.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert260.setStatus(
        ""
    )

dmtfAlert261 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 261)
)
dmtfAlert261.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert261.setStatus(
        ""
    )

dmtfAlert268 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 268)
)
dmtfAlert268.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert268.setStatus(
        ""
    )

dmtfAlert269 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 269)
)
dmtfAlert269.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert269.setStatus(
        ""
    )

dmtfAlert272 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 272)
)
dmtfAlert272.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert272.setStatus(
        ""
    )

dmtfAlert273 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 273)
)
dmtfAlert273.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert273.setStatus(
        ""
    )

dmtfAlert300 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 300)
)
dmtfAlert300.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert300.setStatus(
        ""
    )

dmtfAlert301 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 301)
)
dmtfAlert301.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert301.setStatus(
        ""
    )

dmtfAlert302 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 302)
)
dmtfAlert302.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert302.setStatus(
        ""
    )

dmtfAlert303 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 303)
)
dmtfAlert303.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert303.setStatus(
        ""
    )

dmtfAlert304 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 304)
)
dmtfAlert304.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert304.setStatus(
        ""
    )

dmtfAlert305 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 305)
)
dmtfAlert305.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert305.setStatus(
        ""
    )

dmtfAlert306 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 306)
)
dmtfAlert306.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert306.setStatus(
        ""
    )

dmtfAlert307 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 307)
)
dmtfAlert307.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert307.setStatus(
        ""
    )

dmtfAlert308 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 308)
)
dmtfAlert308.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert308.setStatus(
        ""
    )

dmtfAlert309 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 309)
)
dmtfAlert309.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert309.setStatus(
        ""
    )

dmtfAlert310 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 310)
)
dmtfAlert310.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert310.setStatus(
        ""
    )

dmtfAlert311 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 311)
)
dmtfAlert311.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert311.setStatus(
        ""
    )

dmtfAlert312 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 312)
)
dmtfAlert312.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert312.setStatus(
        ""
    )

dmtfAlert313 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 313)
)
dmtfAlert313.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert313.setStatus(
        ""
    )

dmtfAlert314 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 314)
)
dmtfAlert314.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert314.setStatus(
        ""
    )

dmtfAlert315 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 315)
)
dmtfAlert315.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert315.setStatus(
        ""
    )

dmtfAlert320 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 320)
)
dmtfAlert320.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert320.setStatus(
        ""
    )

dmtfAlert321 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 321)
)
dmtfAlert321.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert321.setStatus(
        ""
    )

dmtfAlert323 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 323)
)
dmtfAlert323.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert323.setStatus(
        ""
    )

dmtfAlert325 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 325)
)
dmtfAlert325.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert325.setStatus(
        ""
    )

dmtfAlert326 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 326)
)
dmtfAlert326.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert326.setStatus(
        ""
    )

dmtfAlert327 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 327)
)
dmtfAlert327.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert327.setStatus(
        ""
    )

dmtfAlert330 = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10890, 1, 0, 330)
)
dmtfAlert330.setObjects(
      *(("DELLBASEBOARDMIF-MIB", "a9999AlertSystem"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertGroup"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertMessage"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertSeverity"),
        ("DELLBASEBOARDMIF-MIB", "a9999AlertData"))
)
if mibBuilder.loadTexts:
    dmtfAlert330.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELLBASEBOARDMIF-MIB",
    **{"DmiInteger": DmiInteger,
       "DmiOctetstring": DmiOctetstring,
       "DmiDisplaystring": DmiDisplaystring,
       "DmiComponentIndex": DmiComponentIndex,
       "dell": dell,
       "server": server,
       "baseboard": baseboard,
       "dmtfAlert260": dmtfAlert260,
       "dmtfAlert261": dmtfAlert261,
       "dmtfAlert268": dmtfAlert268,
       "dmtfAlert269": dmtfAlert269,
       "dmtfAlert272": dmtfAlert272,
       "dmtfAlert273": dmtfAlert273,
       "dmtfAlert300": dmtfAlert300,
       "dmtfAlert301": dmtfAlert301,
       "dmtfAlert302": dmtfAlert302,
       "dmtfAlert303": dmtfAlert303,
       "dmtfAlert304": dmtfAlert304,
       "dmtfAlert305": dmtfAlert305,
       "dmtfAlert306": dmtfAlert306,
       "dmtfAlert307": dmtfAlert307,
       "dmtfAlert308": dmtfAlert308,
       "dmtfAlert309": dmtfAlert309,
       "dmtfAlert310": dmtfAlert310,
       "dmtfAlert311": dmtfAlert311,
       "dmtfAlert312": dmtfAlert312,
       "dmtfAlert313": dmtfAlert313,
       "dmtfAlert314": dmtfAlert314,
       "dmtfAlert315": dmtfAlert315,
       "dmtfAlert320": dmtfAlert320,
       "dmtfAlert321": dmtfAlert321,
       "dmtfAlert323": dmtfAlert323,
       "dmtfAlert325": dmtfAlert325,
       "dmtfAlert326": dmtfAlert326,
       "dmtfAlert327": dmtfAlert327,
       "dmtfAlert330": dmtfAlert330,
       "dmtfGroups": dmtfGroups,
       "tComponentid": tComponentid,
       "eComponentid": eComponentid,
       "a1Manufacturer": a1Manufacturer,
       "a1Product": a1Product,
       "a1Version": a1Version,
       "a1SerialNumber": a1SerialNumber,
       "a1Installation": a1Installation,
       "a1Verify": a1Verify,
       "tTemperature": tTemperature,
       "eTemperature": eTemperature,
       "a2Tempparentindex": a2Tempparentindex,
       "a2Tempindex": a2Tempindex,
       "a2Temptype": a2Temptype,
       "a2Tempstatus": a2Tempstatus,
       "a2Tempreading": a2Tempreading,
       "a2Tempminwarn": a2Tempminwarn,
       "a2Tempmaxwarn": a2Tempmaxwarn,
       "a2Tempminfail": a2Tempminfail,
       "a2Tempmaxfail": a2Tempmaxfail,
       "a2Templocation": a2Templocation,
       "tFan": tFan,
       "eFan": eFan,
       "a3Fansparentindex": a3Fansparentindex,
       "a3Fansindex": a3Fansindex,
       "a3Fanstype": a3Fanstype,
       "a3Fansstatus": a3Fansstatus,
       "a3Fansreading": a3Fansreading,
       "a3Fanswarningmin": a3Fanswarningmin,
       "a3Fansmaxwarn": a3Fansmaxwarn,
       "a3Fansminfail": a3Fansminfail,
       "a3Fansmaxfail": a3Fansmaxfail,
       "a3Fanslocation": a3Fanslocation,
       "tVoltage": tVoltage,
       "eVoltage": eVoltage,
       "a4Voltparentindex": a4Voltparentindex,
       "a4Voltindex": a4Voltindex,
       "a4Volttype": a4Volttype,
       "a4Voltstatus": a4Voltstatus,
       "a4Voltreading": a4Voltreading,
       "a4Voltminwarn": a4Voltminwarn,
       "a4Voltmaxwarn": a4Voltmaxwarn,
       "a4Voltminfail": a4Voltminfail,
       "a4Voltmaxfail": a4Voltmaxfail,
       "a4Voltlocation": a4Voltlocation,
       "tCurrent": tCurrent,
       "eCurrent": eCurrent,
       "a5Ampparentindex": a5Ampparentindex,
       "a5Ampindex": a5Ampindex,
       "a5Amptype": a5Amptype,
       "a5Ampstatus": a5Ampstatus,
       "a5Ampreading": a5Ampreading,
       "a5Ampminwarn": a5Ampminwarn,
       "a5Ampmaxwarn": a5Ampmaxwarn,
       "a5Ampminfail": a5Ampminfail,
       "a5Ampmaxfail": a5Ampmaxfail,
       "a5Amplocation": a5Amplocation,
       "tPowerSupply": tPowerSupply,
       "ePowerSupply": ePowerSupply,
       "a6Pwrsupplyparentindex": a6Pwrsupplyparentindex,
       "a6Pwrsupplyindex": a6Pwrsupplyindex,
       "a6Pwrsupplytype": a6Pwrsupplytype,
       "a6Pwrsupplystatus": a6Pwrsupplystatus,
       "a6Pwrsupplyonline": a6Pwrsupplyonline,
       "a6Pwrlocation": a6Pwrlocation,
       "tGlobalPowerUnit": tGlobalPowerUnit,
       "eGlobalPowerUnit": eGlobalPowerUnit,
       "a7Pwrunitstatus": a7Pwrunitstatus,
       "a7Pwrunitgloballevel": a7Pwrunitgloballevel,
       "a7Pwrunitglobalmaxwarn": a7Pwrunitglobalmaxwarn,
       "a7Pwrunitlevel33v": a7Pwrunitlevel33v,
       "a7Pwrunitmaxwarn33v": a7Pwrunitmaxwarn33v,
       "a7Pwrunitlevel5v": a7Pwrunitlevel5v,
       "a7Pwrunitmaxwarn5v": a7Pwrunitmaxwarn5v,
       "a7Pwrunitlevel12v": a7Pwrunitlevel12v,
       "a7Pwrunitmaxwarn12v": a7Pwrunitmaxwarn12v,
       "a7Pwrunituid": a7Pwrunituid,
       "a7Pwrunitindex": a7Pwrunitindex,
       "tChassisExtension": tChassisExtension,
       "eChassisExtension": eChassisExtension,
       "a8Chassindex": a8Chassindex,
       "a8Chassglobstatus": a8Chassglobstatus,
       "a8Chasstempstatus": a8Chasstempstatus,
       "a8Chasstempprobes": a8Chasstempprobes,
       "a8Chassfansstatus": a8Chassfansstatus,
       "a8Chassfansprobes": a8Chassfansprobes,
       "a8Chassvoltstatus": a8Chassvoltstatus,
       "a8Chassvoltprobes": a8Chassvoltprobes,
       "a8Chassampstatus": a8Chassampstatus,
       "a8Chassampprobes": a8Chassampprobes,
       "a8Chasspsstatus": a8Chasspsstatus,
       "a8Chasspwrsupplies": a8Chasspwrsupplies,
       "a8Chassservicetag": a8Chassservicetag,
       "a8Chassuid": a8Chassuid,
       "a8Chassbackplaneuid": a8Chassbackplaneuid,
       "a8Chassidentify": a8Chassidentify,
       "a8Chassfancontrol": a8Chassfancontrol,
       "a8Chassledconfig": a8Chassledconfig,
       "a8Chassfaultclear": a8Chassfaultclear,
       "tPhysicalContainerGlobalTable": tPhysicalContainerGlobalTable,
       "ePhysicalContainerGlobalTable": ePhysicalContainerGlobalTable,
       "a9ContainerOrChassisType": a9ContainerOrChassisType,
       "a9ContainerAssetTag": a9ContainerAssetTag,
       "a9ChassisLockPresent": a9ChassisLockPresent,
       "a9ContainerChassisBootupState": a9ContainerChassisBootupState,
       "a9PowerState": a9PowerState,
       "a9ThermalState": a9ThermalState,
       "a9FruGroupIndex": a9FruGroupIndex,
       "a9OperationalGroupIndex": a9OperationalGroupIndex,
       "a9ContainerIndex": a9ContainerIndex,
       "a9ContainerName": a9ContainerName,
       "a9ContainerLocation": a9ContainerLocation,
       "a9ContainerSecurityStatus": a9ContainerSecurityStatus,
       "tSystemControl": tSystemControl,
       "eSystemControl": eSystemControl,
       "a10AutomaticCapabilities": a10AutomaticCapabilities,
       "a10AutomaticSettings": a10AutomaticSettings,
       "a10NotificationNumber": a10NotificationNumber,
       "a10ManualCapabilities": a10ManualCapabilities,
       "a10ManualControl": a10ManualControl,
       "tEsmEventLog": tEsmEventLog,
       "eEsmEventLog": eEsmEventLog,
       "a11Esmlogindex": a11Esmlogindex,
       "a11Esmlogdata": a11Esmlogdata,
       "tPostEventLog": tPostEventLog,
       "ePostEventLog": ePostEventLog,
       "a12Postlogindex": a12Postlogindex,
       "a12Postlogdata": a12Postlogdata,
       "tUserSecurityGroup": tUserSecurityGroup,
       "eUserSecurityGroup": eUserSecurityGroup,
       "a13UserIndex": a13UserIndex,
       "a13UserName": a13UserName,
       "a13UserControl": a13UserControl,
       "tDialupControl": tDialupControl,
       "eDialupControl": eDialupControl,
       "a14DialupCapability": a14DialupCapability,
       "a14CallbackNumber": a14CallbackNumber,
       "tFirmwareInformation": tFirmwareInformation,
       "eFirmwareInformation": eFirmwareInformation,
       "a15FirmwareChassisIndex": a15FirmwareChassisIndex,
       "a15FirmwareIndex": a15FirmwareIndex,
       "a15FirmwareType": a15FirmwareType,
       "a15FirmwareVersion": a15FirmwareVersion,
       "a15FirmwareStatus": a15FirmwareStatus,
       "tMiftomib": tMiftomib,
       "eMiftomib": eMiftomib,
       "a99DellBaseboardMib": a99DellBaseboardMib,
       "a99MibOid": a99MibOid,
       "a99DisableTraps": a99DisableTraps,
       "tTemperatureProbeAlerts": tTemperatureProbeAlerts,
       "eTemperatureProbeAlerts": eTemperatureProbeAlerts,
       "a102EventType": a102EventType,
       "a102EventSeverity": a102EventSeverity,
       "a102IsEventStateBased": a102IsEventStateBased,
       "a102EventStateKey": a102EventStateKey,
       "a102AssociatedGroup": a102AssociatedGroup,
       "a102EventSystem": a102EventSystem,
       "a102EventSubsystem": a102EventSubsystem,
       "a102EventSolution": a102EventSolution,
       "a102InstanceDataPresent": a102InstanceDataPresent,
       "a102VendorSpecificMessage": a102VendorSpecificMessage,
       "a102VendorSpecificData": a102VendorSpecificData,
       "a102VendorTrapNumber": a102VendorTrapNumber,
       "tFanSensorAlerts": tFanSensorAlerts,
       "eFanSensorAlerts": eFanSensorAlerts,
       "a103EventType": a103EventType,
       "a103EventSeverity": a103EventSeverity,
       "a103IsEventStateBased": a103IsEventStateBased,
       "a103EventStateKey": a103EventStateKey,
       "a103AssociatedGroup": a103AssociatedGroup,
       "a103EventSystem": a103EventSystem,
       "a103EventSubsystem": a103EventSubsystem,
       "a103EventSolution": a103EventSolution,
       "a103InstanceDataPresent": a103InstanceDataPresent,
       "a103VendorSpecificMessage": a103VendorSpecificMessage,
       "a103VendorSpecificData": a103VendorSpecificData,
       "a103VendorTrapNumber": a103VendorTrapNumber,
       "tVoltageProbeAlerts": tVoltageProbeAlerts,
       "eVoltageProbeAlerts": eVoltageProbeAlerts,
       "a104EventType": a104EventType,
       "a104EventSeverity": a104EventSeverity,
       "a104IsEventStateBased": a104IsEventStateBased,
       "a104EventStateKey": a104EventStateKey,
       "a104AssociatedGroup": a104AssociatedGroup,
       "a104EventSystem": a104EventSystem,
       "a104EventSubsystem": a104EventSubsystem,
       "a104EventSolution": a104EventSolution,
       "a104InstanceDataPresent": a104InstanceDataPresent,
       "a104VendorSpecificMessage": a104VendorSpecificMessage,
       "a104VendorSpecificData": a104VendorSpecificData,
       "a104VendorTrapNumber": a104VendorTrapNumber,
       "tCurrentProbeAlerts": tCurrentProbeAlerts,
       "eCurrentProbeAlerts": eCurrentProbeAlerts,
       "a105EventType": a105EventType,
       "a105EventSeverity": a105EventSeverity,
       "a105IsEventStateBased": a105IsEventStateBased,
       "a105EventStateKey": a105EventStateKey,
       "a105AssociatedGroup": a105AssociatedGroup,
       "a105EventSystem": a105EventSystem,
       "a105EventSubsystem": a105EventSubsystem,
       "a105EventSolution": a105EventSolution,
       "a105InstanceDataPresent": a105InstanceDataPresent,
       "a105VendorSpecificMessage": a105VendorSpecificMessage,
       "a105VendorSpecificData": a105VendorSpecificData,
       "a105VendorTrapNumber": a105VendorTrapNumber,
       "tPowerUnitAlerts": tPowerUnitAlerts,
       "ePowerUnitAlerts": ePowerUnitAlerts,
       "a107EventType": a107EventType,
       "a107EventSeverity": a107EventSeverity,
       "a107IsEventStateBased": a107IsEventStateBased,
       "a107EventStateKey": a107EventStateKey,
       "a107AssociatedGroup": a107AssociatedGroup,
       "a107EventSystem": a107EventSystem,
       "a107EventSubsystem": a107EventSubsystem,
       "a107EventSolution": a107EventSolution,
       "a107InstanceDataPresent": a107InstanceDataPresent,
       "a107VendorSpecificMessage": a107VendorSpecificMessage,
       "a107VendorSpecificData": a107VendorSpecificData,
       "a107VendorTrapNumber": a107VendorTrapNumber,
       "tChassisEventGeneration": tChassisEventGeneration,
       "eChassisEventGeneration": eChassisEventGeneration,
       "a108EventType": a108EventType,
       "a108EventSeverity": a108EventSeverity,
       "a108IsEventStateBased": a108IsEventStateBased,
       "a108EventStateKey": a108EventStateKey,
       "a108AssociatedGroup": a108AssociatedGroup,
       "a108EventSystem": a108EventSystem,
       "a108EventSubsystem": a108EventSubsystem,
       "a108EventSolution": a108EventSolution,
       "a108InstanceDataPresent": a108InstanceDataPresent,
       "a108VendorSpecificMessage": a108VendorSpecificMessage,
       "a108VendorSpecificData": a108VendorSpecificData,
       "a108VendorTrapNumber": a108VendorTrapNumber,
       "tContainerEventGeneration": tContainerEventGeneration,
       "eContainerEventGeneration": eContainerEventGeneration,
       "a109EventType": a109EventType,
       "a109EventSeverity": a109EventSeverity,
       "a109IsEventStateBased": a109IsEventStateBased,
       "a109EventStateKey": a109EventStateKey,
       "a109AssociatedGroup": a109AssociatedGroup,
       "a109EventSystem": a109EventSystem,
       "a109EventSubsystem": a109EventSubsystem,
       "a109EventSolution": a109EventSolution,
       "a109InstanceDataPresent": a109InstanceDataPresent,
       "a109VendorSpecificMessage": a109VendorSpecificMessage,
       "a109VendorSpecificData": a109VendorSpecificData,
       "a109VendorTrapNumber": a109VendorTrapNumber,
       "tResetEventGeneration": tResetEventGeneration,
       "eResetEventGeneration": eResetEventGeneration,
       "a110EventType": a110EventType,
       "a110EventSeverity": a110EventSeverity,
       "a110IsEventStateBased": a110IsEventStateBased,
       "a110EventStateKey": a110EventStateKey,
       "a110AssociatedGroup": a110AssociatedGroup,
       "a110EventSystem": a110EventSystem,
       "a110EventSubsystem": a110EventSubsystem,
       "a110EventSolution": a110EventSolution,
       "a110InstanceDataPresent": a110InstanceDataPresent,
       "a110VendorSpecificMessage": a110VendorSpecificMessage,
       "a110VendorSpecificData": a110VendorSpecificData,
       "a110VendorTrapNumber": a110VendorTrapNumber,
       "tTrapGroup": tTrapGroup,
       "eTrapGroup": eTrapGroup,
       "a9999AlertSystem": a9999AlertSystem,
       "a9999AlertGroup": a9999AlertGroup,
       "a9999AlertMessage": a9999AlertMessage,
       "a9999AlertSeverity": a9999AlertSeverity,
       "a9999AlertData": a9999AlertData}
)
