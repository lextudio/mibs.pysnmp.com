# SNMP MIB module (APERTUS-UA-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APERTUS-UA-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:18 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Directory_ObjectIdentity = ObjectIdentity
directory = _Directory_ObjectIdentity(
    (1, 3, 6, 1, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Apertus_ObjectIdentity = ObjectIdentity
apertus = _Apertus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543)
)
_Isg_ObjectIdentity = ObjectIdentity
isg = _Isg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3)
)
_Aperua_ObjectIdentity = ObjectIdentity
aperua = _Aperua_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3)
)
_Aperbaseua_ObjectIdentity = ObjectIdentity
aperbaseua = _Aperbaseua_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1)
)
_AperUaMIB_ObjectIdentity = ObjectIdentity
aperUaMIB = _AperUaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1)
)
_AperUaMIBObjects_ObjectIdentity = ObjectIdentity
aperUaMIBObjects = _AperUaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1)
)
_AperUaConfig_ObjectIdentity = ObjectIdentity
aperUaConfig = _AperUaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1, 1)
)


class _AperUaConfigStatus_Type(Integer32):
    """Custom type aperUaConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("loading", 2),
          ("ready", 1))
    )


_AperUaConfigStatus_Type.__name__ = "Integer32"
_AperUaConfigStatus_Object = MibScalar
aperUaConfigStatus = _AperUaConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1, 1, 1),
    _AperUaConfigStatus_Type()
)
aperUaConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperUaConfigStatus.setStatus("mandatory")
_AperUaConfigUpTime_Type = TimeTicks
_AperUaConfigUpTime_Object = MibScalar
aperUaConfigUpTime = _AperUaConfigUpTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1, 1, 2),
    _AperUaConfigUpTime_Type()
)
aperUaConfigUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperUaConfigUpTime.setStatus("mandatory")
_AperUaConfigResetTime_Type = TimeTicks
_AperUaConfigResetTime_Object = MibScalar
aperUaConfigResetTime = _AperUaConfigResetTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1, 1, 3),
    _AperUaConfigResetTime_Type()
)
aperUaConfigResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperUaConfigResetTime.setStatus("mandatory")
_AperUaDomain_ObjectIdentity = ObjectIdentity
aperUaDomain = _AperUaDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1, 2)
)
_AperUaDomainTable_Object = MibTable
aperUaDomainTable = _AperUaDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aperUaDomainTable.setStatus("mandatory")
_AperUaDomainEntry_Object = MibTableRow
aperUaDomainEntry = _AperUaDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1, 2, 1, 1)
)
aperUaDomainEntry.setIndexNames(
    (0, "APERTUS-UA-BASE-MIB", "aperUaDomainName"),
)
if mibBuilder.loadTexts:
    aperUaDomainEntry.setStatus("mandatory")
_AperUaDomainName_Type = DisplayString
_AperUaDomainName_Object = MibTableColumn
aperUaDomainName = _AperUaDomainName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1, 2, 1, 1, 1),
    _AperUaDomainName_Type()
)
aperUaDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperUaDomainName.setStatus("mandatory")
_AperUaDomainQueries_Type = Counter32
_AperUaDomainQueries_Object = MibTableColumn
aperUaDomainQueries = _AperUaDomainQueries_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1, 2, 1, 1, 2),
    _AperUaDomainQueries_Type()
)
aperUaDomainQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperUaDomainQueries.setStatus("mandatory")
_AperUaDomainLastAnswer_Type = IpAddress
_AperUaDomainLastAnswer_Object = MibTableColumn
aperUaDomainLastAnswer = _AperUaDomainLastAnswer_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1, 2, 1, 1, 3),
    _AperUaDomainLastAnswer_Type()
)
aperUaDomainLastAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperUaDomainLastAnswer.setStatus("mandatory")
_AperUaDomainLastQueryTime_Type = TimeTicks
_AperUaDomainLastQueryTime_Object = MibTableColumn
aperUaDomainLastQueryTime = _AperUaDomainLastQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1, 2, 1, 1, 4),
    _AperUaDomainLastQueryTime_Type()
)
aperUaDomainLastQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperUaDomainLastQueryTime.setStatus("mandatory")


class _AperUaDomainType_Type(DisplayString):
    """Custom type aperUaDomainType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AperUaDomainType_Type.__name__ = "DisplayString"
_AperUaDomainType_Object = MibTableColumn
aperUaDomainType = _AperUaDomainType_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1, 2, 1, 1, 5),
    _AperUaDomainType_Type()
)
aperUaDomainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperUaDomainType.setStatus("mandatory")
_AperUaDomainTypeOID_Type = ObjectIdentifier
_AperUaDomainTypeOID_Object = MibTableColumn
aperUaDomainTypeOID = _AperUaDomainTypeOID_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 1, 1, 1, 2, 1, 1, 6),
    _AperUaDomainTypeOID_Type()
)
aperUaDomainTypeOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperUaDomainTypeOID.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APERTUS-UA-BASE-MIB",
    **{"internet": internet,
       "directory": directory,
       "mgmt": mgmt,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "apertus": apertus,
       "isg": isg,
       "aperua": aperua,
       "aperbaseua": aperbaseua,
       "aperUaMIB": aperUaMIB,
       "aperUaMIBObjects": aperUaMIBObjects,
       "aperUaConfig": aperUaConfig,
       "aperUaConfigStatus": aperUaConfigStatus,
       "aperUaConfigUpTime": aperUaConfigUpTime,
       "aperUaConfigResetTime": aperUaConfigResetTime,
       "aperUaDomain": aperUaDomain,
       "aperUaDomainTable": aperUaDomainTable,
       "aperUaDomainEntry": aperUaDomainEntry,
       "aperUaDomainName": aperUaDomainName,
       "aperUaDomainQueries": aperUaDomainQueries,
       "aperUaDomainLastAnswer": aperUaDomainLastAnswer,
       "aperUaDomainLastQueryTime": aperUaDomainLastQueryTime,
       "aperUaDomainType": aperUaDomainType,
       "aperUaDomainTypeOID": aperUaDomainTypeOID}
)
