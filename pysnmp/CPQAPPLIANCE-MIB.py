# SNMP MIB module (CPQAPPLIANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQAPPLIANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:14 2024
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqApplianceMgmt_ObjectIdentity = ObjectIdentity
cpqApplianceMgmt = _CpqApplianceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 21)
)
_CpqApMibRev_ObjectIdentity = ObjectIdentity
cpqApMibRev = _CpqApMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 21, 1)
)


class _CpqApMibRevMajor_Type(Integer32):
    """Custom type cpqApMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqApMibRevMajor_Type.__name__ = "Integer32"
_CpqApMibRevMajor_Object = MibScalar
cpqApMibRevMajor = _CpqApMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 21, 1, 1),
    _CpqApMibRevMajor_Type()
)
cpqApMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqApMibRevMajor.setStatus("mandatory")


class _CpqApMibRevMinor_Type(Integer32):
    """Custom type cpqApMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqApMibRevMinor_Type.__name__ = "Integer32"
_CpqApMibRevMinor_Object = MibScalar
cpqApMibRevMinor = _CpqApMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 21, 1, 2),
    _CpqApMibRevMinor_Type()
)
cpqApMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqApMibRevMinor.setStatus("mandatory")


class _CpqApMibCondition_Type(Integer32):
    """Custom type cpqApMibCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqApMibCondition_Type.__name__ = "Integer32"
_CpqApMibCondition_Object = MibScalar
cpqApMibCondition = _CpqApMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 21, 1, 3),
    _CpqApMibCondition_Type()
)
cpqApMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqApMibCondition.setStatus("mandatory")
_CpqApComponent_ObjectIdentity = ObjectIdentity
cpqApComponent = _CpqApComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 21, 2)
)
_CpqApInterface_ObjectIdentity = ObjectIdentity
cpqApInterface = _CpqApInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 21, 2, 1)
)
_CpqApOsCommon_ObjectIdentity = ObjectIdentity
cpqApOsCommon = _CpqApOsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 21, 2, 1, 4)
)


class _CpqApOsCommonPollFreq_Type(Integer32):
    """Custom type cpqApOsCommonPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpqApOsCommonPollFreq_Type.__name__ = "Integer32"
_CpqApOsCommonPollFreq_Object = MibScalar
cpqApOsCommonPollFreq = _CpqApOsCommonPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 21, 2, 1, 4, 1),
    _CpqApOsCommonPollFreq_Type()
)
cpqApOsCommonPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqApOsCommonPollFreq.setStatus("mandatory")
_CpqApConfig_ObjectIdentity = ObjectIdentity
cpqApConfig = _CpqApConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 21, 2, 2)
)
_CpqApApplianceId_Type = Integer32
_CpqApApplianceId_Object = MibScalar
cpqApApplianceId = _CpqApApplianceId_Object(
    (1, 3, 6, 1, 4, 1, 232, 21, 2, 2, 1),
    _CpqApApplianceId_Type()
)
cpqApApplianceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqApApplianceId.setStatus("mandatory")


class _CpqApApplianceDescription_Type(DisplayString):
    """Custom type cpqApApplianceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqApApplianceDescription_Type.__name__ = "DisplayString"
_CpqApApplianceDescription_Object = MibScalar
cpqApApplianceDescription = _CpqApApplianceDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 21, 2, 2, 2),
    _CpqApApplianceDescription_Type()
)
cpqApApplianceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqApApplianceDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQAPPLIANCE-MIB",
    **{"cpqApplianceMgmt": cpqApplianceMgmt,
       "cpqApMibRev": cpqApMibRev,
       "cpqApMibRevMajor": cpqApMibRevMajor,
       "cpqApMibRevMinor": cpqApMibRevMinor,
       "cpqApMibCondition": cpqApMibCondition,
       "cpqApComponent": cpqApComponent,
       "cpqApInterface": cpqApInterface,
       "cpqApOsCommon": cpqApOsCommon,
       "cpqApOsCommonPollFreq": cpqApOsCommonPollFreq,
       "cpqApConfig": cpqApConfig,
       "cpqApApplianceId": cpqApApplianceId,
       "cpqApApplianceDescription": cpqApApplianceDescription}
)
