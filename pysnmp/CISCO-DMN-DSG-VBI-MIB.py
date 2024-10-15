# SNMP MIB module (CISCO-DMN-DSG-VBI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-VBI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:37 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ciscoDSGVBI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 31)
)
ciscoDSGVBI.setRevisions(
        ("2012-03-20 10:00",
         "2010-07-26 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _VbiVitsFlag17_Type(Integer32):
    """Custom type vbiVitsFlag17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_VbiVitsFlag17_Type.__name__ = "Integer32"
_VbiVitsFlag17_Object = MibScalar
vbiVitsFlag17 = _VbiVitsFlag17_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 31, 1),
    _VbiVitsFlag17_Type()
)
vbiVitsFlag17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vbiVitsFlag17.setStatus("current")


class _VbiVitsFlag18_Type(Integer32):
    """Custom type vbiVitsFlag18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_VbiVitsFlag18_Type.__name__ = "Integer32"
_VbiVitsFlag18_Object = MibScalar
vbiVitsFlag18 = _VbiVitsFlag18_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 31, 2),
    _VbiVitsFlag18_Type()
)
vbiVitsFlag18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vbiVitsFlag18.setStatus("current")


class _VbiVitsFlag330_Type(Integer32):
    """Custom type vbiVitsFlag330 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_VbiVitsFlag330_Type.__name__ = "Integer32"
_VbiVitsFlag330_Object = MibScalar
vbiVitsFlag330 = _VbiVitsFlag330_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 31, 3),
    _VbiVitsFlag330_Type()
)
vbiVitsFlag330.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vbiVitsFlag330.setStatus("current")


class _VbiVitsFlag331_Type(Integer32):
    """Custom type vbiVitsFlag331 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_VbiVitsFlag331_Type.__name__ = "Integer32"
_VbiVitsFlag331_Object = MibScalar
vbiVitsFlag331 = _VbiVitsFlag331_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 31, 4),
    _VbiVitsFlag331_Type()
)
vbiVitsFlag331.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vbiVitsFlag331.setStatus("current")


class _VbiVitcMode_Type(Integer32):
    """Custom type vbiVitcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoGenerate", 3),
          ("passthrough", 1),
          ("suppress", 2))
    )


_VbiVitcMode_Type.__name__ = "Integer32"
_VbiVitcMode_Object = MibScalar
vbiVitcMode = _VbiVitcMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 31, 5),
    _VbiVitcMode_Type()
)
vbiVitcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vbiVitcMode.setStatus("current")


class _VbiTimeCode_Type(Integer32):
    """Custom type vbiTimeCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ltc", 1),
          ("vitc", 2))
    )


_VbiTimeCode_Type.__name__ = "Integer32"
_VbiTimeCode_Object = MibScalar
vbiTimeCode = _VbiTimeCode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 31, 6),
    _VbiTimeCode_Type()
)
vbiTimeCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vbiTimeCode.setStatus("current")


class _VbiColorMode_Type(Integer32):
    """Custom type vbiColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_VbiColorMode_Type.__name__ = "Integer32"
_VbiColorMode_Object = MibScalar
vbiColorMode = _VbiColorMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 31, 7),
    _VbiColorMode_Type()
)
vbiColorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vbiColorMode.setStatus("current")


class _VbiDelayComp_Type(Integer32):
    """Custom type vbiDelayComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_VbiDelayComp_Type.__name__ = "Integer32"
_VbiDelayComp_Object = MibScalar
vbiDelayComp = _VbiDelayComp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 31, 8),
    _VbiDelayComp_Type()
)
vbiDelayComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vbiDelayComp.setStatus("current")


class _VbiDropFrame_Type(Integer32):
    """Custom type vbiDropFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_VbiDropFrame_Type.__name__ = "Integer32"
_VbiDropFrame_Object = MibScalar
vbiDropFrame = _VbiDropFrame_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 31, 9),
    _VbiDropFrame_Type()
)
vbiDropFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vbiDropFrame.setStatus("current")


class _VbiVitcStatus_Type(Integer32):
    """Custom type vbiVitcStatus based on Integer32"""
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
        *(("both", 3),
          ("ltc", 1),
          ("undefined", 4),
          ("vitc", 2))
    )


_VbiVitcStatus_Type.__name__ = "Integer32"
_VbiVitcStatus_Object = MibScalar
vbiVitcStatus = _VbiVitcStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 31, 10),
    _VbiVitcStatus_Type()
)
vbiVitcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbiVitcStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-VBI-MIB",
    **{"ciscoDSGVBI": ciscoDSGVBI,
       "vbiVitsFlag17": vbiVitsFlag17,
       "vbiVitsFlag18": vbiVitsFlag18,
       "vbiVitsFlag330": vbiVitsFlag330,
       "vbiVitsFlag331": vbiVitsFlag331,
       "vbiVitcMode": vbiVitcMode,
       "vbiTimeCode": vbiTimeCode,
       "vbiColorMode": vbiColorMode,
       "vbiDelayComp": vbiDelayComp,
       "vbiDropFrame": vbiDropFrame,
       "vbiVitcStatus": vbiVitcStatus}
)
