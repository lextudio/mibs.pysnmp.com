# SNMP MIB module (FDDI-CONCENTRATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FDDI-CONCENTRATOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:32 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fibronics_ObjectIdentity = ObjectIdentity
fibronics = _Fibronics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22)
)
_FddiConcentrator_ObjectIdentity = ObjectIdentity
fddiConcentrator = _FddiConcentrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 70)
)
_ConcentratorPORT_ObjectIdentity = ObjectIdentity
concentratorPORT = _ConcentratorPORT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 70, 1)
)
_ConcentratorPORTTable_Object = MibTable
concentratorPORTTable = _ConcentratorPORTTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 1, 1)
)
if mibBuilder.loadTexts:
    concentratorPORTTable.setStatus("mandatory")
_ConcentratorPORTEntry_Object = MibTableRow
concentratorPORTEntry = _ConcentratorPORTEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 1, 1, 1)
)
concentratorPORTEntry.setIndexNames(
    (0, "FDDI-CONCENTRATOR-MIB", "concentratorPORTSMTIndex"),
    (0, "FDDI-CONCENTRATOR-MIB", "concentratorPORTIndex"),
)
if mibBuilder.loadTexts:
    concentratorPORTEntry.setStatus("mandatory")


class _ConcentratorPORTSMTIndex_Type(Integer32):
    """Custom type concentratorPORTSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConcentratorPORTSMTIndex_Type.__name__ = "Integer32"
_ConcentratorPORTSMTIndex_Object = MibTableColumn
concentratorPORTSMTIndex = _ConcentratorPORTSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 1, 1, 1, 1),
    _ConcentratorPORTSMTIndex_Type()
)
concentratorPORTSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPORTSMTIndex.setStatus("mandatory")


class _ConcentratorPORTIndex_Type(Integer32):
    """Custom type concentratorPORTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConcentratorPORTIndex_Type.__name__ = "Integer32"
_ConcentratorPORTIndex_Object = MibTableColumn
concentratorPORTIndex = _ConcentratorPORTIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 1, 1, 1, 2),
    _ConcentratorPORTIndex_Type()
)
concentratorPORTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPORTIndex.setStatus("mandatory")


class _ConcentratorPORTType_Type(Integer32):
    """Custom type concentratorPORTType based on Integer32"""
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
        *(("baseT", 7),
          ("fiber", 2),
          ("ibm", 5),
          ("mono", 8),
          ("plastic", 6),
          ("stp", 4),
          ("unknown", 1),
          ("utp", 3))
    )


_ConcentratorPORTType_Type.__name__ = "Integer32"
_ConcentratorPORTType_Object = MibTableColumn
concentratorPORTType = _ConcentratorPORTType_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 1, 1, 1, 3),
    _ConcentratorPORTType_Type()
)
concentratorPORTType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPORTType.setStatus("mandatory")


class _ConcentratorPORTStatus_Type(Integer32):
    """Custom type concentratorPORTStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1),
          ("undefind", 3))
    )


_ConcentratorPORTStatus_Type.__name__ = "Integer32"
_ConcentratorPORTStatus_Object = MibTableColumn
concentratorPORTStatus = _ConcentratorPORTStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 1, 1, 1, 4),
    _ConcentratorPORTStatus_Type()
)
concentratorPORTStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPORTStatus.setStatus("mandatory")
_ConcentratorPROCESSOR_ObjectIdentity = ObjectIdentity
concentratorPROCESSOR = _ConcentratorPROCESSOR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 70, 2)
)


class _ConcentratorPROCESSORType_Type(Integer32):
    """Custom type concentratorPROCESSORType based on Integer32"""
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
        *(("p186", 4),
          ("p286", 5),
          ("p386", 6),
          ("p486", 7),
          ("p86", 3),
          ("p88", 2),
          ("unkown", 1))
    )


_ConcentratorPROCESSORType_Type.__name__ = "Integer32"
_ConcentratorPROCESSORType_Object = MibScalar
concentratorPROCESSORType = _ConcentratorPROCESSORType_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 2, 1),
    _ConcentratorPROCESSORType_Type()
)
concentratorPROCESSORType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPROCESSORType.setStatus("mandatory")


class _ConcentratorPROCESSORFrequency_Type(Integer32):
    """Custom type concentratorPROCESSORFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConcentratorPROCESSORFrequency_Type.__name__ = "Integer32"
_ConcentratorPROCESSORFrequency_Object = MibScalar
concentratorPROCESSORFrequency = _ConcentratorPROCESSORFrequency_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 2, 2),
    _ConcentratorPROCESSORFrequency_Type()
)
concentratorPROCESSORFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPROCESSORFrequency.setStatus("mandatory")
_ConcentratorMEMORY_ObjectIdentity = ObjectIdentity
concentratorMEMORY = _ConcentratorMEMORY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 70, 3)
)


class _ConcentratorSystemMEMORYAvailable_Type(Integer32):
    """Custom type concentratorSystemMEMORYAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConcentratorSystemMEMORYAvailable_Type.__name__ = "Integer32"
_ConcentratorSystemMEMORYAvailable_Object = MibScalar
concentratorSystemMEMORYAvailable = _ConcentratorSystemMEMORYAvailable_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 3, 1),
    _ConcentratorSystemMEMORYAvailable_Type()
)
concentratorSystemMEMORYAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSystemMEMORYAvailable.setStatus("mandatory")


class _ConcentratorSystemMEMORYFree_Type(Integer32):
    """Custom type concentratorSystemMEMORYFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConcentratorSystemMEMORYFree_Type.__name__ = "Integer32"
_ConcentratorSystemMEMORYFree_Object = MibScalar
concentratorSystemMEMORYFree = _ConcentratorSystemMEMORYFree_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 3, 2),
    _ConcentratorSystemMEMORYFree_Type()
)
concentratorSystemMEMORYFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSystemMEMORYFree.setStatus("mandatory")


class _ConcentratorBufferMEMORYAvailable_Type(Integer32):
    """Custom type concentratorBufferMEMORYAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConcentratorBufferMEMORYAvailable_Type.__name__ = "Integer32"
_ConcentratorBufferMEMORYAvailable_Object = MibScalar
concentratorBufferMEMORYAvailable = _ConcentratorBufferMEMORYAvailable_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 3, 3),
    _ConcentratorBufferMEMORYAvailable_Type()
)
concentratorBufferMEMORYAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorBufferMEMORYAvailable.setStatus("mandatory")


class _ConcentratorMEMORYFlashEPROM_Type(Integer32):
    """Custom type concentratorMEMORYFlashEPROM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 1),
          ("present", 2))
    )


_ConcentratorMEMORYFlashEPROM_Type.__name__ = "Integer32"
_ConcentratorMEMORYFlashEPROM_Object = MibScalar
concentratorMEMORYFlashEPROM = _ConcentratorMEMORYFlashEPROM_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 3, 4),
    _ConcentratorMEMORYFlashEPROM_Type()
)
concentratorMEMORYFlashEPROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorMEMORYFlashEPROM.setStatus("mandatory")
_ConcentratorSERIALPORT_ObjectIdentity = ObjectIdentity
concentratorSERIALPORT = _ConcentratorSERIALPORT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 70, 4)
)


class _ConcentratorSERIALPORTBaudRate_Type(Integer32):
    """Custom type concentratorSERIALPORTBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConcentratorSERIALPORTBaudRate_Type.__name__ = "Integer32"
_ConcentratorSERIALPORTBaudRate_Object = MibScalar
concentratorSERIALPORTBaudRate = _ConcentratorSERIALPORTBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 4, 1),
    _ConcentratorSERIALPORTBaudRate_Type()
)
concentratorSERIALPORTBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorSERIALPORTBaudRate.setStatus("mandatory")


class _ConcentratorSERIALPORTParity_Type(Integer32):
    """Custom type concentratorSERIALPORTParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_ConcentratorSERIALPORTParity_Type.__name__ = "Integer32"
_ConcentratorSERIALPORTParity_Object = MibScalar
concentratorSERIALPORTParity = _ConcentratorSERIALPORTParity_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 4, 2),
    _ConcentratorSERIALPORTParity_Type()
)
concentratorSERIALPORTParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSERIALPORTParity.setStatus("mandatory")


class _ConcentratorSERIALPORTStopBits_Type(Integer32):
    """Custom type concentratorSERIALPORTStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConcentratorSERIALPORTStopBits_Type.__name__ = "Integer32"
_ConcentratorSERIALPORTStopBits_Object = MibScalar
concentratorSERIALPORTStopBits = _ConcentratorSERIALPORTStopBits_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 4, 3),
    _ConcentratorSERIALPORTStopBits_Type()
)
concentratorSERIALPORTStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorSERIALPORTStopBits.setStatus("mandatory")
_ConcentratorVERSIONS_ObjectIdentity = ObjectIdentity
concentratorVERSIONS = _ConcentratorVERSIONS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 70, 5)
)


class _ConcentratorVERSIONSBoardSerialNumber_Type(OctetString):
    """Custom type concentratorVERSIONSBoardSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConcentratorVERSIONSBoardSerialNumber_Type.__name__ = "OctetString"
_ConcentratorVERSIONSBoardSerialNumber_Object = MibScalar
concentratorVERSIONSBoardSerialNumber = _ConcentratorVERSIONSBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 1),
    _ConcentratorVERSIONSBoardSerialNumber_Type()
)
concentratorVERSIONSBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorVERSIONSBoardSerialNumber.setStatus("mandatory")


class _ConcentratorVERSIONSNMP_Type(OctetString):
    """Custom type concentratorVERSIONSNMP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConcentratorVERSIONSNMP_Type.__name__ = "OctetString"
_ConcentratorVERSIONSNMP_Object = MibScalar
concentratorVERSIONSNMP = _ConcentratorVERSIONSNMP_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 2),
    _ConcentratorVERSIONSNMP_Type()
)
concentratorVERSIONSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorVERSIONSNMP.setStatus("mandatory")


class _ConcentratorVERSIONBIOS_Type(OctetString):
    """Custom type concentratorVERSIONBIOS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConcentratorVERSIONBIOS_Type.__name__ = "OctetString"
_ConcentratorVERSIONBIOS_Object = MibScalar
concentratorVERSIONBIOS = _ConcentratorVERSIONBIOS_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 3),
    _ConcentratorVERSIONBIOS_Type()
)
concentratorVERSIONBIOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorVERSIONBIOS.setStatus("mandatory")


class _ConcentratorVERSIONSMT_Type(OctetString):
    """Custom type concentratorVERSIONSMT based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ConcentratorVERSIONSMT_Type.__name__ = "OctetString"
_ConcentratorVERSIONSMT_Object = MibScalar
concentratorVERSIONSMT = _ConcentratorVERSIONSMT_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 4),
    _ConcentratorVERSIONSMT_Type()
)
concentratorVERSIONSMT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorVERSIONSMT.setStatus("mandatory")


class _ConcentratorVERSIONMAC_Type(OctetString):
    """Custom type concentratorVERSIONMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ConcentratorVERSIONMAC_Type.__name__ = "OctetString"
_ConcentratorVERSIONMAC_Object = MibScalar
concentratorVERSIONMAC = _ConcentratorVERSIONMAC_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 5),
    _ConcentratorVERSIONMAC_Type()
)
concentratorVERSIONMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorVERSIONMAC.setStatus("mandatory")


class _ConcentratorVERSIONHRDWR_Type(OctetString):
    """Custom type concentratorVERSIONHRDWR based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_ConcentratorVERSIONHRDWR_Type.__name__ = "OctetString"
_ConcentratorVERSIONHRDWR_Object = MibScalar
concentratorVERSIONHRDWR = _ConcentratorVERSIONHRDWR_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 6),
    _ConcentratorVERSIONHRDWR_Type()
)
concentratorVERSIONHRDWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorVERSIONHRDWR.setStatus("mandatory")


class _ConcentratorVERSIONSlotsNumber_Type(Integer32):
    """Custom type concentratorVERSIONSlotsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConcentratorVERSIONSlotsNumber_Type.__name__ = "Integer32"
_ConcentratorVERSIONSlotsNumber_Object = MibScalar
concentratorVERSIONSlotsNumber = _ConcentratorVERSIONSlotsNumber_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 7),
    _ConcentratorVERSIONSlotsNumber_Type()
)
concentratorVERSIONSlotsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorVERSIONSlotsNumber.setStatus("mandatory")
_ConcentratorVERSIONSlotsTable_Object = MibTable
concentratorVERSIONSlotsTable = _ConcentratorVERSIONSlotsTable_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 8)
)
if mibBuilder.loadTexts:
    concentratorVERSIONSlotsTable.setStatus("mandatory")
_ConcentratorVERSIONSlotEntry_Object = MibTableRow
concentratorVERSIONSlotEntry = _ConcentratorVERSIONSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 8, 1)
)
concentratorVERSIONSlotEntry.setIndexNames(
    (0, "FDDI-CONCENTRATOR-MIB", "concentratorVERSIONSlotIndex"),
)
if mibBuilder.loadTexts:
    concentratorVERSIONSlotEntry.setStatus("mandatory")


class _ConcentratorVERSIONSlotIndex_Type(Integer32):
    """Custom type concentratorVERSIONSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ConcentratorVERSIONSlotIndex_Type.__name__ = "Integer32"
_ConcentratorVERSIONSlotIndex_Object = MibTableColumn
concentratorVERSIONSlotIndex = _ConcentratorVERSIONSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 8, 1, 1),
    _ConcentratorVERSIONSlotIndex_Type()
)
concentratorVERSIONSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorVERSIONSlotIndex.setStatus("mandatory")


class _ConcentratorVERSIONSlotSerialNumber_Type(OctetString):
    """Custom type concentratorVERSIONSlotSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_ConcentratorVERSIONSlotSerialNumber_Type.__name__ = "OctetString"
_ConcentratorVERSIONSlotSerialNumber_Object = MibTableColumn
concentratorVERSIONSlotSerialNumber = _ConcentratorVERSIONSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 8, 1, 2),
    _ConcentratorVERSIONSlotSerialNumber_Type()
)
concentratorVERSIONSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorVERSIONSlotSerialNumber.setStatus("mandatory")


class _ConcentratorVERSIONSlotId_Type(Integer32):
    """Custom type concentratorVERSIONSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConcentratorVERSIONSlotId_Type.__name__ = "Integer32"
_ConcentratorVERSIONSlotId_Object = MibTableColumn
concentratorVERSIONSlotId = _ConcentratorVERSIONSlotId_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 8, 1, 3),
    _ConcentratorVERSIONSlotId_Type()
)
concentratorVERSIONSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorVERSIONSlotId.setStatus("mandatory")


class _ConcentratorVERSIONSlotHrdwrStatus_Type(Integer32):
    """Custom type concentratorVERSIONSlotHrdwrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConcentratorVERSIONSlotHrdwrStatus_Type.__name__ = "Integer32"
_ConcentratorVERSIONSlotHrdwrStatus_Object = MibTableColumn
concentratorVERSIONSlotHrdwrStatus = _ConcentratorVERSIONSlotHrdwrStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 8, 1, 4),
    _ConcentratorVERSIONSlotHrdwrStatus_Type()
)
concentratorVERSIONSlotHrdwrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorVERSIONSlotHrdwrStatus.setStatus("mandatory")


class _ConcentratorVERSIONSlotRevision_Type(Integer32):
    """Custom type concentratorVERSIONSlotRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ConcentratorVERSIONSlotRevision_Type.__name__ = "Integer32"
_ConcentratorVERSIONSlotRevision_Object = MibTableColumn
concentratorVERSIONSlotRevision = _ConcentratorVERSIONSlotRevision_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 5, 8, 1, 5),
    _ConcentratorVERSIONSlotRevision_Type()
)
concentratorVERSIONSlotRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorVERSIONSlotRevision.setStatus("mandatory")
_ConcentratorPOWER_ObjectIdentity = ObjectIdentity
concentratorPOWER = _ConcentratorPOWER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 70, 6)
)


class _ConcentratorPOWERFirstSupplyState_Type(Integer32):
    """Custom type concentratorPOWERFirstSupplyState based on Integer32"""
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
        *(("failure", 2),
          ("notpresent", 3),
          ("ok", 1),
          ("reserved", 4))
    )


_ConcentratorPOWERFirstSupplyState_Type.__name__ = "Integer32"
_ConcentratorPOWERFirstSupplyState_Object = MibScalar
concentratorPOWERFirstSupplyState = _ConcentratorPOWERFirstSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 6, 1),
    _ConcentratorPOWERFirstSupplyState_Type()
)
concentratorPOWERFirstSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPOWERFirstSupplyState.setStatus("mandatory")


class _ConcentratorPOWERSecondSupplyState_Type(Integer32):
    """Custom type concentratorPOWERSecondSupplyState based on Integer32"""
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
        *(("failure", 2),
          ("notpresent", 3),
          ("ok", 1),
          ("reserved", 4))
    )


_ConcentratorPOWERSecondSupplyState_Type.__name__ = "Integer32"
_ConcentratorPOWERSecondSupplyState_Object = MibScalar
concentratorPOWERSecondSupplyState = _ConcentratorPOWERSecondSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 6, 2),
    _ConcentratorPOWERSecondSupplyState_Type()
)
concentratorPOWERSecondSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPOWERSecondSupplyState.setStatus("mandatory")


class _ConcentratorPOWERFirstFANState_Type(Integer32):
    """Custom type concentratorPOWERFirstFANState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("ok", 1))
    )


_ConcentratorPOWERFirstFANState_Type.__name__ = "Integer32"
_ConcentratorPOWERFirstFANState_Object = MibScalar
concentratorPOWERFirstFANState = _ConcentratorPOWERFirstFANState_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 6, 3),
    _ConcentratorPOWERFirstFANState_Type()
)
concentratorPOWERFirstFANState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPOWERFirstFANState.setStatus("mandatory")


class _ConcentratorPOWERSecondFANState_Type(Integer32):
    """Custom type concentratorPOWERSecondFANState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("ok", 1))
    )


_ConcentratorPOWERSecondFANState_Type.__name__ = "Integer32"
_ConcentratorPOWERSecondFANState_Object = MibScalar
concentratorPOWERSecondFANState = _ConcentratorPOWERSecondFANState_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 6, 4),
    _ConcentratorPOWERSecondFANState_Type()
)
concentratorPOWERSecondFANState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPOWERSecondFANState.setStatus("mandatory")
_ConcentratorPOWERTemperature_Type = Integer32
_ConcentratorPOWERTemperature_Object = MibScalar
concentratorPOWERTemperature = _ConcentratorPOWERTemperature_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 6, 5),
    _ConcentratorPOWERTemperature_Type()
)
concentratorPOWERTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPOWERTemperature.setStatus("mandatory")


class _ConcentratorPOWERBatteryStatus_Type(Integer32):
    """Custom type concentratorPOWERBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("notpresent", 3),
          ("ok", 1))
    )


_ConcentratorPOWERBatteryStatus_Type.__name__ = "Integer32"
_ConcentratorPOWERBatteryStatus_Object = MibScalar
concentratorPOWERBatteryStatus = _ConcentratorPOWERBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 6, 6),
    _ConcentratorPOWERBatteryStatus_Type()
)
concentratorPOWERBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorPOWERBatteryStatus.setStatus("mandatory")
_ConcentratorTRAPS_ObjectIdentity = ObjectIdentity
concentratorTRAPS = _ConcentratorTRAPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 70, 7)
)
_ConcentratorMgrAddress_Type = IpAddress
_ConcentratorMgrAddress_Object = MibScalar
concentratorMgrAddress = _ConcentratorMgrAddress_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 7, 1),
    _ConcentratorMgrAddress_Type()
)
concentratorMgrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    concentratorMgrAddress.setStatus("mandatory")
_ConcentratorIDENTIFIER_ObjectIdentity = ObjectIdentity
concentratorIDENTIFIER = _ConcentratorIDENTIFIER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 70, 8)
)
_ConcentratorTRAFFIC_ObjectIdentity = ObjectIdentity
concentratorTRAFFIC = _ConcentratorTRAFFIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22, 70, 9)
)
_ConcentratorTRAFFICSMTTransmits_Type = Counter32
_ConcentratorTRAFFICSMTTransmits_Object = MibScalar
concentratorTRAFFICSMTTransmits = _ConcentratorTRAFFICSMTTransmits_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 9, 1),
    _ConcentratorTRAFFICSMTTransmits_Type()
)
concentratorTRAFFICSMTTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorTRAFFICSMTTransmits.setStatus("mandatory")
_ConcentratorTRAFFICSMTReceivs_Type = Counter32
_ConcentratorTRAFFICSMTReceivs_Object = MibScalar
concentratorTRAFFICSMTReceivs = _ConcentratorTRAFFICSMTReceivs_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 9, 2),
    _ConcentratorTRAFFICSMTReceivs_Type()
)
concentratorTRAFFICSMTReceivs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorTRAFFICSMTReceivs.setStatus("mandatory")


class _ConcentratorTRAFFICRS232Activity_Type(Integer32):
    """Custom type concentratorTRAFFICRS232Activity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("nonactive", 2))
    )


_ConcentratorTRAFFICRS232Activity_Type.__name__ = "Integer32"
_ConcentratorTRAFFICRS232Activity_Object = MibScalar
concentratorTRAFFICRS232Activity = _ConcentratorTRAFFICRS232Activity_Object(
    (1, 3, 6, 1, 4, 1, 22, 70, 9, 3),
    _ConcentratorTRAFFICRS232Activity_Type()
)
concentratorTRAFFICRS232Activity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concentratorTRAFFICRS232Activity.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDDI-CONCENTRATOR-MIB",
    **{"fibronics": fibronics,
       "fddiConcentrator": fddiConcentrator,
       "concentratorPORT": concentratorPORT,
       "concentratorPORTTable": concentratorPORTTable,
       "concentratorPORTEntry": concentratorPORTEntry,
       "concentratorPORTSMTIndex": concentratorPORTSMTIndex,
       "concentratorPORTIndex": concentratorPORTIndex,
       "concentratorPORTType": concentratorPORTType,
       "concentratorPORTStatus": concentratorPORTStatus,
       "concentratorPROCESSOR": concentratorPROCESSOR,
       "concentratorPROCESSORType": concentratorPROCESSORType,
       "concentratorPROCESSORFrequency": concentratorPROCESSORFrequency,
       "concentratorMEMORY": concentratorMEMORY,
       "concentratorSystemMEMORYAvailable": concentratorSystemMEMORYAvailable,
       "concentratorSystemMEMORYFree": concentratorSystemMEMORYFree,
       "concentratorBufferMEMORYAvailable": concentratorBufferMEMORYAvailable,
       "concentratorMEMORYFlashEPROM": concentratorMEMORYFlashEPROM,
       "concentratorSERIALPORT": concentratorSERIALPORT,
       "concentratorSERIALPORTBaudRate": concentratorSERIALPORTBaudRate,
       "concentratorSERIALPORTParity": concentratorSERIALPORTParity,
       "concentratorSERIALPORTStopBits": concentratorSERIALPORTStopBits,
       "concentratorVERSIONS": concentratorVERSIONS,
       "concentratorVERSIONSBoardSerialNumber": concentratorVERSIONSBoardSerialNumber,
       "concentratorVERSIONSNMP": concentratorVERSIONSNMP,
       "concentratorVERSIONBIOS": concentratorVERSIONBIOS,
       "concentratorVERSIONSMT": concentratorVERSIONSMT,
       "concentratorVERSIONMAC": concentratorVERSIONMAC,
       "concentratorVERSIONHRDWR": concentratorVERSIONHRDWR,
       "concentratorVERSIONSlotsNumber": concentratorVERSIONSlotsNumber,
       "concentratorVERSIONSlotsTable": concentratorVERSIONSlotsTable,
       "concentratorVERSIONSlotEntry": concentratorVERSIONSlotEntry,
       "concentratorVERSIONSlotIndex": concentratorVERSIONSlotIndex,
       "concentratorVERSIONSlotSerialNumber": concentratorVERSIONSlotSerialNumber,
       "concentratorVERSIONSlotId": concentratorVERSIONSlotId,
       "concentratorVERSIONSlotHrdwrStatus": concentratorVERSIONSlotHrdwrStatus,
       "concentratorVERSIONSlotRevision": concentratorVERSIONSlotRevision,
       "concentratorPOWER": concentratorPOWER,
       "concentratorPOWERFirstSupplyState": concentratorPOWERFirstSupplyState,
       "concentratorPOWERSecondSupplyState": concentratorPOWERSecondSupplyState,
       "concentratorPOWERFirstFANState": concentratorPOWERFirstFANState,
       "concentratorPOWERSecondFANState": concentratorPOWERSecondFANState,
       "concentratorPOWERTemperature": concentratorPOWERTemperature,
       "concentratorPOWERBatteryStatus": concentratorPOWERBatteryStatus,
       "concentratorTRAPS": concentratorTRAPS,
       "concentratorMgrAddress": concentratorMgrAddress,
       "concentratorIDENTIFIER": concentratorIDENTIFIER,
       "concentratorTRAFFIC": concentratorTRAFFIC,
       "concentratorTRAFFICSMTTransmits": concentratorTRAFFICSMTTransmits,
       "concentratorTRAFFICSMTReceivs": concentratorTRAFFICSMTReceivs,
       "concentratorTRAFFICRS232Activity": concentratorTRAFFICRS232Activity}
)
