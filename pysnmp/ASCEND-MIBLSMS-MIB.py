# SNMP MIB module (ASCEND-MIBLSMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBLSMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:53 2024
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

_MiblsmsProfile_ObjectIdentity = ObjectIdentity
miblsmsProfile = _MiblsmsProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 150)
)
_MiblsmsProfileTable_Object = MibTable
miblsmsProfileTable = _MiblsmsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 150, 1)
)
if mibBuilder.loadTexts:
    miblsmsProfileTable.setStatus("mandatory")
_MiblsmsProfileEntry_Object = MibTableRow
miblsmsProfileEntry = _MiblsmsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1)
)
miblsmsProfileEntry.setIndexNames(
    (0, "ASCEND-MIBLSMS-MIB", "lsmsProfile-Index-o"),
)
if mibBuilder.loadTexts:
    miblsmsProfileEntry.setStatus("mandatory")
_LsmsProfile_Index_o_Type = Integer32
_LsmsProfile_Index_o_Object = MibScalar
lsmsProfile_Index_o = _LsmsProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 1),
    _LsmsProfile_Index_o_Type()
)
lsmsProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsmsProfile_Index_o.setStatus("mandatory")


class _LsmsProfile_Active_Type(Integer32):
    """Custom type lsmsProfile_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LsmsProfile_Active_Type.__name__ = "Integer32"
_LsmsProfile_Active_Object = MibScalar
lsmsProfile_Active = _LsmsProfile_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 2),
    _LsmsProfile_Active_Type()
)
lsmsProfile_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsmsProfile_Active.setStatus("mandatory")
_LsmsProfile_LsmsIpAddr_Type = IpAddress
_LsmsProfile_LsmsIpAddr_Object = MibScalar
lsmsProfile_LsmsIpAddr = _LsmsProfile_LsmsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 3),
    _LsmsProfile_LsmsIpAddr_Type()
)
lsmsProfile_LsmsIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsmsProfile_LsmsIpAddr.setStatus("mandatory")
_LsmsProfile_NocGatewayIpAddr_Type = IpAddress
_LsmsProfile_NocGatewayIpAddr_Object = MibScalar
lsmsProfile_NocGatewayIpAddr = _LsmsProfile_NocGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 4),
    _LsmsProfile_NocGatewayIpAddr_Type()
)
lsmsProfile_NocGatewayIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsmsProfile_NocGatewayIpAddr.setStatus("mandatory")
_LsmsProfile_Spi_Type = DisplayString
_LsmsProfile_Spi_Object = MibScalar
lsmsProfile_Spi = _LsmsProfile_Spi_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 5),
    _LsmsProfile_Spi_Type()
)
lsmsProfile_Spi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsmsProfile_Spi.setStatus("mandatory")
_LsmsProfile_PresharedKey_Type = DisplayString
_LsmsProfile_PresharedKey_Object = MibScalar
lsmsProfile_PresharedKey = _LsmsProfile_PresharedKey_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 6),
    _LsmsProfile_PresharedKey_Type()
)
lsmsProfile_PresharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsmsProfile_PresharedKey.setStatus("mandatory")


class _LsmsProfile_AllowInsecure_Type(Integer32):
    """Custom type lsmsProfile_AllowInsecure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LsmsProfile_AllowInsecure_Type.__name__ = "Integer32"
_LsmsProfile_AllowInsecure_Object = MibScalar
lsmsProfile_AllowInsecure = _LsmsProfile_AllowInsecure_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 7),
    _LsmsProfile_AllowInsecure_Type()
)
lsmsProfile_AllowInsecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsmsProfile_AllowInsecure.setStatus("mandatory")


class _LsmsProfile_Action_o_Type(Integer32):
    """Custom type lsmsProfile_Action_o based on Integer32"""
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


_LsmsProfile_Action_o_Type.__name__ = "Integer32"
_LsmsProfile_Action_o_Object = MibScalar
lsmsProfile_Action_o = _LsmsProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 150, 1, 1, 8),
    _LsmsProfile_Action_o_Type()
)
lsmsProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lsmsProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBLSMS-MIB",
    **{"DisplayString": DisplayString,
       "miblsmsProfile": miblsmsProfile,
       "miblsmsProfileTable": miblsmsProfileTable,
       "miblsmsProfileEntry": miblsmsProfileEntry,
       "lsmsProfile-Index-o": lsmsProfile_Index_o,
       "lsmsProfile-Active": lsmsProfile_Active,
       "lsmsProfile-LsmsIpAddr": lsmsProfile_LsmsIpAddr,
       "lsmsProfile-NocGatewayIpAddr": lsmsProfile_NocGatewayIpAddr,
       "lsmsProfile-Spi": lsmsProfile_Spi,
       "lsmsProfile-PresharedKey": lsmsProfile_PresharedKey,
       "lsmsProfile-AllowInsecure": lsmsProfile_AllowInsecure,
       "lsmsProfile-Action-o": lsmsProfile_Action_o}
)
