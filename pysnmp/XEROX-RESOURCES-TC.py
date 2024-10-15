# SNMP MIB module (XEROX-RESOURCES-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEROX-RESOURCES-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:32 2024
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

(xeroxCommonMIB,) = mibBuilder.importSymbols(
    "XEROX-COMMON-MIB",
    "xeroxCommonMIB")


# MODULE-IDENTITY

xcmRsrcTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 56)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class XcmRsrcGroupSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class XcmRsrcType(Integer32, TextualConvention):
    status = "current"
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
        *(("font", 3),
          ("form", 5),
          ("image", 6),
          ("logo", 4),
          ("other", 1),
          ("unknown", 2))
    )



class XcmRsrcPersistence(Integer32, TextualConvention):
    status = "current"
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
        *(("nonvolatile", 4),
          ("other", 1),
          ("permanent", 5),
          ("unknown", 2),
          ("volatile", 3))
    )



class XcmFontType(Integer32, TextualConvention):
    status = "current"
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("pclIntellifont", 11),
          ("pclSoftFont", 10),
          ("psCIDType0", 7),
          ("psCIDType1", 8),
          ("psCIDType2", 9),
          ("psType0", 5),
          ("psType1", 3),
          ("psType14", 13),
          ("psType2", 14),
          ("psType3", 4),
          ("psType42", 6),
          ("unknown", 2),
          ("xeroxICF", 12))
    )



class XcmFontSpacing(Integer32, TextualConvention):
    status = "current"
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
        *(("fixedSpacing", 3),
          ("other", 1),
          ("proportionalSpacing", 4),
          ("unknown", 2))
    )



class XcmFontPCLStyle(Integer32, TextualConvention):
    status = "current"
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("compressed", 7),
          ("condensed", 5),
          ("condensedItalic", 6),
          ("expanded", 8),
          ("inline", 10),
          ("italic", 4),
          ("other", 1),
          ("outline", 9),
          ("outlineShadowed", 12),
          ("shadowed", 11),
          ("unknown", 2),
          ("upright", 3))
    )



class XcmFontPCLStrokeWeight(Integer32, TextualConvention):
    status = "current"
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("black", 15),
          ("bold", 13),
          ("demiBold", 12),
          ("demiLight", 8),
          ("extraBlack", 16),
          ("extraBold", 14),
          ("extraLight", 6),
          ("extraThin", 4),
          ("light", 7),
          ("medium", 10),
          ("other", 1),
          ("semiBold", 11),
          ("semiLight", 9),
          ("thin", 5),
          ("ultraBlack", 17),
          ("ultraThin", 3),
          ("unknown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_XCmRsrcDummy_ObjectIdentity = ObjectIdentity
xCmRsrcDummy = _XCmRsrcDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 253, 8, 56, 999)
)
_XCmRsrcGroupSupport_Type = XcmRsrcGroupSupport
_XCmRsrcGroupSupport_Object = MibScalar
xCmRsrcGroupSupport = _XCmRsrcGroupSupport_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 56, 999, 1),
    _XCmRsrcGroupSupport_Type()
)
xCmRsrcGroupSupport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmRsrcGroupSupport.setStatus("current")
_XCmRsrcType_Type = XcmRsrcType
_XCmRsrcType_Object = MibScalar
xCmRsrcType = _XCmRsrcType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 56, 999, 2),
    _XCmRsrcType_Type()
)
xCmRsrcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmRsrcType.setStatus("current")
_XCmRsrcPersistence_Type = XcmRsrcPersistence
_XCmRsrcPersistence_Object = MibScalar
xCmRsrcPersistence = _XCmRsrcPersistence_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 56, 999, 3),
    _XCmRsrcPersistence_Type()
)
xCmRsrcPersistence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmRsrcPersistence.setStatus("current")
_XCmFontType_Type = XcmFontType
_XCmFontType_Object = MibScalar
xCmFontType = _XCmFontType_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 56, 999, 4),
    _XCmFontType_Type()
)
xCmFontType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmFontType.setStatus("current")
_XCmFontSpacing_Type = XcmFontSpacing
_XCmFontSpacing_Object = MibScalar
xCmFontSpacing = _XCmFontSpacing_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 56, 999, 5),
    _XCmFontSpacing_Type()
)
xCmFontSpacing.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmFontSpacing.setStatus("current")
_XCmFontPCLStyle_Type = XcmFontPCLStyle
_XCmFontPCLStyle_Object = MibScalar
xCmFontPCLStyle = _XCmFontPCLStyle_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 56, 999, 6),
    _XCmFontPCLStyle_Type()
)
xCmFontPCLStyle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmFontPCLStyle.setStatus("current")
_XCmFontPCLStrokeWeight_Type = XcmFontPCLStrokeWeight
_XCmFontPCLStrokeWeight_Object = MibScalar
xCmFontPCLStrokeWeight = _XCmFontPCLStrokeWeight_Object(
    (1, 3, 6, 1, 4, 1, 253, 8, 56, 999, 7),
    _XCmFontPCLStrokeWeight_Type()
)
xCmFontPCLStrokeWeight.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xCmFontPCLStrokeWeight.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEROX-RESOURCES-TC",
    **{"XcmRsrcGroupSupport": XcmRsrcGroupSupport,
       "XcmRsrcType": XcmRsrcType,
       "XcmRsrcPersistence": XcmRsrcPersistence,
       "XcmFontType": XcmFontType,
       "XcmFontSpacing": XcmFontSpacing,
       "XcmFontPCLStyle": XcmFontPCLStyle,
       "XcmFontPCLStrokeWeight": XcmFontPCLStrokeWeight,
       "xcmRsrcTC": xcmRsrcTC,
       "xCmRsrcDummy": xCmRsrcDummy,
       "xCmRsrcGroupSupport": xCmRsrcGroupSupport,
       "xCmRsrcType": xCmRsrcType,
       "xCmRsrcPersistence": xCmRsrcPersistence,
       "xCmFontType": xCmFontType,
       "xCmFontSpacing": xCmFontSpacing,
       "xCmFontPCLStyle": xCmFontPCLStyle,
       "xCmFontPCLStrokeWeight": xCmFontPCLStrokeWeight}
)
