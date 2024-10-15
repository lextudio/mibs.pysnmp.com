# SNMP MIB module (ADTRAN-AOSSNMP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOSSNMP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:19 2024
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

(adGenAOSCommon,
 adGenAOSConformance) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSCommon",
    "adGenAOSConformance")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

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
 RowStatus,
 TAddress,
 TDomain,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention")


# MODULE-IDENTITY

adGenAOSSnmpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 2)
)
adGenAOSSnmpMib.setRevisions(
        ("2008-10-20 00:00",
         "2008-10-09 00:00",
         "2004-09-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSSnmp_ObjectIdentity = ObjectIdentity
adGenAOSSnmp = _AdGenAOSSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2)
)
_AdAOSSNMPCommunitiesTable_Object = MibTable
adAOSSNMPCommunitiesTable = _AdAOSSNMPCommunitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adAOSSNMPCommunitiesTable.setStatus("current")
_AdAOSSNMPCommunitiesEntry_Object = MibTableRow
adAOSSNMPCommunitiesEntry = _AdAOSSNMPCommunitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1)
)
adAOSSNMPCommunitiesEntry.setIndexNames(
    (0, "ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesIndex"),
)
if mibBuilder.loadTexts:
    adAOSSNMPCommunitiesEntry.setStatus("current")


class _AdAOSSNMPCommunitiesIndex_Type(Integer32):
    """Custom type adAOSSNMPCommunitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AdAOSSNMPCommunitiesIndex_Type.__name__ = "Integer32"
_AdAOSSNMPCommunitiesIndex_Object = MibTableColumn
adAOSSNMPCommunitiesIndex = _AdAOSSNMPCommunitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 1),
    _AdAOSSNMPCommunitiesIndex_Type()
)
adAOSSNMPCommunitiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adAOSSNMPCommunitiesIndex.setStatus("current")


class _AdAOSSNMPCommunitiesString_Type(DisplayString):
    """Custom type adAOSSNMPCommunitiesString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AdAOSSNMPCommunitiesString_Type.__name__ = "DisplayString"
_AdAOSSNMPCommunitiesString_Object = MibTableColumn
adAOSSNMPCommunitiesString = _AdAOSSNMPCommunitiesString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 2),
    _AdAOSSNMPCommunitiesString_Type()
)
adAOSSNMPCommunitiesString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSSNMPCommunitiesString.setStatus("current")


class _AdAOSSNMPCommunitiesPrivilege_Type(Integer32):
    """Custom type adAOSSNMPCommunitiesPrivilege based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("set", 2))
    )


_AdAOSSNMPCommunitiesPrivilege_Type.__name__ = "Integer32"
_AdAOSSNMPCommunitiesPrivilege_Object = MibTableColumn
adAOSSNMPCommunitiesPrivilege = _AdAOSSNMPCommunitiesPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 3),
    _AdAOSSNMPCommunitiesPrivilege_Type()
)
adAOSSNMPCommunitiesPrivilege.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSSNMPCommunitiesPrivilege.setStatus("current")
_AdAOSSNMPCommunitiesStatus_Type = RowStatus
_AdAOSSNMPCommunitiesStatus_Object = MibTableColumn
adAOSSNMPCommunitiesStatus = _AdAOSSNMPCommunitiesStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 4),
    _AdAOSSNMPCommunitiesStatus_Type()
)
adAOSSNMPCommunitiesStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSSNMPCommunitiesStatus.setStatus("current")
_AdAOSSNMPTrapsTable_Object = MibTable
adAOSSNMPTrapsTable = _AdAOSSNMPTrapsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2)
)
if mibBuilder.loadTexts:
    adAOSSNMPTrapsTable.setStatus("current")
_AdAOSSNMPTrapsEntry_Object = MibTableRow
adAOSSNMPTrapsEntry = _AdAOSSNMPTrapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1)
)
adAOSSNMPTrapsEntry.setIndexNames(
    (0, "ADTRAN-AOSSNMP", "adAOSSNMPTrapsIndex"),
)
if mibBuilder.loadTexts:
    adAOSSNMPTrapsEntry.setStatus("current")
_AdAOSSNMPTrapsIndex_Type = Integer32
_AdAOSSNMPTrapsIndex_Object = MibTableColumn
adAOSSNMPTrapsIndex = _AdAOSSNMPTrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 1),
    _AdAOSSNMPTrapsIndex_Type()
)
adAOSSNMPTrapsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adAOSSNMPTrapsIndex.setStatus("current")


class _AdAOSSNMPTrapsString_Type(DisplayString):
    """Custom type adAOSSNMPTrapsString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdAOSSNMPTrapsString_Type.__name__ = "DisplayString"
_AdAOSSNMPTrapsString_Object = MibTableColumn
adAOSSNMPTrapsString = _AdAOSSNMPTrapsString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 2),
    _AdAOSSNMPTrapsString_Type()
)
adAOSSNMPTrapsString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSSNMPTrapsString.setStatus("current")


class _AdAOSSNMPTrapsMngmtAddr_Type(DisplayString):
    """Custom type adAOSSNMPTrapsMngmtAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdAOSSNMPTrapsMngmtAddr_Type.__name__ = "DisplayString"
_AdAOSSNMPTrapsMngmtAddr_Object = MibTableColumn
adAOSSNMPTrapsMngmtAddr = _AdAOSSNMPTrapsMngmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 3),
    _AdAOSSNMPTrapsMngmtAddr_Type()
)
adAOSSNMPTrapsMngmtAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSSNMPTrapsMngmtAddr.setStatus("current")
_AdAOSSNMPTrapsStatus_Type = RowStatus
_AdAOSSNMPTrapsStatus_Object = MibTableColumn
adAOSSNMPTrapsStatus = _AdAOSSNMPTrapsStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 4),
    _AdAOSSNMPTrapsStatus_Type()
)
adAOSSNMPTrapsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adAOSSNMPTrapsStatus.setStatus("current")


class _AdAOSSNMPEnableTraps_Type(Integer32):
    """Custom type adAOSSNMPEnableTraps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AdAOSSNMPEnableTraps_Type.__name__ = "Integer32"
_AdAOSSNMPEnableTraps_Object = MibScalar
adAOSSNMPEnableTraps = _AdAOSSNMPEnableTraps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 3),
    _AdAOSSNMPEnableTraps_Type()
)
adAOSSNMPEnableTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adAOSSNMPEnableTraps.setStatus("current")


class _AdAOSSNMPAuthenticationTraps_Type(Integer32):
    """Custom type adAOSSNMPAuthenticationTraps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AdAOSSNMPAuthenticationTraps_Type.__name__ = "Integer32"
_AdAOSSNMPAuthenticationTraps_Object = MibScalar
adAOSSNMPAuthenticationTraps = _AdAOSSNMPAuthenticationTraps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 4),
    _AdAOSSNMPAuthenticationTraps_Type()
)
adAOSSNMPAuthenticationTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adAOSSNMPAuthenticationTraps.setStatus("current")
_AdGenAOSSnmpConformance_ObjectIdentity = ObjectIdentity
adGenAOSSnmpConformance = _AdGenAOSSnmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2)
)
_AdAOSSnmpCompliances_ObjectIdentity = ObjectIdentity
adAOSSnmpCompliances = _AdAOSSnmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 1)
)
_AdAOSSnmpGroups_ObjectIdentity = ObjectIdentity
adAOSSnmpGroups = _AdAOSSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 2)
)

# Managed Objects groups

adAOSSNMPConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 2, 1)
)
adAOSSNMPConfigGroup.setObjects(
      *(("ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesString"),
        ("ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesPrivilege"),
        ("ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesStatus"),
        ("ADTRAN-AOSSNMP", "adAOSSNMPEnableTraps"),
        ("ADTRAN-AOSSNMP", "adAOSSNMPAuthenticationTraps"),
        ("ADTRAN-AOSSNMP", "adAOSSNMPTrapsString"),
        ("ADTRAN-AOSSNMP", "adAOSSNMPTrapsMngmtAddr"),
        ("ADTRAN-AOSSNMP", "adAOSSNMPTrapsStatus"))
)
if mibBuilder.loadTexts:
    adAOSSNMPConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adAOSSnmpConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 1, 1)
)
if mibBuilder.loadTexts:
    adAOSSnmpConfigCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOSSNMP",
    **{"adGenAOSSnmp": adGenAOSSnmp,
       "adAOSSNMPCommunitiesTable": adAOSSNMPCommunitiesTable,
       "adAOSSNMPCommunitiesEntry": adAOSSNMPCommunitiesEntry,
       "adAOSSNMPCommunitiesIndex": adAOSSNMPCommunitiesIndex,
       "adAOSSNMPCommunitiesString": adAOSSNMPCommunitiesString,
       "adAOSSNMPCommunitiesPrivilege": adAOSSNMPCommunitiesPrivilege,
       "adAOSSNMPCommunitiesStatus": adAOSSNMPCommunitiesStatus,
       "adAOSSNMPTrapsTable": adAOSSNMPTrapsTable,
       "adAOSSNMPTrapsEntry": adAOSSNMPTrapsEntry,
       "adAOSSNMPTrapsIndex": adAOSSNMPTrapsIndex,
       "adAOSSNMPTrapsString": adAOSSNMPTrapsString,
       "adAOSSNMPTrapsMngmtAddr": adAOSSNMPTrapsMngmtAddr,
       "adAOSSNMPTrapsStatus": adAOSSNMPTrapsStatus,
       "adAOSSNMPEnableTraps": adAOSSNMPEnableTraps,
       "adAOSSNMPAuthenticationTraps": adAOSSNMPAuthenticationTraps,
       "adGenAOSSnmpConformance": adGenAOSSnmpConformance,
       "adAOSSnmpCompliances": adAOSSnmpCompliances,
       "adAOSSnmpConfigCompliance": adAOSSnmpConfigCompliance,
       "adAOSSnmpGroups": adAOSSnmpGroups,
       "adAOSSNMPConfigGroup": adAOSSNMPConfigGroup,
       "adGenAOSSnmpMib": adGenAOSSnmpMib}
)
