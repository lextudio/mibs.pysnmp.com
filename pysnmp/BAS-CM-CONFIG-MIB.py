# SNMP MIB module (BAS-CM-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-CM-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:21 2024
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

(basCmConfig,) = mibBuilder.importSymbols(
    "BAS-MIB",
    "basCmConfig")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

basCmConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasCmDsFreq_Type = Integer32
_BasCmDsFreq_Object = MibScalar
basCmDsFreq = _BasCmDsFreq_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 1),
    _BasCmDsFreq_Type()
)
basCmDsFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmDsFreq.setStatus("current")
_BasCmUsChannelId_Type = Integer32
_BasCmUsChannelId_Object = MibScalar
basCmUsChannelId = _BasCmUsChannelId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 2),
    _BasCmUsChannelId_Type()
)
basCmUsChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmUsChannelId.setStatus("current")


class _BasCmNetworkAccess_Type(Integer32):
    """Custom type basCmNetworkAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_BasCmNetworkAccess_Type.__name__ = "Integer32"
_BasCmNetworkAccess_Object = MibScalar
basCmNetworkAccess = _BasCmNetworkAccess_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 3),
    _BasCmNetworkAccess_Type()
)
basCmNetworkAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmNetworkAccess.setStatus("current")
_BasCmCosTable_Object = MibTable
basCmCosTable = _BasCmCosTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4)
)
if mibBuilder.loadTexts:
    basCmCosTable.setStatus("current")
_BasCmCosEntry_Object = MibTableRow
basCmCosEntry = _BasCmCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1)
)
basCmCosEntry.setIndexNames(
    (0, "BAS-CM-CONFIG-MIB", "basCmCosClassId"),
)
if mibBuilder.loadTexts:
    basCmCosEntry.setStatus("current")
_BasCmCosClassId_Type = Integer32
_BasCmCosClassId_Object = MibTableColumn
basCmCosClassId = _BasCmCosClassId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 1),
    _BasCmCosClassId_Type()
)
basCmCosClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmCosClassId.setStatus("current")
_BasCmCosMaxDsBps_Type = Integer32
_BasCmCosMaxDsBps_Object = MibTableColumn
basCmCosMaxDsBps = _BasCmCosMaxDsBps_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 2),
    _BasCmCosMaxDsBps_Type()
)
basCmCosMaxDsBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmCosMaxDsBps.setStatus("current")
_BasCmCosMaxUsBps_Type = Integer32
_BasCmCosMaxUsBps_Object = MibTableColumn
basCmCosMaxUsBps = _BasCmCosMaxUsBps_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 3),
    _BasCmCosMaxUsBps_Type()
)
basCmCosMaxUsBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmCosMaxUsBps.setStatus("current")


class _BasCmCosUsPriority_Type(Integer32):
    """Custom type basCmCosUsPriority based on Integer32"""
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
        *(("five", 5),
          ("four", 4),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("three", 3),
          ("two", 2),
          ("zero", 0))
    )


_BasCmCosUsPriority_Type.__name__ = "Integer32"
_BasCmCosUsPriority_Object = MibTableColumn
basCmCosUsPriority = _BasCmCosUsPriority_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 4),
    _BasCmCosUsPriority_Type()
)
basCmCosUsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmCosUsPriority.setStatus("current")
_BasCmCosGuaranteedUsBps_Type = Integer32
_BasCmCosGuaranteedUsBps_Object = MibTableColumn
basCmCosGuaranteedUsBps = _BasCmCosGuaranteedUsBps_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 5),
    _BasCmCosGuaranteedUsBps_Type()
)
basCmCosGuaranteedUsBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmCosGuaranteedUsBps.setStatus("current")
_BasCmCosMaxUsBurst_Type = Integer32
_BasCmCosMaxUsBurst_Object = MibTableColumn
basCmCosMaxUsBurst = _BasCmCosMaxUsBurst_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 6),
    _BasCmCosMaxUsBurst_Type()
)
basCmCosMaxUsBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmCosMaxUsBurst.setStatus("current")


class _BasCmCosBp_Type(Integer32):
    """Custom type basCmCosBp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_BasCmCosBp_Type.__name__ = "Integer32"
_BasCmCosBp_Object = MibTableColumn
basCmCosBp = _BasCmCosBp_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 4, 1, 7),
    _BasCmCosBp_Type()
)
basCmCosBp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmCosBp.setStatus("current")
_BasCmCapabilities_ObjectIdentity = ObjectIdentity
basCmCapabilities = _BasCmCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 5)
)


class _BasCmCapConcat_Type(Integer32):
    """Custom type basCmCapConcat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_BasCmCapConcat_Type.__name__ = "Integer32"
_BasCmCapConcat_Object = MibScalar
basCmCapConcat = _BasCmCapConcat_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 5, 1),
    _BasCmCapConcat_Type()
)
basCmCapConcat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmCapConcat.setStatus("current")
_BasSnmpMibObjectTable_Object = MibTable
basSnmpMibObjectTable = _BasSnmpMibObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 11)
)
if mibBuilder.loadTexts:
    basSnmpMibObjectTable.setStatus("current")
_BasSnmpMibObjectEntry_Object = MibTableRow
basSnmpMibObjectEntry = _BasSnmpMibObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 11, 1)
)
basSnmpMibObjectEntry.setIndexNames(
    (0, "BAS-CM-CONFIG-MIB", "basSnmpMibObjectIdx"),
)
if mibBuilder.loadTexts:
    basSnmpMibObjectEntry.setStatus("current")
_BasSnmpMibObjectIdx_Type = Integer32
_BasSnmpMibObjectIdx_Object = MibTableColumn
basSnmpMibObjectIdx = _BasSnmpMibObjectIdx_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 11, 1, 1),
    _BasSnmpMibObjectIdx_Type()
)
basSnmpMibObjectIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basSnmpMibObjectIdx.setStatus("current")


class _BasSnmpMibObjectVarBind_Type(OctetString):
    """Custom type basSnmpMibObjectVarBind based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_BasSnmpMibObjectVarBind_Type.__name__ = "OctetString"
_BasSnmpMibObjectVarBind_Object = MibTableColumn
basSnmpMibObjectVarBind = _BasSnmpMibObjectVarBind_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 11, 1, 2),
    _BasSnmpMibObjectVarBind_Type()
)
basSnmpMibObjectVarBind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basSnmpMibObjectVarBind.setStatus("current")
_BasCpeAddressTable_Object = MibTable
basCpeAddressTable = _BasCpeAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 14)
)
if mibBuilder.loadTexts:
    basCpeAddressTable.setStatus("current")
_BasCpeAddressEntry_Object = MibTableRow
basCpeAddressEntry = _BasCpeAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 14, 1)
)
basCpeAddressEntry.setIndexNames(
    (0, "BAS-CM-CONFIG-MIB", "basCpeAddressIdx"),
)
if mibBuilder.loadTexts:
    basCpeAddressEntry.setStatus("current")
_BasCpeAddressIdx_Type = Integer32
_BasCpeAddressIdx_Object = MibTableColumn
basCpeAddressIdx = _BasCpeAddressIdx_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 14, 1, 1),
    _BasCpeAddressIdx_Type()
)
basCpeAddressIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCpeAddressIdx.setStatus("current")


class _BasCpeAddressMacAddr_Type(OctetString):
    """Custom type basCpeAddressMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_BasCpeAddressMacAddr_Type.__name__ = "OctetString"
_BasCpeAddressMacAddr_Object = MibTableColumn
basCpeAddressMacAddr = _BasCpeAddressMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 14, 1, 2),
    _BasCpeAddressMacAddr_Type()
)
basCpeAddressMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCpeAddressMacAddr.setStatus("current")
_BasCmBpiSettings_ObjectIdentity = ObjectIdentity
basCmBpiSettings = _BasCmBpiSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17)
)


class _BasCmBpiAuthWaitTimeout_Type(Integer32):
    """Custom type basCmBpiAuthWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BasCmBpiAuthWaitTimeout_Type.__name__ = "Integer32"
_BasCmBpiAuthWaitTimeout_Object = MibScalar
basCmBpiAuthWaitTimeout = _BasCmBpiAuthWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 1),
    _BasCmBpiAuthWaitTimeout_Type()
)
basCmBpiAuthWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmBpiAuthWaitTimeout.setStatus("current")


class _BasCmBpiReAuthWaitTimeout_Type(Integer32):
    """Custom type basCmBpiReAuthWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_BasCmBpiReAuthWaitTimeout_Type.__name__ = "Integer32"
_BasCmBpiReAuthWaitTimeout_Object = MibScalar
basCmBpiReAuthWaitTimeout = _BasCmBpiReAuthWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 2),
    _BasCmBpiReAuthWaitTimeout_Type()
)
basCmBpiReAuthWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmBpiReAuthWaitTimeout.setStatus("current")


class _BasCmBpiAuthGraceTime_Type(Integer32):
    """Custom type basCmBpiAuthGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_BasCmBpiAuthGraceTime_Type.__name__ = "Integer32"
_BasCmBpiAuthGraceTime_Object = MibScalar
basCmBpiAuthGraceTime = _BasCmBpiAuthGraceTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 3),
    _BasCmBpiAuthGraceTime_Type()
)
basCmBpiAuthGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmBpiAuthGraceTime.setStatus("current")


class _BasCmBpiOperWaitTimeout_Type(Integer32):
    """Custom type basCmBpiOperWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BasCmBpiOperWaitTimeout_Type.__name__ = "Integer32"
_BasCmBpiOperWaitTimeout_Object = MibScalar
basCmBpiOperWaitTimeout = _BasCmBpiOperWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 4),
    _BasCmBpiOperWaitTimeout_Type()
)
basCmBpiOperWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmBpiOperWaitTimeout.setStatus("current")


class _BasCmBpiRekeyWaitTimeout_Type(Integer32):
    """Custom type basCmBpiRekeyWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BasCmBpiRekeyWaitTimeout_Type.__name__ = "Integer32"
_BasCmBpiRekeyWaitTimeout_Object = MibScalar
basCmBpiRekeyWaitTimeout = _BasCmBpiRekeyWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 5),
    _BasCmBpiRekeyWaitTimeout_Type()
)
basCmBpiRekeyWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmBpiRekeyWaitTimeout.setStatus("current")


class _BasCmBpiTEKGraceTime_Type(Integer32):
    """Custom type basCmBpiTEKGraceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_BasCmBpiTEKGraceTime_Type.__name__ = "Integer32"
_BasCmBpiTEKGraceTime_Object = MibScalar
basCmBpiTEKGraceTime = _BasCmBpiTEKGraceTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 6),
    _BasCmBpiTEKGraceTime_Type()
)
basCmBpiTEKGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmBpiTEKGraceTime.setStatus("current")


class _BasCmBpiAuthRejectWaitTimeout_Type(Integer32):
    """Custom type basCmBpiAuthRejectWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_BasCmBpiAuthRejectWaitTimeout_Type.__name__ = "Integer32"
_BasCmBpiAuthRejectWaitTimeout_Object = MibScalar
basCmBpiAuthRejectWaitTimeout = _BasCmBpiAuthRejectWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 7),
    _BasCmBpiAuthRejectWaitTimeout_Type()
)
basCmBpiAuthRejectWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmBpiAuthRejectWaitTimeout.setStatus("current")


class _BasCmBpiSAMapWaitTimeout_Type(Integer32):
    """Custom type basCmBpiSAMapWaitTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BasCmBpiSAMapWaitTimeout_Type.__name__ = "Integer32"
_BasCmBpiSAMapWaitTimeout_Object = MibScalar
basCmBpiSAMapWaitTimeout = _BasCmBpiSAMapWaitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 8),
    _BasCmBpiSAMapWaitTimeout_Type()
)
basCmBpiSAMapWaitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmBpiSAMapWaitTimeout.setStatus("current")


class _BasCmBpiMaxClockDrift_Type(Integer32):
    """Custom type basCmBpiMaxClockDrift based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_BasCmBpiMaxClockDrift_Type.__name__ = "Integer32"
_BasCmBpiMaxClockDrift_Object = MibScalar
basCmBpiMaxClockDrift = _BasCmBpiMaxClockDrift_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 9),
    _BasCmBpiMaxClockDrift_Type()
)
basCmBpiMaxClockDrift.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmBpiMaxClockDrift.setStatus("current")


class _BasCmBpiSAMapMaxRetries_Type(Integer32):
    """Custom type basCmBpiSAMapMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_BasCmBpiSAMapMaxRetries_Type.__name__ = "Integer32"
_BasCmBpiSAMapMaxRetries_Object = MibScalar
basCmBpiSAMapMaxRetries = _BasCmBpiSAMapMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 17, 10),
    _BasCmBpiSAMapMaxRetries_Type()
)
basCmBpiSAMapMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmBpiSAMapMaxRetries.setStatus("current")
_BasCmMaxNumCPEs_Type = Integer32
_BasCmMaxNumCPEs_Object = MibScalar
basCmMaxNumCPEs = _BasCmMaxNumCPEs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 18),
    _BasCmMaxNumCPEs_Type()
)
basCmMaxNumCPEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmMaxNumCPEs.setStatus("current")


class _BasCmMIC_Type(OctetString):
    """Custom type basCmMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_BasCmMIC_Type.__name__ = "OctetString"
_BasCmMIC_Object = MibScalar
basCmMIC = _BasCmMIC_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 256),
    _BasCmMIC_Type()
)
basCmMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmMIC.setStatus("current")


class _BasCmtsMIC_Type(OctetString):
    """Custom type basCmtsMIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_BasCmtsMIC_Type.__name__ = "OctetString"
_BasCmtsMIC_Object = MibScalar
basCmtsMIC = _BasCmtsMIC_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 257),
    _BasCmtsMIC_Type()
)
basCmtsMIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basCmtsMIC.setStatus("current")
_BasCmEndOfMib_Type = Integer32
_BasCmEndOfMib_Object = MibScalar
basCmEndOfMib = _BasCmEndOfMib_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 12, 1, 258),
    _BasCmEndOfMib_Type()
)
basCmEndOfMib.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basCmEndOfMib.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-CM-CONFIG-MIB",
    **{"basCmConfigMIB": basCmConfigMIB,
       "basCmDsFreq": basCmDsFreq,
       "basCmUsChannelId": basCmUsChannelId,
       "basCmNetworkAccess": basCmNetworkAccess,
       "basCmCosTable": basCmCosTable,
       "basCmCosEntry": basCmCosEntry,
       "basCmCosClassId": basCmCosClassId,
       "basCmCosMaxDsBps": basCmCosMaxDsBps,
       "basCmCosMaxUsBps": basCmCosMaxUsBps,
       "basCmCosUsPriority": basCmCosUsPriority,
       "basCmCosGuaranteedUsBps": basCmCosGuaranteedUsBps,
       "basCmCosMaxUsBurst": basCmCosMaxUsBurst,
       "basCmCosBp": basCmCosBp,
       "basCmCapabilities": basCmCapabilities,
       "basCmCapConcat": basCmCapConcat,
       "basSnmpMibObjectTable": basSnmpMibObjectTable,
       "basSnmpMibObjectEntry": basSnmpMibObjectEntry,
       "basSnmpMibObjectIdx": basSnmpMibObjectIdx,
       "basSnmpMibObjectVarBind": basSnmpMibObjectVarBind,
       "basCpeAddressTable": basCpeAddressTable,
       "basCpeAddressEntry": basCpeAddressEntry,
       "basCpeAddressIdx": basCpeAddressIdx,
       "basCpeAddressMacAddr": basCpeAddressMacAddr,
       "basCmBpiSettings": basCmBpiSettings,
       "basCmBpiAuthWaitTimeout": basCmBpiAuthWaitTimeout,
       "basCmBpiReAuthWaitTimeout": basCmBpiReAuthWaitTimeout,
       "basCmBpiAuthGraceTime": basCmBpiAuthGraceTime,
       "basCmBpiOperWaitTimeout": basCmBpiOperWaitTimeout,
       "basCmBpiRekeyWaitTimeout": basCmBpiRekeyWaitTimeout,
       "basCmBpiTEKGraceTime": basCmBpiTEKGraceTime,
       "basCmBpiAuthRejectWaitTimeout": basCmBpiAuthRejectWaitTimeout,
       "basCmBpiSAMapWaitTimeout": basCmBpiSAMapWaitTimeout,
       "basCmBpiMaxClockDrift": basCmBpiMaxClockDrift,
       "basCmBpiSAMapMaxRetries": basCmBpiSAMapMaxRetries,
       "basCmMaxNumCPEs": basCmMaxNumCPEs,
       "basCmMIC": basCmMIC,
       "basCmtsMIC": basCmtsMIC,
       "basCmEndOfMib": basCmEndOfMib}
)
