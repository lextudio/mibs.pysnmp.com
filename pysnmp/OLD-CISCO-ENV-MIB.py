# SNMP MIB module (OLD-CISCO-ENV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLD-CISCO-ENV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:00 2024
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

(local,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "local")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lenv_ObjectIdentity = ObjectIdentity
lenv = _Lenv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 1)
)
_EnvPresent_Type = Integer32
_EnvPresent_Object = MibScalar
envPresent = _EnvPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 77),
    _EnvPresent_Type()
)
envPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPresent.setStatus("mandatory")
_EnvTestPt1Descr_Type = DisplayString
_EnvTestPt1Descr_Object = MibScalar
envTestPt1Descr = _EnvTestPt1Descr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 78),
    _EnvTestPt1Descr_Type()
)
envTestPt1Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt1Descr.setStatus("mandatory")
_EnvTestPt1Measure_Type = Integer32
_EnvTestPt1Measure_Object = MibScalar
envTestPt1Measure = _EnvTestPt1Measure_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 79),
    _EnvTestPt1Measure_Type()
)
envTestPt1Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt1Measure.setStatus("mandatory")
_EnvTestPt2Descr_Type = DisplayString
_EnvTestPt2Descr_Object = MibScalar
envTestPt2Descr = _EnvTestPt2Descr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 80),
    _EnvTestPt2Descr_Type()
)
envTestPt2Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt2Descr.setStatus("mandatory")
_EnvTestPt2Measure_Type = Integer32
_EnvTestPt2Measure_Object = MibScalar
envTestPt2Measure = _EnvTestPt2Measure_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 81),
    _EnvTestPt2Measure_Type()
)
envTestPt2Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt2Measure.setStatus("mandatory")
_EnvTestPt3Descr_Type = DisplayString
_EnvTestPt3Descr_Object = MibScalar
envTestPt3Descr = _EnvTestPt3Descr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 82),
    _EnvTestPt3Descr_Type()
)
envTestPt3Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt3Descr.setStatus("mandatory")
_EnvTestPt3Measure_Type = Integer32
_EnvTestPt3Measure_Object = MibScalar
envTestPt3Measure = _EnvTestPt3Measure_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 83),
    _EnvTestPt3Measure_Type()
)
envTestPt3Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt3Measure.setStatus("mandatory")
_EnvTestPt4Descr_Type = DisplayString
_EnvTestPt4Descr_Object = MibScalar
envTestPt4Descr = _EnvTestPt4Descr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 84),
    _EnvTestPt4Descr_Type()
)
envTestPt4Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt4Descr.setStatus("mandatory")
_EnvTestPt4Measure_Type = Integer32
_EnvTestPt4Measure_Object = MibScalar
envTestPt4Measure = _EnvTestPt4Measure_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 85),
    _EnvTestPt4Measure_Type()
)
envTestPt4Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt4Measure.setStatus("mandatory")
_EnvTestPt5Descr_Type = DisplayString
_EnvTestPt5Descr_Object = MibScalar
envTestPt5Descr = _EnvTestPt5Descr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 86),
    _EnvTestPt5Descr_Type()
)
envTestPt5Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt5Descr.setStatus("mandatory")
_EnvTestPt5Measure_Type = Integer32
_EnvTestPt5Measure_Object = MibScalar
envTestPt5Measure = _EnvTestPt5Measure_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 87),
    _EnvTestPt5Measure_Type()
)
envTestPt5Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt5Measure.setStatus("mandatory")
_EnvTestPt6Descr_Type = DisplayString
_EnvTestPt6Descr_Object = MibScalar
envTestPt6Descr = _EnvTestPt6Descr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 88),
    _EnvTestPt6Descr_Type()
)
envTestPt6Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt6Descr.setStatus("mandatory")
_EnvTestPt6Measure_Type = Integer32
_EnvTestPt6Measure_Object = MibScalar
envTestPt6Measure = _EnvTestPt6Measure_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 89),
    _EnvTestPt6Measure_Type()
)
envTestPt6Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt6Measure.setStatus("mandatory")
_EnvTestPt1MarginVal_Type = Integer32
_EnvTestPt1MarginVal_Object = MibScalar
envTestPt1MarginVal = _EnvTestPt1MarginVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 90),
    _EnvTestPt1MarginVal_Type()
)
envTestPt1MarginVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt1MarginVal.setStatus("mandatory")
_EnvTestPt2MarginVal_Type = Integer32
_EnvTestPt2MarginVal_Object = MibScalar
envTestPt2MarginVal = _EnvTestPt2MarginVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 91),
    _EnvTestPt2MarginVal_Type()
)
envTestPt2MarginVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt2MarginVal.setStatus("mandatory")
_EnvTestPt3MarginPercent_Type = Integer32
_EnvTestPt3MarginPercent_Object = MibScalar
envTestPt3MarginPercent = _EnvTestPt3MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 92),
    _EnvTestPt3MarginPercent_Type()
)
envTestPt3MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt3MarginPercent.setStatus("mandatory")
_EnvTestPt4MarginPercent_Type = Integer32
_EnvTestPt4MarginPercent_Object = MibScalar
envTestPt4MarginPercent = _EnvTestPt4MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 93),
    _EnvTestPt4MarginPercent_Type()
)
envTestPt4MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt4MarginPercent.setStatus("mandatory")
_EnvTestPt5MarginPercent_Type = Integer32
_EnvTestPt5MarginPercent_Object = MibScalar
envTestPt5MarginPercent = _EnvTestPt5MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 94),
    _EnvTestPt5MarginPercent_Type()
)
envTestPt5MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt5MarginPercent.setStatus("mandatory")
_EnvTestPt6MarginPercent_Type = Integer32
_EnvTestPt6MarginPercent_Object = MibScalar
envTestPt6MarginPercent = _EnvTestPt6MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 95),
    _EnvTestPt6MarginPercent_Type()
)
envTestPt6MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt6MarginPercent.setStatus("mandatory")
_EnvTestPt1last_Type = Integer32
_EnvTestPt1last_Object = MibScalar
envTestPt1last = _EnvTestPt1last_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 96),
    _EnvTestPt1last_Type()
)
envTestPt1last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt1last.setStatus("mandatory")
_EnvTestPt2last_Type = Integer32
_EnvTestPt2last_Object = MibScalar
envTestPt2last = _EnvTestPt2last_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 97),
    _EnvTestPt2last_Type()
)
envTestPt2last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt2last.setStatus("mandatory")
_EnvTestPt3last_Type = Integer32
_EnvTestPt3last_Object = MibScalar
envTestPt3last = _EnvTestPt3last_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 98),
    _EnvTestPt3last_Type()
)
envTestPt3last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt3last.setStatus("mandatory")
_EnvTestPt4last_Type = Integer32
_EnvTestPt4last_Object = MibScalar
envTestPt4last = _EnvTestPt4last_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 99),
    _EnvTestPt4last_Type()
)
envTestPt4last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt4last.setStatus("mandatory")
_EnvTestPt5last_Type = Integer32
_EnvTestPt5last_Object = MibScalar
envTestPt5last = _EnvTestPt5last_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 100),
    _EnvTestPt5last_Type()
)
envTestPt5last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt5last.setStatus("mandatory")
_EnvTestPt6last_Type = Integer32
_EnvTestPt6last_Object = MibScalar
envTestPt6last = _EnvTestPt6last_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 101),
    _EnvTestPt6last_Type()
)
envTestPt6last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt6last.setStatus("mandatory")


class _EnvTestPt1warn_Type(Integer32):
    """Custom type envTestPt1warn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWarning", 2),
          ("warning", 1))
    )


_EnvTestPt1warn_Type.__name__ = "Integer32"
_EnvTestPt1warn_Object = MibScalar
envTestPt1warn = _EnvTestPt1warn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 102),
    _EnvTestPt1warn_Type()
)
envTestPt1warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt1warn.setStatus("mandatory")


class _EnvTestPt2warn_Type(Integer32):
    """Custom type envTestPt2warn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWarning", 2),
          ("warning", 1))
    )


_EnvTestPt2warn_Type.__name__ = "Integer32"
_EnvTestPt2warn_Object = MibScalar
envTestPt2warn = _EnvTestPt2warn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 103),
    _EnvTestPt2warn_Type()
)
envTestPt2warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt2warn.setStatus("mandatory")


class _EnvTestPt3warn_Type(Integer32):
    """Custom type envTestPt3warn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWarning", 2),
          ("warning", 1))
    )


_EnvTestPt3warn_Type.__name__ = "Integer32"
_EnvTestPt3warn_Object = MibScalar
envTestPt3warn = _EnvTestPt3warn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 104),
    _EnvTestPt3warn_Type()
)
envTestPt3warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt3warn.setStatus("mandatory")


class _EnvTestPt4warn_Type(Integer32):
    """Custom type envTestPt4warn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWarning", 2),
          ("warning", 1))
    )


_EnvTestPt4warn_Type.__name__ = "Integer32"
_EnvTestPt4warn_Object = MibScalar
envTestPt4warn = _EnvTestPt4warn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 105),
    _EnvTestPt4warn_Type()
)
envTestPt4warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt4warn.setStatus("mandatory")


class _EnvTestPt5warn_Type(Integer32):
    """Custom type envTestPt5warn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWarning", 2),
          ("warning", 1))
    )


_EnvTestPt5warn_Type.__name__ = "Integer32"
_EnvTestPt5warn_Object = MibScalar
envTestPt5warn = _EnvTestPt5warn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 106),
    _EnvTestPt5warn_Type()
)
envTestPt5warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt5warn.setStatus("mandatory")


class _EnvTestPt6warn_Type(Integer32):
    """Custom type envTestPt6warn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWarning", 2),
          ("warning", 1))
    )


_EnvTestPt6warn_Type.__name__ = "Integer32"
_EnvTestPt6warn_Object = MibScalar
envTestPt6warn = _EnvTestPt6warn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 107),
    _EnvTestPt6warn_Type()
)
envTestPt6warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt6warn.setStatus("mandatory")
_EnvFirmVersion_Type = DisplayString
_EnvFirmVersion_Object = MibScalar
envFirmVersion = _EnvFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 108),
    _EnvFirmVersion_Type()
)
envFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFirmVersion.setStatus("mandatory")
_EnvTechnicianID_Type = DisplayString
_EnvTechnicianID_Object = MibScalar
envTechnicianID = _EnvTechnicianID_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 109),
    _EnvTechnicianID_Type()
)
envTechnicianID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTechnicianID.setStatus("mandatory")
_EnvType_Type = DisplayString
_EnvType_Object = MibScalar
envType = _EnvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 110),
    _EnvType_Type()
)
envType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envType.setStatus("mandatory")
_EnvBurnDate_Type = DisplayString
_EnvBurnDate_Object = MibScalar
envBurnDate = _EnvBurnDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 111),
    _EnvBurnDate_Type()
)
envBurnDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envBurnDate.setStatus("mandatory")
_EnvSerialNumber_Type = DisplayString
_EnvSerialNumber_Object = MibScalar
envSerialNumber = _EnvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 112),
    _EnvSerialNumber_Type()
)
envSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envSerialNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-ENV-MIB",
    **{"lenv": lenv,
       "envPresent": envPresent,
       "envTestPt1Descr": envTestPt1Descr,
       "envTestPt1Measure": envTestPt1Measure,
       "envTestPt2Descr": envTestPt2Descr,
       "envTestPt2Measure": envTestPt2Measure,
       "envTestPt3Descr": envTestPt3Descr,
       "envTestPt3Measure": envTestPt3Measure,
       "envTestPt4Descr": envTestPt4Descr,
       "envTestPt4Measure": envTestPt4Measure,
       "envTestPt5Descr": envTestPt5Descr,
       "envTestPt5Measure": envTestPt5Measure,
       "envTestPt6Descr": envTestPt6Descr,
       "envTestPt6Measure": envTestPt6Measure,
       "envTestPt1MarginVal": envTestPt1MarginVal,
       "envTestPt2MarginVal": envTestPt2MarginVal,
       "envTestPt3MarginPercent": envTestPt3MarginPercent,
       "envTestPt4MarginPercent": envTestPt4MarginPercent,
       "envTestPt5MarginPercent": envTestPt5MarginPercent,
       "envTestPt6MarginPercent": envTestPt6MarginPercent,
       "envTestPt1last": envTestPt1last,
       "envTestPt2last": envTestPt2last,
       "envTestPt3last": envTestPt3last,
       "envTestPt4last": envTestPt4last,
       "envTestPt5last": envTestPt5last,
       "envTestPt6last": envTestPt6last,
       "envTestPt1warn": envTestPt1warn,
       "envTestPt2warn": envTestPt2warn,
       "envTestPt3warn": envTestPt3warn,
       "envTestPt4warn": envTestPt4warn,
       "envTestPt5warn": envTestPt5warn,
       "envTestPt6warn": envTestPt6warn,
       "envFirmVersion": envFirmVersion,
       "envTechnicianID": envTechnicianID,
       "envType": envType,
       "envBurnDate": envBurnDate,
       "envSerialNumber": envSerialNumber}
)
