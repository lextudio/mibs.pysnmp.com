# SNMP MIB module (ASCEND-MIBFWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBFWALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:36 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibfwallProfile_ObjectIdentity = ObjectIdentity
mibfwallProfile = _MibfwallProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 79)
)
_MibfwallProfileTable_Object = MibTable
mibfwallProfileTable = _MibfwallProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 79, 1)
)
if mibBuilder.loadTexts:
    mibfwallProfileTable.setStatus("mandatory")
_MibfwallProfileEntry_Object = MibTableRow
mibfwallProfileEntry = _MibfwallProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1)
)
mibfwallProfileEntry.setIndexNames(
    (0, "ASCEND-MIBFWALL-MIB", "fwallProfile-Name"),
)
if mibBuilder.loadTexts:
    mibfwallProfileEntry.setStatus("mandatory")
_FwallProfile_Name_Type = DisplayString
_FwallProfile_Name_Object = MibScalar
fwallProfile_Name = _FwallProfile_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 1),
    _FwallProfile_Name_Type()
)
fwallProfile_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwallProfile_Name.setStatus("mandatory")
_FwallProfile_Version_Type = Integer32
_FwallProfile_Version_Object = MibScalar
fwallProfile_Version = _FwallProfile_Version_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 2),
    _FwallProfile_Version_Type()
)
fwallProfile_Version.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallProfile_Version.setStatus("mandatory")
_FwallProfile_Data_Type = DisplayString
_FwallProfile_Data_Object = MibScalar
fwallProfile_Data = _FwallProfile_Data_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 3),
    _FwallProfile_Data_Type()
)
fwallProfile_Data.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallProfile_Data.setStatus("mandatory")
_FwallProfile_Link_Type = DisplayString
_FwallProfile_Link_Object = MibScalar
fwallProfile_Link = _FwallProfile_Link_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 4),
    _FwallProfile_Link_Type()
)
fwallProfile_Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallProfile_Link.setStatus("mandatory")


class _FwallProfile_Action_o_Type(Integer32):
    """Custom type fwallProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_FwallProfile_Action_o_Type.__name__ = "Integer32"
_FwallProfile_Action_o_Object = MibScalar
fwallProfile_Action_o = _FwallProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 79, 1, 1, 5),
    _FwallProfile_Action_o_Type()
)
fwallProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwallProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBFWALL-MIB",
    **{"DisplayString": DisplayString,
       "mibfwallProfile": mibfwallProfile,
       "mibfwallProfileTable": mibfwallProfileTable,
       "mibfwallProfileEntry": mibfwallProfileEntry,
       "fwallProfile-Name": fwallProfile_Name,
       "fwallProfile-Version": fwallProfile_Version,
       "fwallProfile-Data": fwallProfile_Data,
       "fwallProfile-Link": fwallProfile_Link,
       "fwallProfile-Action-o": fwallProfile_Action_o}
)
