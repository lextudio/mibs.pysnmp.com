# SNMP MIB module (TRANGO-APEX-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRANGO-APEX-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:19 2024
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(ModuleIdentity,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Unsigned32,
 apex) = mibBuilder.importSymbols(
    "TRANGO-APEX-MIB",
    "ModuleIdentity",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Unsigned32",
    "apex")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Modem_ObjectIdentity = ObjectIdentity
modem = _Modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2)
)


class _ModemLoopbackMode_Type(Integer32):
    """Custom type modemLoopbackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("DIGITAL", 1),
          ("IF", 2),
          ("OFF", 0),
          ("RFGEN", 3),
          ("RFREFL", 4))
    )


_ModemLoopbackMode_Type.__name__ = "Integer32"
_ModemLoopbackMode_Object = MibScalar
modemLoopbackMode = _ModemLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 1),
    _ModemLoopbackMode_Type()
)
modemLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemLoopbackMode.setStatus("current")


class _ModemDataPattern_Type(Integer32):
    """Custom type modemDataPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("EXT", 0),
          ("INT", 1))
    )


_ModemDataPattern_Type.__name__ = "Integer32"
_ModemDataPattern_Object = MibScalar
modemDataPattern = _ModemDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 2),
    _ModemDataPattern_Type()
)
modemDataPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemDataPattern.setStatus("current")
_ModemBER_Type = DisplayString
_ModemBER_Object = MibScalar
modemBER = _ModemBER_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 3),
    _ModemBER_Type()
)
modemBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemBER.setStatus("current")
_ModemMSE_Type = Integer32
_ModemMSE_Object = MibScalar
modemMSE = _ModemMSE_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 4),
    _ModemMSE_Type()
)
modemMSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemMSE.setStatus("current")
_ModemFER_Type = DisplayString
_ModemFER_Object = MibScalar
modemFER = _ModemFER_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 5),
    _ModemFER_Type()
)
modemFER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemFER.setStatus("current")
_Lock_ObjectIdentity = ObjectIdentity
lock = _Lock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 6)
)


class _ModemLockStatus_Type(Integer32):
    """Custom type modemLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("LOCKED", 1),
          ("PROGRESS", 2),
          ("UNLOCKED", 0))
    )


_ModemLockStatus_Type.__name__ = "Integer32"
_ModemLockStatus_Object = MibScalar
modemLockStatus = _ModemLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 6, 1),
    _ModemLockStatus_Type()
)
modemLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemLockStatus.setStatus("current")


class _ModemTimingLock_Type(Integer32):
    """Custom type modemTimingLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("LOCKED", 1),
          ("NOTLOCKED", 0))
    )


_ModemTimingLock_Type.__name__ = "Integer32"
_ModemTimingLock_Object = MibScalar
modemTimingLock = _ModemTimingLock_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 6, 2),
    _ModemTimingLock_Type()
)
modemTimingLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemTimingLock.setStatus("current")


class _ModemPreambleLock_Type(Integer32):
    """Custom type modemPreambleLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("LOCKED", 1),
          ("NOTLOCKED", 0))
    )


_ModemPreambleLock_Type.__name__ = "Integer32"
_ModemPreambleLock_Object = MibScalar
modemPreambleLock = _ModemPreambleLock_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 6, 3),
    _ModemPreambleLock_Type()
)
modemPreambleLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemPreambleLock.setStatus("current")


class _ModemLdpcLock_Type(Integer32):
    """Custom type modemLdpcLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("LOCKED", 1),
          ("NOTLOCKED", 0))
    )


_ModemLdpcLock_Type.__name__ = "Integer32"
_ModemLdpcLock_Object = MibScalar
modemLdpcLock = _ModemLdpcLock_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 6, 4),
    _ModemLdpcLock_Type()
)
modemLdpcLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemLdpcLock.setStatus("current")
_ModemReserved_Type = Integer32
_ModemReserved_Object = MibScalar
modemReserved = _ModemReserved_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 6, 5),
    _ModemReserved_Type()
)
modemReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemReserved.setStatus("current")
_Acm_ObjectIdentity = ObjectIdentity
acm = _Acm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7)
)


class _ModemACMEnable_Type(Integer32):
    """Custom type modemACMEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("DISABLED", 0),
          ("ENABLED", 1))
    )


_ModemACMEnable_Type.__name__ = "Integer32"
_ModemACMEnable_Object = MibScalar
modemACMEnable = _ModemACMEnable_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 1),
    _ModemACMEnable_Type()
)
modemACMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMEnable.setStatus("current")
_Acmprofile_ObjectIdentity = ObjectIdentity
acmprofile = _Acmprofile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 2)
)


class _ModemACMProfileQPSKEnable_Type(Integer32):
    """Custom type modemACMProfileQPSKEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("DISABLED", 0),
          ("ENABLED", 1))
    )


_ModemACMProfileQPSKEnable_Type.__name__ = "Integer32"
_ModemACMProfileQPSKEnable_Object = MibScalar
modemACMProfileQPSKEnable = _ModemACMProfileQPSKEnable_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 2, 1),
    _ModemACMProfileQPSKEnable_Type()
)
modemACMProfileQPSKEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMProfileQPSKEnable.setStatus("current")


class _ModemACMProfileQAM16Enable_Type(Integer32):
    """Custom type modemACMProfileQAM16Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("DISABLED", 0),
          ("ENABLED", 1))
    )


_ModemACMProfileQAM16Enable_Type.__name__ = "Integer32"
_ModemACMProfileQAM16Enable_Object = MibScalar
modemACMProfileQAM16Enable = _ModemACMProfileQAM16Enable_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 2, 2),
    _ModemACMProfileQAM16Enable_Type()
)
modemACMProfileQAM16Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMProfileQAM16Enable.setStatus("current")


class _ModemACMProfileQAM32Enable_Type(Integer32):
    """Custom type modemACMProfileQAM32Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("DISABLED", 0),
          ("ENABLED", 1))
    )


_ModemACMProfileQAM32Enable_Type.__name__ = "Integer32"
_ModemACMProfileQAM32Enable_Object = MibScalar
modemACMProfileQAM32Enable = _ModemACMProfileQAM32Enable_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 2, 3),
    _ModemACMProfileQAM32Enable_Type()
)
modemACMProfileQAM32Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMProfileQAM32Enable.setStatus("current")


class _ModemACMProfileQAM64Enable_Type(Integer32):
    """Custom type modemACMProfileQAM64Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("DISABLED", 0),
          ("ENABLED", 1))
    )


_ModemACMProfileQAM64Enable_Type.__name__ = "Integer32"
_ModemACMProfileQAM64Enable_Object = MibScalar
modemACMProfileQAM64Enable = _ModemACMProfileQAM64Enable_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 2, 4),
    _ModemACMProfileQAM64Enable_Type()
)
modemACMProfileQAM64Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMProfileQAM64Enable.setStatus("current")


class _ModemACMProfileQAM128Enable_Type(Integer32):
    """Custom type modemACMProfileQAM128Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("DISABLED", 0),
          ("ENABLED", 1))
    )


_ModemACMProfileQAM128Enable_Type.__name__ = "Integer32"
_ModemACMProfileQAM128Enable_Object = MibScalar
modemACMProfileQAM128Enable = _ModemACMProfileQAM128Enable_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 2, 5),
    _ModemACMProfileQAM128Enable_Type()
)
modemACMProfileQAM128Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMProfileQAM128Enable.setStatus("current")


class _ModemACMProfileQAM256Enable_Type(Integer32):
    """Custom type modemACMProfileQAM256Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("DISABLED", 0),
          ("ENABLED", 1))
    )


_ModemACMProfileQAM256Enable_Type.__name__ = "Integer32"
_ModemACMProfileQAM256Enable_Object = MibScalar
modemACMProfileQAM256Enable = _ModemACMProfileQAM256Enable_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 2, 6),
    _ModemACMProfileQAM256Enable_Type()
)
modemACMProfileQAM256Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMProfileQAM256Enable.setStatus("current")
_AcmMSEImprove_ObjectIdentity = ObjectIdentity
acmMSEImprove = _AcmMSEImprove_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 3)
)
_ModemACMQPSKMSEImprove_Type = Opaque
_ModemACMQPSKMSEImprove_Object = MibScalar
modemACMQPSKMSEImprove = _ModemACMQPSKMSEImprove_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 3, 1),
    _ModemACMQPSKMSEImprove_Type()
)
modemACMQPSKMSEImprove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMQPSKMSEImprove.setStatus("current")
_ModemACMQAM16MSEImprove_Type = Opaque
_ModemACMQAM16MSEImprove_Object = MibScalar
modemACMQAM16MSEImprove = _ModemACMQAM16MSEImprove_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 3, 2),
    _ModemACMQAM16MSEImprove_Type()
)
modemACMQAM16MSEImprove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMQAM16MSEImprove.setStatus("current")
_ModemACMQAM32MSEImprove_Type = Opaque
_ModemACMQAM32MSEImprove_Object = MibScalar
modemACMQAM32MSEImprove = _ModemACMQAM32MSEImprove_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 3, 3),
    _ModemACMQAM32MSEImprove_Type()
)
modemACMQAM32MSEImprove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMQAM32MSEImprove.setStatus("current")
_ModemACMQAM64MSEImprove_Type = Opaque
_ModemACMQAM64MSEImprove_Object = MibScalar
modemACMQAM64MSEImprove = _ModemACMQAM64MSEImprove_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 3, 4),
    _ModemACMQAM64MSEImprove_Type()
)
modemACMQAM64MSEImprove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMQAM64MSEImprove.setStatus("current")
_ModemACMQAM128MSEImprove_Type = Opaque
_ModemACMQAM128MSEImprove_Object = MibScalar
modemACMQAM128MSEImprove = _ModemACMQAM128MSEImprove_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 3, 5),
    _ModemACMQAM128MSEImprove_Type()
)
modemACMQAM128MSEImprove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMQAM128MSEImprove.setStatus("current")
_ModemACMQAM256MSEImprove_Type = Opaque
_ModemACMQAM256MSEImprove_Object = MibScalar
modemACMQAM256MSEImprove = _ModemACMQAM256MSEImprove_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 3, 6),
    _ModemACMQAM256MSEImprove_Type()
)
modemACMQAM256MSEImprove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMQAM256MSEImprove.setStatus("current")
_AcmMSEDegrade_ObjectIdentity = ObjectIdentity
acmMSEDegrade = _AcmMSEDegrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 4)
)
_ModemACMQPSKMSEDegrade_Type = Opaque
_ModemACMQPSKMSEDegrade_Object = MibScalar
modemACMQPSKMSEDegrade = _ModemACMQPSKMSEDegrade_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 4, 1),
    _ModemACMQPSKMSEDegrade_Type()
)
modemACMQPSKMSEDegrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMQPSKMSEDegrade.setStatus("current")
_ModemACMQAM16MSEDegrade_Type = Opaque
_ModemACMQAM16MSEDegrade_Object = MibScalar
modemACMQAM16MSEDegrade = _ModemACMQAM16MSEDegrade_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 4, 2),
    _ModemACMQAM16MSEDegrade_Type()
)
modemACMQAM16MSEDegrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMQAM16MSEDegrade.setStatus("current")
_ModemACMQAM32MSEDegrade_Type = Opaque
_ModemACMQAM32MSEDegrade_Object = MibScalar
modemACMQAM32MSEDegrade = _ModemACMQAM32MSEDegrade_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 4, 3),
    _ModemACMQAM32MSEDegrade_Type()
)
modemACMQAM32MSEDegrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMQAM32MSEDegrade.setStatus("current")
_ModemACMQAM64MSEDegrade_Type = Opaque
_ModemACMQAM64MSEDegrade_Object = MibScalar
modemACMQAM64MSEDegrade = _ModemACMQAM64MSEDegrade_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 4, 4),
    _ModemACMQAM64MSEDegrade_Type()
)
modemACMQAM64MSEDegrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMQAM64MSEDegrade.setStatus("current")
_ModemACMQAM128MSEDegrade_Type = Opaque
_ModemACMQAM128MSEDegrade_Object = MibScalar
modemACMQAM128MSEDegrade = _ModemACMQAM128MSEDegrade_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 4, 5),
    _ModemACMQAM128MSEDegrade_Type()
)
modemACMQAM128MSEDegrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMQAM128MSEDegrade.setStatus("current")
_ModemACMQAM256MSEDegrade_Type = Opaque
_ModemACMQAM256MSEDegrade_Object = MibScalar
modemACMQAM256MSEDegrade = _ModemACMQAM256MSEDegrade_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 7, 4, 6),
    _ModemACMQAM256MSEDegrade_Type()
)
modemACMQAM256MSEDegrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMQAM256MSEDegrade.setStatus("current")
_Profile_ObjectIdentity = ObjectIdentity
profile = _Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 8)
)
_ModemACMTxProfile_Type = Integer32
_ModemACMTxProfile_Object = MibScalar
modemACMTxProfile = _ModemACMTxProfile_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 8, 1),
    _ModemACMTxProfile_Type()
)
modemACMTxProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMTxProfile.setStatus("current")
_ModemACMRxProfile_Type = Integer32
_ModemACMRxProfile_Object = MibScalar
modemACMRxProfile = _ModemACMRxProfile_Object(
    (1, 3, 6, 1, 4, 1, 5454, 1, 60, 2, 8, 2),
    _ModemACMRxProfile_Type()
)
modemACMRxProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemACMRxProfile.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRANGO-APEX-MODEM-MIB",
    **{"modem": modem,
       "modemLoopbackMode": modemLoopbackMode,
       "modemDataPattern": modemDataPattern,
       "modemBER": modemBER,
       "modemMSE": modemMSE,
       "modemFER": modemFER,
       "lock": lock,
       "modemLockStatus": modemLockStatus,
       "modemTimingLock": modemTimingLock,
       "modemPreambleLock": modemPreambleLock,
       "modemLdpcLock": modemLdpcLock,
       "modemReserved": modemReserved,
       "acm": acm,
       "modemACMEnable": modemACMEnable,
       "acmprofile": acmprofile,
       "modemACMProfileQPSKEnable": modemACMProfileQPSKEnable,
       "modemACMProfileQAM16Enable": modemACMProfileQAM16Enable,
       "modemACMProfileQAM32Enable": modemACMProfileQAM32Enable,
       "modemACMProfileQAM64Enable": modemACMProfileQAM64Enable,
       "modemACMProfileQAM128Enable": modemACMProfileQAM128Enable,
       "modemACMProfileQAM256Enable": modemACMProfileQAM256Enable,
       "acmMSEImprove": acmMSEImprove,
       "modemACMQPSKMSEImprove": modemACMQPSKMSEImprove,
       "modemACMQAM16MSEImprove": modemACMQAM16MSEImprove,
       "modemACMQAM32MSEImprove": modemACMQAM32MSEImprove,
       "modemACMQAM64MSEImprove": modemACMQAM64MSEImprove,
       "modemACMQAM128MSEImprove": modemACMQAM128MSEImprove,
       "modemACMQAM256MSEImprove": modemACMQAM256MSEImprove,
       "acmMSEDegrade": acmMSEDegrade,
       "modemACMQPSKMSEDegrade": modemACMQPSKMSEDegrade,
       "modemACMQAM16MSEDegrade": modemACMQAM16MSEDegrade,
       "modemACMQAM32MSEDegrade": modemACMQAM32MSEDegrade,
       "modemACMQAM64MSEDegrade": modemACMQAM64MSEDegrade,
       "modemACMQAM128MSEDegrade": modemACMQAM128MSEDegrade,
       "modemACMQAM256MSEDegrade": modemACMQAM256MSEDegrade,
       "profile": profile,
       "modemACMTxProfile": modemACMTxProfile,
       "modemACMRxProfile": modemACMRxProfile}
)
