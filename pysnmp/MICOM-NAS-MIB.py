# SNMP MIB module (MICOM-NAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-NAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:47 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

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

_Micom_nas_ObjectIdentity = ObjectIdentity
micom_nas = _Micom_nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16)
)
_NasBase_ObjectIdentity = ObjectIdentity
nasBase = _NasBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 1)
)


class _NasOSCARHelloTime_Type(Integer32):
    """Custom type nasOSCARHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 8000),
    )


_NasOSCARHelloTime_Type.__name__ = "Integer32"
_NasOSCARHelloTime_Object = MibScalar
nasOSCARHelloTime = _NasOSCARHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 1, 1),
    _NasOSCARHelloTime_Type()
)
nasOSCARHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nasOSCARHelloTime.setStatus("mandatory")


class _NasOSCARCntrZero_Type(Integer32):
    """Custom type nasOSCARCntrZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_NasOSCARCntrZero_Type.__name__ = "Integer32"
_NasOSCARCntrZero_Object = MibScalar
nasOSCARCntrZero = _NasOSCARCntrZero_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 1, 2),
    _NasOSCARCntrZero_Type()
)
nasOSCARCntrZero.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nasOSCARCntrZero.setStatus("obsolete")
_NasOSCARTableSize_Type = Counter32
_NasOSCARTableSize_Object = MibScalar
nasOSCARTableSize = _NasOSCARTableSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 1, 3),
    _NasOSCARTableSize_Type()
)
nasOSCARTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOSCARTableSize.setStatus("mandatory")
_NasDNDNAdbSize_Type = Counter32
_NasDNDNAdbSize_Object = MibScalar
nasDNDNAdbSize = _NasDNDNAdbSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 1, 4),
    _NasDNDNAdbSize_Type()
)
nasDNDNAdbSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDNDNAdbSize.setStatus("mandatory")
_NasStat_ObjectIdentity = ObjectIdentity
nasStat = _NasStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 2)
)
_NasInDNARequests_Type = Counter32
_NasInDNARequests_Object = MibScalar
nasInDNARequests = _NasInDNARequests_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 2, 1),
    _NasInDNARequests_Type()
)
nasInDNARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasInDNARequests.setStatus("mandatory")
_NasInDNAResolveds_Type = Counter32
_NasInDNAResolveds_Object = MibScalar
nasInDNAResolveds = _NasInDNAResolveds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 2, 2),
    _NasInDNAResolveds_Type()
)
nasInDNAResolveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasInDNAResolveds.setStatus("mandatory")
_NasInDNAUnResolveds_Type = Counter32
_NasInDNAUnResolveds_Object = MibScalar
nasInDNAUnResolveds = _NasInDNAUnResolveds_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 2, 3),
    _NasInDNAUnResolveds_Type()
)
nasInDNAUnResolveds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasInDNAUnResolveds.setStatus("mandatory")
_NasInNACHellos_Type = Counter32
_NasInNACHellos_Object = MibScalar
nasInNACHellos = _NasInNACHellos_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 2, 4),
    _NasInNACHellos_Type()
)
nasInNACHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasInNACHellos.setStatus("mandatory")
_NasInRegisters_Type = Counter32
_NasInRegisters_Object = MibScalar
nasInRegisters = _NasInRegisters_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 2, 5),
    _NasInRegisters_Type()
)
nasInRegisters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasInRegisters.setStatus("mandatory")
_NasInUnknowns_Type = Counter32
_NasInUnknowns_Object = MibScalar
nasInUnknowns = _NasInUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 2, 6),
    _NasInUnknowns_Type()
)
nasInUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasInUnknowns.setStatus("mandatory")
_NasOSCARRegSuccess_Type = Counter32
_NasOSCARRegSuccess_Object = MibScalar
nasOSCARRegSuccess = _NasOSCARRegSuccess_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 2, 7),
    _NasOSCARRegSuccess_Type()
)
nasOSCARRegSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOSCARRegSuccess.setStatus("mandatory")
_NasOSCARRegFails_Type = Counter32
_NasOSCARRegFails_Object = MibScalar
nasOSCARRegFails = _NasOSCARRegFails_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 2, 8),
    _NasOSCARRegFails_Type()
)
nasOSCARRegFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOSCARRegFails.setStatus("mandatory")
_NasOSCARTimedOuts_Type = Counter32
_NasOSCARTimedOuts_Object = MibScalar
nasOSCARTimedOuts = _NasOSCARTimedOuts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 2, 9),
    _NasOSCARTimedOuts_Type()
)
nasOSCARTimedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOSCARTimedOuts.setStatus("mandatory")
_NasOutNASHellos_Type = Counter32
_NasOutNASHellos_Object = MibScalar
nasOutNASHellos = _NasOutNASHellos_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 2, 10),
    _NasOutNASHellos_Type()
)
nasOutNASHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOutNASHellos.setStatus("mandatory")
_NasOutRegisterRequests_Type = Counter32
_NasOutRegisterRequests_Object = MibScalar
nasOutRegisterRequests = _NasOutRegisterRequests_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 2, 11),
    _NasOutRegisterRequests_Type()
)
nasOutRegisterRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOutRegisterRequests.setStatus("mandatory")
_NasOscar_ObjectIdentity = ObjectIdentity
nasOscar = _NasOscar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 3)
)
_NasOSCARTable_Object = MibTable
nasOSCARTable = _NasOSCARTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 3, 1)
)
if mibBuilder.loadTexts:
    nasOSCARTable.setStatus("mandatory")
_NasOSCAREntry_Object = MibTableRow
nasOSCAREntry = _NasOSCAREntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 3, 1, 1)
)
nasOSCAREntry.setIndexNames(
    (0, "MICOM-NAS-MIB", "nasOSCARCustomerId"),
    (0, "MICOM-NAS-MIB", "nasOSCARDNADigits"),
)
if mibBuilder.loadTexts:
    nasOSCAREntry.setStatus("mandatory")


class _NasOSCARCustomerId_Type(Integer32):
    """Custom type nasOSCARCustomerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NasOSCARCustomerId_Type.__name__ = "Integer32"
_NasOSCARCustomerId_Object = MibTableColumn
nasOSCARCustomerId = _NasOSCARCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 3, 1, 1, 1),
    _NasOSCARCustomerId_Type()
)
nasOSCARCustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOSCARCustomerId.setStatus("mandatory")


class _NasOSCARDNADigits_Type(DisplayString):
    """Custom type nasOSCARDNADigits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_NasOSCARDNADigits_Type.__name__ = "DisplayString"
_NasOSCARDNADigits_Object = MibTableColumn
nasOSCARDNADigits = _NasOSCARDNADigits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 3, 1, 1, 2),
    _NasOSCARDNADigits_Type()
)
nasOSCARDNADigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOSCARDNADigits.setStatus("mandatory")


class _NasOSCARState_Type(Integer32):
    """Custom type nasOSCARState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NasOSCARState_Type.__name__ = "Integer32"
_NasOSCARState_Object = MibTableColumn
nasOSCARState = _NasOSCARState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 3, 1, 1, 3),
    _NasOSCARState_Type()
)
nasOSCARState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOSCARState.setStatus("mandatory")
_NasOSCARIpAddr_Type = IpAddress
_NasOSCARIpAddr_Object = MibTableColumn
nasOSCARIpAddr = _NasOSCARIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 3, 1, 1, 4),
    _NasOSCARIpAddr_Type()
)
nasOSCARIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOSCARIpAddr.setStatus("mandatory")
_NasOSCARSuppDns_Type = Counter32
_NasOSCARSuppDns_Object = MibTableColumn
nasOSCARSuppDns = _NasOSCARSuppDns_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 3, 1, 1, 5),
    _NasOSCARSuppDns_Type()
)
nasOSCARSuppDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasOSCARSuppDns.setStatus("mandatory")
_NasDn_ObjectIdentity = ObjectIdentity
nasDn = _NasDn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 4)
)
_NasDNTable_Object = MibTable
nasDNTable = _NasDNTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 4, 1)
)
if mibBuilder.loadTexts:
    nasDNTable.setStatus("mandatory")
_NasDNEntry_Object = MibTableRow
nasDNEntry = _NasDNEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 4, 1, 1)
)
nasDNEntry.setIndexNames(
    (0, "MICOM-NAS-MIB", "nasDNCustomerId"),
    (0, "MICOM-NAS-MIB", "nasDNDigits"),
)
if mibBuilder.loadTexts:
    nasDNEntry.setStatus("mandatory")


class _NasDNCustomerId_Type(Integer32):
    """Custom type nasDNCustomerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NasDNCustomerId_Type.__name__ = "Integer32"
_NasDNCustomerId_Object = MibTableColumn
nasDNCustomerId = _NasDNCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 4, 1, 1, 1),
    _NasDNCustomerId_Type()
)
nasDNCustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDNCustomerId.setStatus("mandatory")


class _NasDNDigits_Type(DisplayString):
    """Custom type nasDNDigits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NasDNDigits_Type.__name__ = "DisplayString"
_NasDNDigits_Object = MibTableColumn
nasDNDigits = _NasDNDigits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 4, 1, 1, 2),
    _NasDNDigits_Type()
)
nasDNDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDNDigits.setStatus("mandatory")


class _NasDNDNADigits_Type(DisplayString):
    """Custom type nasDNDNADigits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_NasDNDNADigits_Type.__name__ = "DisplayString"
_NasDNDNADigits_Object = MibTableColumn
nasDNDNADigits = _NasDNDNADigits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 4, 1, 1, 3),
    _NasDNDNADigits_Type()
)
nasDNDNADigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDNDNADigits.setStatus("mandatory")


class _NasDNState_Type(Integer32):
    """Custom type nasDNState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NasDNState_Type.__name__ = "Integer32"
_NasDNState_Object = MibTableColumn
nasDNState = _NasDNState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 4, 1, 1, 4),
    _NasDNState_Type()
)
nasDNState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasDNState.setStatus("mandatory")
_NasNvParam_ObjectIdentity = ObjectIdentity
nasNvParam = _NasNvParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 5)
)


class _NasNvOSCARHelloTime_Type(Integer32):
    """Custom type nasNvOSCARHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 8000),
    )


_NasNvOSCARHelloTime_Type.__name__ = "Integer32"
_NasNvOSCARHelloTime_Object = MibScalar
nasNvOSCARHelloTime = _NasNvOSCARHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 16, 5, 1),
    _NasNvOSCARHelloTime_Type()
)
nasNvOSCARHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nasNvOSCARHelloTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-NAS-MIB",
    **{"micom-nas": micom_nas,
       "nasBase": nasBase,
       "nasOSCARHelloTime": nasOSCARHelloTime,
       "nasOSCARCntrZero": nasOSCARCntrZero,
       "nasOSCARTableSize": nasOSCARTableSize,
       "nasDNDNAdbSize": nasDNDNAdbSize,
       "nasStat": nasStat,
       "nasInDNARequests": nasInDNARequests,
       "nasInDNAResolveds": nasInDNAResolveds,
       "nasInDNAUnResolveds": nasInDNAUnResolveds,
       "nasInNACHellos": nasInNACHellos,
       "nasInRegisters": nasInRegisters,
       "nasInUnknowns": nasInUnknowns,
       "nasOSCARRegSuccess": nasOSCARRegSuccess,
       "nasOSCARRegFails": nasOSCARRegFails,
       "nasOSCARTimedOuts": nasOSCARTimedOuts,
       "nasOutNASHellos": nasOutNASHellos,
       "nasOutRegisterRequests": nasOutRegisterRequests,
       "nasOscar": nasOscar,
       "nasOSCARTable": nasOSCARTable,
       "nasOSCAREntry": nasOSCAREntry,
       "nasOSCARCustomerId": nasOSCARCustomerId,
       "nasOSCARDNADigits": nasOSCARDNADigits,
       "nasOSCARState": nasOSCARState,
       "nasOSCARIpAddr": nasOSCARIpAddr,
       "nasOSCARSuppDns": nasOSCARSuppDns,
       "nasDn": nasDn,
       "nasDNTable": nasDNTable,
       "nasDNEntry": nasDNEntry,
       "nasDNCustomerId": nasDNCustomerId,
       "nasDNDigits": nasDNDigits,
       "nasDNDNADigits": nasDNDNADigits,
       "nasDNState": nasDNState,
       "nasNvParam": nasNvParam,
       "nasNvOSCARHelloTime": nasNvOSCARHelloTime}
)
