# SNMP MIB module (CISCO-WAN-T38-FAXRELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-T38-FAXRELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:21 2024
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

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoWanT38FaxRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 19)
)
ciscoWanT38FaxRelayMIB.setRevisions(
        ("2004-02-19 00:00",
         "2002-06-01 00:00",
         "2002-04-12 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWanT38FaxRelayMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanT38FaxRelayMIBObjects = _CiscoWanT38FaxRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1)
)
_T38FaxRelayGrp_ObjectIdentity = ObjectIdentity
t38FaxRelayGrp = _T38FaxRelayGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1)
)
_T38FaxRelayGrpTable_Object = MibTable
t38FaxRelayGrpTable = _T38FaxRelayGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t38FaxRelayGrpTable.setStatus("current")
_T38FaxRelayGrpEntry_Object = MibTableRow
t38FaxRelayGrpEntry = _T38FaxRelayGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1)
)
t38FaxRelayGrpEntry.setIndexNames(
    (0, "CISCO-WAN-T38-FAXRELAY-MIB", "t38vismDs1Number"),
)
if mibBuilder.loadTexts:
    t38FaxRelayGrpEntry.setStatus("current")


class _T38vismDs1Number_Type(Integer32):
    """Custom type t38vismDs1Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_T38vismDs1Number_Type.__name__ = "Integer32"
_T38vismDs1Number_Object = MibTableColumn
t38vismDs1Number = _T38vismDs1Number_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 1),
    _T38vismDs1Number_Type()
)
t38vismDs1Number.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t38vismDs1Number.setStatus("current")


class _T38MaxFaxTxRate_Type(Integer32):
    """Custom type t38MaxFaxTxRate based on Integer32"""
    defaultValue = 6

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
        *(("fx12000bps", 5),
          ("fx14400bps", 6),
          ("fx2400bps", 1),
          ("fx4800bps", 2),
          ("fx7200bps", 3),
          ("fx9600bps", 4))
    )


_T38MaxFaxTxRate_Type.__name__ = "Integer32"
_T38MaxFaxTxRate_Object = MibTableColumn
t38MaxFaxTxRate = _T38MaxFaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 2),
    _T38MaxFaxTxRate_Type()
)
t38MaxFaxTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38MaxFaxTxRate.setStatus("current")


class _T38FaxInfoFieldSize_Type(Integer32):
    """Custom type t38FaxInfoFieldSize based on Integer32"""
    defaultValue = 48

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_T38FaxInfoFieldSize_Type.__name__ = "Integer32"
_T38FaxInfoFieldSize_Object = MibTableColumn
t38FaxInfoFieldSize = _T38FaxInfoFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 3),
    _T38FaxInfoFieldSize_Type()
)
t38FaxInfoFieldSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38FaxInfoFieldSize.setStatus("deprecated")


class _T38HsDataPacketSize_Type(Integer32):
    """Custom type t38HsDataPacketSize based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40)
        )
    )
    namedValues = NamedValues(
        *(("fortyms", 40),
          ("tenms", 10),
          ("thirtyms", 30),
          ("twentyms", 20))
    )


_T38HsDataPacketSize_Type.__name__ = "Integer32"
_T38HsDataPacketSize_Object = MibTableColumn
t38HsDataPacketSize = _T38HsDataPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 4),
    _T38HsDataPacketSize_Type()
)
t38HsDataPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38HsDataPacketSize.setStatus("current")


class _T38LsDataRedundancy_Type(Integer32):
    """Custom type t38LsDataRedundancy based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_T38LsDataRedundancy_Type.__name__ = "Integer32"
_T38LsDataRedundancy_Object = MibTableColumn
t38LsDataRedundancy = _T38LsDataRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 5),
    _T38LsDataRedundancy_Type()
)
t38LsDataRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38LsDataRedundancy.setStatus("current")


class _T38HsDataRedundancy_Type(Integer32):
    """Custom type t38HsDataRedundancy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_T38HsDataRedundancy_Type.__name__ = "Integer32"
_T38HsDataRedundancy_Object = MibTableColumn
t38HsDataRedundancy = _T38HsDataRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 6),
    _T38HsDataRedundancy_Type()
)
t38HsDataRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38HsDataRedundancy.setStatus("current")


class _T38TCFmethod_Type(Integer32):
    """Custom type t38TCFmethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTCF", 1),
          ("networkTCF", 2))
    )


_T38TCFmethod_Type.__name__ = "Integer32"
_T38TCFmethod_Object = MibTableColumn
t38TCFmethod = _T38TCFmethod_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 7),
    _T38TCFmethod_Type()
)
t38TCFmethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38TCFmethod.setStatus("current")


class _T38ErrCorrection_Type(Integer32):
    """Custom type t38ErrCorrection based on Integer32"""
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


_T38ErrCorrection_Type.__name__ = "Integer32"
_T38ErrCorrection_Object = MibTableColumn
t38ErrCorrection = _T38ErrCorrection_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 8),
    _T38ErrCorrection_Type()
)
t38ErrCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38ErrCorrection.setStatus("deprecated")


class _T38NSFOverride_Type(Integer32):
    """Custom type t38NSFOverride based on Integer32"""
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


_T38NSFOverride_Type.__name__ = "Integer32"
_T38NSFOverride_Object = MibTableColumn
t38NSFOverride = _T38NSFOverride_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 9),
    _T38NSFOverride_Type()
)
t38NSFOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38NSFOverride.setStatus("current")


class _T38NSFCountryCode_Type(Integer32):
    """Custom type t38NSFCountryCode based on Integer32"""
    defaultValue = 173

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_T38NSFCountryCode_Type.__name__ = "Integer32"
_T38NSFCountryCode_Object = MibTableColumn
t38NSFCountryCode = _T38NSFCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 10),
    _T38NSFCountryCode_Type()
)
t38NSFCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38NSFCountryCode.setStatus("current")


class _T38NSFVendorCode_Type(Integer32):
    """Custom type t38NSFVendorCode based on Integer32"""
    defaultValue = 81

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_T38NSFVendorCode_Type.__name__ = "Integer32"
_T38NSFVendorCode_Object = MibTableColumn
t38NSFVendorCode = _T38NSFVendorCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 11),
    _T38NSFVendorCode_Type()
)
t38NSFVendorCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38NSFVendorCode.setStatus("current")


class _T38NseAckTimeOut_Type(Integer32):
    """Custom type t38NseAckTimeOut based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 10000),
    )


_T38NseAckTimeOut_Type.__name__ = "Integer32"
_T38NseAckTimeOut_Object = MibTableColumn
t38NseAckTimeOut = _T38NseAckTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 12),
    _T38NseAckTimeOut_Type()
)
t38NseAckTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38NseAckTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    t38NseAckTimeOut.setUnits("milliseconds")


class _T38FxLCO_Type(Integer32):
    """Custom type t38FxLCO based on Integer32"""
    defaultValue = 1

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
        *(("gw", 2),
          ("gwAndPt", 1),
          ("off", 5),
          ("pt", 4),
          ("ptAndGw", 3))
    )


_T38FxLCO_Type.__name__ = "Integer32"
_T38FxLCO_Object = MibTableColumn
t38FxLCO = _T38FxLCO_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 13),
    _T38FxLCO_Type()
)
t38FxLCO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38FxLCO.setStatus("current")


class _T38Redundancy_Type(Integer32):
    """Custom type t38Redundancy based on Integer32"""
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


_T38Redundancy_Type.__name__ = "Integer32"
_T38Redundancy_Object = MibTableColumn
t38Redundancy = _T38Redundancy_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 14),
    _T38Redundancy_Type()
)
t38Redundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38Redundancy.setStatus("deprecated")


class _T38T30ECM_Type(Integer32):
    """Custom type t38T30ECM based on Integer32"""
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


_T38T30ECM_Type.__name__ = "Integer32"
_T38T30ECM_Object = MibTableColumn
t38T30ECM = _T38T30ECM_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 1, 1, 1, 1, 15),
    _T38T30ECM_Type()
)
t38T30ECM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t38T30ECM.setStatus("current")
_T38NotificationPrefix_ObjectIdentity = ObjectIdentity
t38NotificationPrefix = _T38NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 2)
)
_T38Notifications_ObjectIdentity = ObjectIdentity
t38Notifications = _T38Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 2, 0)
)
_T38FaxRelayMIBConformance_ObjectIdentity = ObjectIdentity
t38FaxRelayMIBConformance = _T38FaxRelayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 3)
)
_T38FaxRelayMIBCompliances_ObjectIdentity = ObjectIdentity
t38FaxRelayMIBCompliances = _T38FaxRelayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 3, 1)
)
_T38FaxRelayMIBGroups_ObjectIdentity = ObjectIdentity
t38FaxRelayMIBGroups = _T38FaxRelayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 3, 2)
)

# Managed Objects groups

t38FaxRelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 3, 2, 1)
)
t38FaxRelayGroup.setObjects(
      *(("CISCO-WAN-T38-FAXRELAY-MIB", "t38MaxFaxTxRate"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38FaxInfoFieldSize"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38HsDataPacketSize"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38LsDataRedundancy"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38HsDataRedundancy"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38TCFmethod"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38ErrCorrection"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NSFOverride"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NSFCountryCode"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NSFVendorCode"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NseAckTimeOut"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38FxLCO"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38Redundancy"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38T30ECM"))
)
if mibBuilder.loadTexts:
    t38FaxRelayGroup.setStatus("deprecated")

t38FaxRelayGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 3, 2, 2)
)
t38FaxRelayGroupRev1.setObjects(
      *(("CISCO-WAN-T38-FAXRELAY-MIB", "t38MaxFaxTxRate"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38HsDataPacketSize"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38LsDataRedundancy"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38HsDataRedundancy"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38TCFmethod"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NSFOverride"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NSFCountryCode"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NSFVendorCode"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38NseAckTimeOut"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38FxLCO"),
        ("CISCO-WAN-T38-FAXRELAY-MIB", "t38T30ECM"))
)
if mibBuilder.loadTexts:
    t38FaxRelayGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

t38FaxRelayMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 3, 1, 1)
)
if mibBuilder.loadTexts:
    t38FaxRelayMIBCompliance.setStatus(
        "deprecated"
    )

t38FaxRelayMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 19, 3, 1, 2)
)
if mibBuilder.loadTexts:
    t38FaxRelayMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-T38-FAXRELAY-MIB",
    **{"ciscoWanT38FaxRelayMIB": ciscoWanT38FaxRelayMIB,
       "ciscoWanT38FaxRelayMIBObjects": ciscoWanT38FaxRelayMIBObjects,
       "t38FaxRelayGrp": t38FaxRelayGrp,
       "t38FaxRelayGrpTable": t38FaxRelayGrpTable,
       "t38FaxRelayGrpEntry": t38FaxRelayGrpEntry,
       "t38vismDs1Number": t38vismDs1Number,
       "t38MaxFaxTxRate": t38MaxFaxTxRate,
       "t38FaxInfoFieldSize": t38FaxInfoFieldSize,
       "t38HsDataPacketSize": t38HsDataPacketSize,
       "t38LsDataRedundancy": t38LsDataRedundancy,
       "t38HsDataRedundancy": t38HsDataRedundancy,
       "t38TCFmethod": t38TCFmethod,
       "t38ErrCorrection": t38ErrCorrection,
       "t38NSFOverride": t38NSFOverride,
       "t38NSFCountryCode": t38NSFCountryCode,
       "t38NSFVendorCode": t38NSFVendorCode,
       "t38NseAckTimeOut": t38NseAckTimeOut,
       "t38FxLCO": t38FxLCO,
       "t38Redundancy": t38Redundancy,
       "t38T30ECM": t38T30ECM,
       "t38NotificationPrefix": t38NotificationPrefix,
       "t38Notifications": t38Notifications,
       "t38FaxRelayMIBConformance": t38FaxRelayMIBConformance,
       "t38FaxRelayMIBCompliances": t38FaxRelayMIBCompliances,
       "t38FaxRelayMIBCompliance": t38FaxRelayMIBCompliance,
       "t38FaxRelayMIBComplianceRev1": t38FaxRelayMIBComplianceRev1,
       "t38FaxRelayMIBGroups": t38FaxRelayMIBGroups,
       "t38FaxRelayGroup": t38FaxRelayGroup,
       "t38FaxRelayGroupRev1": t38FaxRelayGroupRev1}
)
